from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    html = "Site under construction <br> <!--Subdomain takeover regarding the Bugbounty program of this asset. more info on /excis3"
    return html

@app.route('/excis3')
def poc():
    html = "Subdomain Takeover PoC By <a href=https://hackerone.com/excis3>Excis3</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
