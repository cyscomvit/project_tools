import validators
import socket 
def parse(input):
    try:
        socket.inet_aton(input)
        # legal
        return {"status":True}
    except socket.error:
        if validators.url(input):
            #legal
            return {"status":True}
        else:
            return {"status":False,"error":"input type not valid"}
