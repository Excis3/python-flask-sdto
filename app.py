from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "under construction"

@app.route("/excis3")
def hello():
    return "Subdomain Takeover PoC By <a href=https://hackerone.com/excis3>Excis3</a>"

if __name__ == '__main__':
   app.run()
