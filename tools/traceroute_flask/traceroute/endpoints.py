from traceroute.utils.main import traceroute
from flask import request, jsonify


def index3():
    body = request.get_json()
    print(body)
    result = traceroute(body.get('hostname'))
    return jsonify(res)