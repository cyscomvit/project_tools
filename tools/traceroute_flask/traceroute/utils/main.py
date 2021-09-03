from project_tools.tools.traceroute_flask.traceroute.utils.parser import parse
from scapy.all import ICMP,sr1,IP
def traceroute(hostname):
    print(hostname)
    res=parse(hostname)
    if not res.get("status"):
        return {"status":"Error","payload": res.get("error")} 
    ans={}
    i=1
    temp=0
    init_time=0
    final=sr1(IP(dst=hostname)/ICMP(),verbose=0)
    if final.src==None:
        return {"status":"Not Found","payload": "None"}
    while(1):
        pkt = IP(dst=hostname, ttl=i)/ICMP()
        reply = sr1(pkt, verbose=0,timeout=2)
        if(i==1):
            init_time=reply.time
        if reply is None:
            i+=1
            continue
        if reply.src==final.src:
            ans[i]=[reply.src,(reply.time-init_time)*1000]
            return ans
        if reply.src==temp:
            i+=1
        else:
            temp=reply.src
            i+=1
        ans[(i-1)]= [reply.src, (reply.time-init_time)*1000]