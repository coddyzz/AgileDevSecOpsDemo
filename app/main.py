
from utils import threat_identification,threat_classification,threat_notifications
from flask import Flask, jsonify,request
import subprocess
import json

app = Flask(__name__)

@app.route('/searchplain/<content>', methods=['GET'])
def get_cls(content):
    is_threat = threat_identification(content)
    if is_threat:
        threat_cate, threat_level = threat_classification(content,is_threat)
    else:
        threat_cate = threat_level = None
    return jsonify({'is_threat': is_threat,
        'threat_cate':threat_cate,
        'threat_level':threat_level})


# @app.route('/searchplain/<content>', methods=['GET'])
# def get_cls(content):
#     is_threat = threat_identification(content)
#     if is_threat:
#         threat_cate, threat_level = threat_classification(content,is_threat)
#     else:
#         threat_cate = threat_level = None
#     return jsonify({'is_threat': is_threat,
#         'threat_cate':threat_cate,
#         'threat_level':threat_level})

    
if __name__ == '__main__':
    print('sample command http://127.0.0.1:5001/searchplain/name=agawewe&sdf=wer&4234=3wer222321')
    app.run(host='0.0.0.0')