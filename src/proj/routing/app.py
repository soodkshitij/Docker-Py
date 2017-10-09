from flask import Flask, request
import json
from proj.utils import utils
from proj.service.service import Service

app = Flask(__name__)
helperService = Service()

@app.route('/api/v1/scripts',methods=['POST'])
def post_file():
    print("inside post")
    file = request.files['data']
    infoObject = utils.store_file(file)
    helperService.store_info_in_db(infoObject)
    return json.dumps({"response":{"script_id":infoObject.script_id}})

@app.route('/api/v1/scripts/create-container/<script_id>',methods=['GET'])
def create_container(script_id):
    infoObject = helperService.create_container(script_id)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state})

@app.route('/api/v1/scripts/start-container/<script_id>',methods=['GET'])
def start_container(script_id):
    infoObject = helperService.start_container(script_id)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state})

@app.route('/api/v1/scripts/read-logs/<script_id>',methods=['GET'])
def read_logs(script_id):
    infoObject,logs = helperService.read_logs(script_id)
    print(logs)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state,"logs":logs})

@app.route('/api/v1/scripts/stop-container/<script_id>',methods=['GET'])
def stop_container(script_id):
    infoObject = helperService.stop_container(script_id)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state})

@app.route('/api/v1/scripts/pause-container/<script_id>',methods=['GET'])
def pause_container(script_id):
    infoObject = helperService.pause_container(script_id)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state})

@app.route('/api/v1/scripts/resume-container/<script_id>',methods=['GET'])
def unpause_container(script_id):
    infoObject = helperService.unpause_container(script_id)
    print(infoObject.__dict__)
    return json.dumps({"response":{"script_id":infoObject.script_id},"container_state":infoObject.state})



if __name__ == '__main__':
    app.run()
