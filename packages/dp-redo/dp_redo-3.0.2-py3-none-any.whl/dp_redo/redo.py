from .logging import get_logger
from .version import __version__
import inspect, hashlib, atexit, os, sys, json, shutil

logger = get_logger()

# All targets functions keyed by names
targets = {}
json_info = {}

REDO_DATA_DIR_NAME = ".redo"
REDO_DATA_FILE_NAME = "info.json"
source_tree = os.path.dirname(os.path.abspath(sys.argv[0]))
build_tree = os.getcwd()
redo_data_dir = os.path.join(build_tree, REDO_DATA_DIR_NAME)
redo_data_path = os.path.join(redo_data_dir, REDO_DATA_FILE_NAME)

exit_code = 1
sys_exit = sys.exit

def new_exit(code):
    global exit_code
    exit_code = code
    sys_exit()

sys.exit = new_exit

class Target():
    def __init__(self, func, output_name, last_info):
        self.name = func.__name__
        self.__func = func
        self.output_name = output_name
        self.__info = last_info
        self.digest = self.__digest(func)
        self.__updated_target_deps = []
        self.__updated_source_deps = []

        if "target_deps" not in self.__info:
            self.__info["target_deps"] = {}

        if "source_deps" not in self.__info:
            self.__info["source_deps"] = {}
    
    def add_target_dep(self, dep):
        self.__updated_target_deps.append(dep)

    def add_source_dep(self, dep):
        dep = os.path.join(source_tree, dep.strip())
        if not os.path.exists(dep):
            logger.error("Cannot find source file: %s", dep)
            exit(1)

        self.__updated_source_deps.append(dep)

    def redo_ifchange(self, target_name, target_base_name):
        need_redo = False
        redo_reason = ""
        output_path =  os.path.join(build_tree, target_name)
        if "digest" not in self.__info or self.__info["digest"] != self.digest:
            need_redo = True
            self.__info["digest"] = self.digest
            redo_reason = "It's python code has changed"

        if need_redo == False:
            if not os.path.exists(output_path):
                need_redo = True
                redo_reason = "The target file doesn't exist"

        if need_redo == False:
            for dep in self.__info["source_deps"]:
                dep_path = os.path.join(source_tree, dep)
                if not os.path.exists(dep_path) or \
                    abs(self.__info["source_deps"][dep] - os.path.getmtime(dep_path)) > 0.001:
                        need_redo = True
                        redo_reason = "Source {} has been modified".format(dep)
                        break
        
        if need_redo == False:
            for dep in self.__info["target_deps"]:
                target_path = os.path.join(build_tree, dep)
                if not os.path.exists(target_path) or \
                    abs(self.__info["target_deps"][dep] - os.path.getmtime(target_path)) > 0.001:
                    need_redo = True
                    redo_reason = "Target {} has been modified".format(dep)
                    break

                need_redo = find_target_by_output_name(dep).redo_ifchange(target_name, target_base_name) or need_redo
        
        redoing_tmp_name = output_path + "---redoing"
        print(redoing_tmp_name)
        if need_redo:
            logger.info("Redoing target: %s. Reason: %s", self.name, redo_reason)
            self.__func(target_name, target_base_name, redoing_tmp_name)
            
            self.__info["source_deps"] = {}
            for source_dep in self.__updated_source_deps:
                self.__info["source_deps"][source_dep] = os.path.getmtime(os.path.join(source_tree, source_dep))
            
            self.__info["target_deps"] = {}
            for target_dep in self.__updated_target_deps:
                self.__info["target_deps"][target_dep] = os.path.getmtime(os.path.join(build_tree, target_dep))

            if os.path.exists(redoing_tmp_name):
                shutil.move(redoing_tmp_name, output_path)
            else:
                logger.warning("%s didn't generate any target file.", self.name)
        else:
            logger.info("Skipping target %s: it's up to date.", self.name)

    def __digest(self, func):
        md5 = hashlib.md5()
        for v in dir(func.__code__):
            if not v.startswith("co_") or v == "co_firstlineno":
                continue
            md5.update(str(func.__code__.__getattribute__(v)).encode(encoding="utf-8"))
        return md5.hexdigest()


def do(output_name):
    def register(func):
        if func.__name__ in targets:
            logger.error("Duplicate targets found: %s", output_name)
            exit(1)

        if func.__code__.co_argcount != 3:
            logger.error("Target method must receive 3 arguments")
            exit(1)
        
        if func.__name__ not in json_info:
            json_info[func.__name__] = {}

        targets[func.__name__] = Target(func, output_name, json_info[func.__name__])
        return func
    return register

def redo_ifchange(*deps):
    caller = inspect.stack()[1].function
    for dep in deps:
        if isinstance(dep, str):
            dep = dep.strip()
            source_file = os.path.join(source_tree, dep)
            if os.path.exists(source_file):
                source_dep(caller, dep)
            else:
                target = find_target_by_output_name(dep)
                if target == None:
                    logger.error("Cannot find target %s", dep)
                    exit(1)

                target_dep(caller, target, dep)
        else:
            if dep.__name__ not in targets:
                logger.error("redo_ifchange must be applied to a target. Invalid function: %s", dep.__name__)
                exit(1)
            
            target_dep(caller, targets[dep.__name__], targets[dep.__name__].output_name)

def source_dep(caller, dep_name):
    if caller != "<module>":
        targets[caller].add_source_dep(dep_name)

def target_dep(caller, target, target_name):
    if caller != "<module>":
        targets[caller].add_target_dep(target_name)

    target_base_name, _ = os.path.splitext(os.path.basename(target_name))
    target.redo_ifchange(target_name, target_base_name)

def find_target_by_output_name(output_name):
    # If the file is not found in the source tree, treat it as a target
    for name in targets:
        if targets[name].output_name == output_name:
            return targets[name]
    
    # Search the defaults
    _, ext = os.path.splitext(output_name)
    for name in targets:
        if targets[name].output_name == ext:
            return targets[name]

def flush_info():
    if exit_code != 0:
        return

    if not os.path.exists(redo_data_dir):
        os.mkdir(redo_data_dir)

    with open(redo_data_path, mode='w', encoding='utf-8') as json_file:
        json.dump(json_info, json_file)

def load_info():
    global json_info
    if os.path.exists(redo_data_path):
        with open(redo_data_path, encoding='utf-8') as json_file:
            try:
                json_info = json.load(json_file)
            except Exception as e:
                logger.warning("info.json is corrupted - ignoring it.")

load_info()
atexit.register(flush_info)
