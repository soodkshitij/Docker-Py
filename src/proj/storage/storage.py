from proj.utils import utils
import rocksdb
from random import randint
encoding = "UTF-8"

class Storage():
    
    _scriptId = randint(0,1000)
    _db = rocksdb.DB("lab1.db", rocksdb.Options(create_if_missing=True))
        
    @utils.custom_serialze
    def store(self, info_object, script_id):
        print(Storage._scriptId)
        print(info_object)
        print(type(info_object))
        Storage._db.put(bytes(str(script_id),encoding),info_object)
    
    @utils.custom_deserialize
    def get_from_db(self, info_object):
        print(info_object.__dict__)
        return info_object

    def retrieve(self, script_id):
        return self.get_from_db(Storage._db.get(bytes(script_id,encoding)))
    
    def generate_random_script_id(self):
        Storage._scriptId = Storage._scriptId + randint(0,1000)
        return Storage._scriptId
    
    def delete(self, script_id):
        Storage._db.delete(bytes(str(script_id),encoding))
