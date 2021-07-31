import project_tools.tools.nmap.nmap.nmap as nm
from flask import jsonify

scanner = nm.PortScanner()

def synack_scan(p):
    res = { "info": "", "IP Status": "", "Protocols": "", "Open Ports": "" }
    scanner.scan(p, '1-1024', '-v -sS');

    res["info"] = jsonify(scanner.scaninfo())  
    res["IP Status"] = jsonify(scanner[p].state())
    res["Protocols"] = jsonify(scanner[p].all_protocols())
    res["Open Ports"] = jsonify(scanner[p]['tcp'].keys())

    return res

def udp_scan(p):
    res = { "info": "", "IP Status": "", "Protocols": "", "Open Ports": "" }
    scanner.scan(p, '1-1024', '-v -sU')
    
    res["info"] = scanner.scaninfo()
    res["IP Status"] = scanner[p].state()
    res["Protocols"] = scanner[p].all_protocols()
    res["Open Ports"] = scanner[p]['udp'].keys()

    return res

def comp_scan(p):
    res = { "info": "", "IP Status": "", "Protocols": "", "Open Ports": "" }
    scanner.scan(p, '1-1024', '-v -sS -sV -sC -A -O')

    res["info"] = scanner.scaninfo()  
    res["IP Status"] = scanner[p].state()
    res["Protocols"] = scanner[p].all_protocols()
    res["Open Ports"] = scanner[p]['tcp'].keys()

    return res    

def reg_scan(p):
    res = { "info": "", "IP Status": "", "Protocols": "", "Open Ports": "" }
    scanner.scan(p)

    res["info"] = scanner.scaninfo()  
    res["IP Status"] = scanner[p].state()
    res["Protocols"] = scanner[p].all_protocols()
    res["Open Ports"] = scanner[p]['tcp'].keys()

    return res

def ping_scan(p):
    res = { "Info": "" }
    scanner.scan(hosts=p, arguments='-n -sP -PE -PA21,23,80,3389')

    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    counter = 0
    info = {}
    for host, status in hosts_list:
        info[host] = status
        counter += 1
    if counter == 0:
        res["info"] = "Either the host is down or the system is private"

    res["Info"] = jsonify(info)

    return res

    
    


