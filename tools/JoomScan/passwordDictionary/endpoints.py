from Joomscan.passwordDictionary.utils.main import Joomscan
from flask import request, jsonify

def index2():
    body = request.get_json()
    print(body)
    res = Joomscan(body.get('a'))
    return jsonify(res)