from project_tools.tools.JoomScan.passwordDictionary.utils.main import Joomscan
from flask import request, jsonify, json

def index2():
    
    body1 = request.form.get('a')
    print(body1)
    #print(body1)
    #a='www.google.com'
    res = Joomscan(body1)
    return res
    #return jsonify(res)