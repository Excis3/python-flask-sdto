from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Site under construction <br> <!--Subdomain takeover regarding the Bugbounty program of this asset. more info on /excis3"

@app.route('/excis3')
def poc():
    return "Subdomain Takeover PoC By <a href=https://hackerone.com/excis3>Excis3</a>"

if __name__ == '__main__':
    app.run(debug=True)
