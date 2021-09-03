import validators
import socket 
def parse(input):
    try:
        print(input, "hello")
        socket.inet_aton(str(input))
        # legal
        return {"status":True}
    except socket.error:
        if validators.url(input):
            #legal
            return {"status":True}
        else:
            return {"status":False,"error":"input type not valid"}
