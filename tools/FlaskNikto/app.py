from Nikto.endpoints import index4
from flask import Flask

app=Flask(__name__)

@app.route('/')

def index():
    return "Hello, World!"

app.add_url_rule('/vulnscan',methods=["POST"], view_func=index4)

if __name__=="__main__":
    app.run(debug=True)