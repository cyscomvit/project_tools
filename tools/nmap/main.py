from project_tools.tools.nmap import utils
from project_tools.tools.nmap.parser import parse
from flask import request, jsonify, make_response, json

def nmap_route():
    # port,type
    body = request#.json#get_json()
    
    print(body)

    port = body.form['port']
    type_scan = body.form['type']
    
    res = nmap(port,type_scan)
    
    #return jsonify(res)
    return res
    #return make_response(jsonify(res), 200)
    #return make_response(json.dumps(res), 200)

def nmap(port,type_scan):

    res = None
    #isValid = parse(port,type_scan);

    #if not isValid["status"]:
        #return { "status": "error", "payload": isValid["payload"] }    

    if type_scan == '1':
        res = utils.synack_scan(port)
    elif type_scan == '2':
        res = utils.udp_scan(port)
    elif type_scan == '3':
        res = utils.comp_scan(port)
    elif type_scan == '4':
        res = utils.reg_scan(port)
    elif type_scan == '5':
        res = utils.ping_scan(port)

    print("RESULT:",res,type(res))
    #print(json.dumps(res))    
    #return { "status": "success", "payload": jsonify(res) }
    return { "status": "success", "payload": res }
    #return { "status": "success", "payload": make_response(jsonify(res), 200)}
    #return { "status": "success", "payload": json.dumps(res) }

    
