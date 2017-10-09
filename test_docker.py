import docker
from datetime import datetime, timedelta
from time import sleep
import uuid


print(uuid.uuid4().hex)
from time import time

print(time())
print(time())
print(time())



c = docker.APIClient()
x = c.create_container('flask-lambda',tty=True,detach=True,
                host_config=c.create_host_config(binds=[
                    '/Users/kshitijsood/code/trunk/assignment_2:/usr/bin/src'
                ]),command="python3.6 /usr/bin/src/t.py")    
print(x)
c.start(x['Id'])
c.stop(x['Id'])
print(c.inspect_container("1")['State']['Status'])
sleep(1)
c.pause(x['Id'])
print(c.inspect_container(x['Id']))
sleep(10)
c.unpause(x['Id'])
print(c.inspect_container(x['Id']))
sleep(10)

#c.remove_container(x['Id'])



# print(x)
# print(x['Id'])
# 
# print(c.logs(x['Id'], timestamps=True,stdout=True, stderr=True, stream=False))
# # x = (c.logs(x['Id'], stdout=True, stderr=True, stream=True))
# # print(next(x))
# # print("=====")
# # print(next(x))
# # print("=====")
# # print(next(x))
# # print("=====")
# # print(next(x))
# # print("=====")
# print(c.logs(x['Id'], stdout=True, stderr=True, stream=False))
# print(c.logs(x['Id'], stdout=True, stderr=True, stream=False))
# from time import sleep
# sleep(3)
# print(c.logs(x['Id'], stdout=True, stderr=True, stream=False))
# sleep(3)
# print(c.logs(x['Id'], stdout=True, stderr=True, stream=False))