from flask import Flask
from project_tools.tools.nmap.main import nmap_route

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


# endpoints
app.add_url_rule('/nmap',methods=["POST"], view_func=nmap_route)



if __name__== '__main__':
    app.run(debug=True)