from flask import Flask
from traceroute.endpoints import index3
app=Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

app.add_url_rule('/trace-route',methods=["POST"], view_func=index3)

if __name__== '__main__':
    app.run(debug=True)
