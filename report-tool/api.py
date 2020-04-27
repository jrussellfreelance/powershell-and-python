from waitress import serve
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
import glob,os,json

app = Flask(__name__)
auth = HTTPBasicAuth()
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%m-%d-%Y.%H.%M.%S")
USER_LOGIN = {
    "admin": "testing123"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_LOGIN.get(username) == password
@app.route('/info-store')
@auth.login_required
def list_jsonfiles():
    filelist = []
    for file in os.listdir("./"):
        if file.endswith(".json"):
            filelist.append(file)
    return jsonify(filelist)
@app.route('/info-store/add', methods=['POST'])
@auth.login_required
def add_json():
    try:
        info = request.get_json()
        name = info["CS_Name"]
        with open(name+"_"+timestampStr+'.json', 'w') as outfile:
            json.dump(info, outfile)
            print("json file created")
            return {'message': 'info added successfully'}
    except:
        return {'message': 'an error occurred'}
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8083)