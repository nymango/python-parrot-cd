from flask import Flask, request
app = Flask(__name__)
 
@app.route("/")
def hello():
    return '<form action="/polly/" method="GET"><input name="text"><input type="submit" value="Polly"></form>'
 
@app.route("/orders/")
def orderup():
    return "fulfilled!\n"
@app.route("/polly/")
def echo():
    return "You said " + request.args.get('text','')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
