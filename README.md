# assignment_2
# Post file
``sh
curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@test.py" http://localhost:5000/api/v1/scripts
``
Response:
{"response": {"script_id": 776}}

<h4>Create Container</h4>
http://localhost:5000/api/v1/scripts/create-container/776
Response:
{"response": {"script_id": 776}, "container_state": "CREATED"}

<h4>Run container</h4>
http://localhost:5000/api/v1/scripts/start-container/776
Response:
{"response": {"script_id": 776}, "container_state": "RUNNING"}

<h4>Read logs</h4>
http://localhost:5000/api/v1/scripts/read-logs/776
Response:
{"response": {"script_id": 776}, "container_state": "RUNNING", "logs": "hello\r\nbye\r\n"}

<h4>Container Status</h4>
http://localhost:5000/api/v1/scripts/container-stats/776
Response: 
{"response": {"script_id": "776"}, "container_state": "exited"}


<h4>Pause Container</h4>
http://localhost:5000/api/v1/scripts/pause-container/2567
Response:
{"response": {"script_id": 2567}, "container_state": "paused"}

<h4>Resume Container</h4>
http://localhost:5000/api/v1/scripts/resume-container/2567
Response:
{"response": {"script_id": "2567"}, "container_state": "running"}

<h4>Stop Container</h4>
http://localhost:5000/api/v1/scripts/stop-container/2567
Response:
{"response": {"script_id": 2567}, "container_state": "exited"}

<h4>Delete Container</h4>
http://localhost:5000/api/v1/scripts/delete-container/2567
Response:
{"response": {"script_id": "2567"}, "container_state": "DELETED"}
