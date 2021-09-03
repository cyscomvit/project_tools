from project_tools.tools.FlaskNikto.Nikto.utils.vulnerability_scanner import vulscan
from flask import request, jsonify


def index4():
    body = request.form["port"]
    print(body)
    res = vulscan(body)
    print(res)
    return res