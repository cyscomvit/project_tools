from project_tools.tools.nmap import utils
from project_tools.tools.nmap.parser import parse
from flask import request, jsonify

def nmap_route():
    # port,type
    body = request.get_json()
    
    print(body)

    port = body.get('port')
    type_scan = body.get('type')
    
    res = nmap(port,type_scan)
    
    return jsonify(res)

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
    return { "status": "success", "payload": jsonify(res) }  
    
