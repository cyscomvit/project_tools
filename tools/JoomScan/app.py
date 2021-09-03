from flask import Flask
from flask import render_template,redirect,url_for,flash
from JoomScan.passwordDictionary.endpoints import index2


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/Joomscan',methods=['POST'])
def joomscan():
    print("called")
    
    res = index2()
    print(res)
    return redirect(url_for('/'))

# endpoints
#app.add_url_rule('/Joomscan',methods=["POST"], view_func=index2)


if __name__== '__main__':
    app.run(debug=True)