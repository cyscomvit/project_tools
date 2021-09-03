from project_tools.tools.traceroute_flask.traceroute.utils.main import traceroute


from flask import request, jsonify


def index3():
    print("hi")
    body = request.form["port"]
    print("hi")
    print(body)
    result = traceroute(body)
    return result