from flask import Flask
from Joomscan.passwordDictionary.endpoints import index3

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


# endpoints
app.add_url_rule('/Joomscan',methods=["POST"], view_func=index3)


if __name__== '__main__':
    app.run(debug=True)