import validators
import socket 
def parse(input):
        if validators.url(input):
            return {"status":True}
        else:
            return {"status":False,"error":"input type not valid"}
