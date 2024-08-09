import os
import json



defaults = {
        "NumberOfNodesToProcess": "5000",
        "NumberOfThreadsProcessing": "5"
}

def root_project_path (marker_file='.project_root'):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.isfile(os.path.join(current_dir, marker_file)):
             return current_dir
        new_dir = os.path.abspath(os.path.join(current_dir, os.pardir))    
        if new_dir == current_dir:
            raise Exception("Project root not found")
        current_dir = new_dir

    

def load_config_file_value():
    cfg_file_json = locate_config_file()
    try:
         with open(cfg_file_json, 'r') as init_cfg_file:
              config = json.load(init_cfg_file)
    except FileNotFoundError:
         raise Exception (f"Configuration File {cfg_file_json} not found.")
    except json.JSONDecodeError:
         raise Exception (f"The file{cfg_file_json} contains invalid JSON format")
       
    mandatory_config = config.get("mandatory", {})
    optional_config = config.get("optional", {})

    final_config = {**mandatory_config, **optional_config}

    return final_config
def update_config_file():
    
    return "Empty Function"
    
def locate_config_file():
    
        project_root = root_project_path()
        return os.path.join(project_root,'config.json')

    

