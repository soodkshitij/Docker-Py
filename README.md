# assignment_2

##### Build flask-lambda image using docker file.To use any other image change config.ini
##### Build egg or add project in pypath
##### Install docker sdk, flask and rocksdb

### Post file
```bash
curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@test.py" http://localhost:5000/api/v1/scripts
```
### Response:
```json
{"response": {"script_id": 776}}
```
### Create Container
```http
GET : http://localhost:5000/api/v1/scripts/create-container/776
```
### Response:
```json
{"response": {"script_id": 776}, "container_state": "CREATED"}
```
### Run container
```http
GET : http://localhost:5000/api/v1/scripts/start-container/776
```
### Response:
```json
{"response": {"script_id": 776}, "container_state": "RUNNING"}
```
### Read logs
```http
GET : http://localhost:5000/api/v1/scripts/read-logs/776
```
### Response:
```json
{"response": {"script_id": 776}, "container_state": "RUNNING", "logs": "hello\r\nbye\r\n"}
```
### Container Status
```http
GET http://localhost:5000/api/v1/scripts/container-stats/776
```
### Response:
```json
{"response": {"script_id": "776"}, "container_state": "exited"}
```

### Pause Container
```http
GET http://localhost:5000/api/v1/scripts/pause-container/2567
```
### Response:
```json
{"response": {"script_id": 2567}, "container_state": "paused"}
```
### Resume Container
```http
GET http://localhost:5000/api/v1/scripts/resume-container/2567
```
### Response:
```json
{"response": {"script_id": "2567"}, "container_state": "running"}
```
### Stop Container
```http
GET http://localhost:5000/api/v1/scripts/stop-container/2567
```
### Response:
```json
{"response": {"script_id": 2567}, "container_state": "exited"}
```
### Delete Container
```http
GET http://localhost:5000/api/v1/scripts/delete-container/2567
```
### Response:
```json
{"response": {"script_id": "2567"}, "container_state": "DELETED"}
```
