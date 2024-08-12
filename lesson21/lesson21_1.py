from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H2>Hello,傻逼 席XX !</H1>"