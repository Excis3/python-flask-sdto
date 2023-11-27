from flask import Flask
app = Flask(__name__)

@app.route("/excis3")
def hello():
    return "Subdomain Takeover PoC By Excis3"
