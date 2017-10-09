import docker
from proj.utils import utils

class Container():
    
    _client = docker.APIClient()
    
    
    def create_container(self, file_name ):
        print(file_name)
        print(utils.get_property("volume_host"))
        print(utils.get_property("volume_docker"))
        container = self._client.create_container(utils.get_property("base_image"),tty=True,detach=True,
                host_config=self._client.create_host_config(binds=[
                     utils.get_property("volume_host")+":"+utils.get_property("volume_docker")
                 ]),command="python3.6 "+ utils.get_property("volume_docker")+"/"+file_name)    
        return container
    
    
    def run_container(self,container):
        self._client.start(container)
        
    
    def get_logs(self,container_id):
        return self._client.logs(container_id, timestamps=False,stdout=True, stderr=True)
    
    def delete_container(self,container_id):
        self._client.remove_container(container_id)
        
    def stop_container(self,container_id):
        self._client.stop(container_id, timeout=30)
        
    def pause_container(self,container_id):
        self._client.pause(container_id)
        
    def unpause_container(self,container_id):
        self._client.unpause(container_id)
        
    def get_container_stats(self,container_id):
        return self._client.inspect_container(container_id)
    