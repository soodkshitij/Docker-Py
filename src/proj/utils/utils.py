from functools import wraps
import uuid
import pickle
from enum import Enum
import configparser
import os

config = configparser.ConfigParser()
config.read("../config/config.ini")

config_dic = {}

for option in config['DEFAULT']:
    config_dic[option] = config.get('DEFAULT', option, raw=True)

print(config_dic)

class ContainerState(Enum):
    CREATED = 1
    RUNNING = 2
    STOPPED = 3
    DELETED = 4 
    PAUSE = 5

class InfoObject():
    
    def __init__(self, file_name, script_id=None, container_id=None, state = None):
        self.file_name = file_name
        self.script_id = script_id
        self.container_id = container_id
        self.state = state

def get_property(property_name):
    return config_dic.get(property_name,"")

def custom_serialze(func):
    print("Inside custom_serialzed")
    @wraps(func)
    def serialize(*args):
        print("args",args)
        nargs = (args[0],pickle.dumps(args[1]),args[2])
        func(*nargs)
    return serialize

def custom_deserialize(func):
    print("Inside custom_deserialize")
    @wraps(func)
    def deserialize(*args):
        print(args)
        nargs = (args[0],pickle.loads(args[1]))
        return func(*nargs)
    return deserialize


def store_file(file,location=config_dic.get("upload_path")):
    name = uuid.uuid4().hex
    print(name)
    print(location)
    file.save(os.path.join(location, name))
    return InfoObject(name)

    