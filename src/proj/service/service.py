from proj.storage.storage import Storage
from proj.container.ContainerService import Container
from proj.utils import utils

class Service():
    
    @staticmethod
    def store_info_in_db(info_object):
        info_object.script_id = Storage().generate_random_script_id()
        Storage().store(info_object, info_object.script_id)
        
        
    @staticmethod
    def update_info_in_db(info_object):
        Storage().store(info_object, info_object.script_id)
    
    
    @staticmethod
    def get_info_from_db(script_id):
        return Storage().retrieve(script_id)
    
    @staticmethod
    def delete_info_from_db(script_id):
        return Storage().delete(script_id)
    
    
    @staticmethod
    def get_container_status(script_id):
        info_obj = Service.get_info_from_db(script_id)
        stats = Container().get_container_stats(info_obj.container_id)
        return stats['State']['Status']
    
    @staticmethod
    def create_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        container = Container().create_container(info_obj.file_name)
        info_obj.container_id = container['Id']
        info_obj.state = utils.ContainerState.CREATED.name
        Service.update_info_in_db(info_obj)
        return info_obj
    
    @staticmethod
    def start_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        Container().run_container(info_obj.container_id)
        info_obj.state = utils.ContainerState.RUNNING.name
        return info_obj
    
    @staticmethod
    def read_logs(script_id):
        info_obj = Service.get_info_from_db(script_id)
        logs = Container().get_logs(info_obj.container_id)
        return info_obj, logs.decode("utf-8") 
    
    @staticmethod
    def delete_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        Container().delete_container(info_obj.container_id)
        Service.delete_info_from_db(script_id)
        info_obj.state = utils.ContainerState.DELETED.name
        return info_obj
    
    @staticmethod
    def stop_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        Container().stop_container(info_obj.container_id)
        info_obj.state = utils.ContainerState.STOPPED.name
        return info_obj
    
    @staticmethod
    def pause_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        Container().pause_container(info_obj.container_id)
        info_obj.state = utils.ContainerState.PAUSE.name
        return info_obj
    
    @staticmethod
    def unpause_container(script_id):
        info_obj = Service.get_info_from_db(script_id)
        Container().unpause_container(info_obj.container_id)
        info_obj.state = utils.ContainerState.RUNNING.name
        return info_obj
    
        
        