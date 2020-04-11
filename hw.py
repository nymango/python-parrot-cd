from flask import Flask, request
app = Flask(__name__)
 
@app.route("/")
def hello():
    return '<form action="/echo/" method="POST"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/orders/")
def orderup():
    return "fulfilled!\n"

@app.route("/echo/", methods=['POST'])
def echo():
# You can access the values passed in the URL via request.args and the values passed in a POST-request via request.form
# The recommended way to access the values is via request.args.get('key', '') for GET requests and request.form['key'] for POST. 
    return "Your name is " + request.form['text']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
