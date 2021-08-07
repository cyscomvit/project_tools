from Nikto.utils.vulnerability_scanner import vulscan
from flask import request, jsonify


def index4():
    body = request.get_json()
    print(body)
    res = vulscan(body.get('hostname'))
    return jsonify(res)