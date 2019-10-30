from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/signup", methods=['GET'])
def sign_up():
    return render_template("sign_up.html")

@app.route("/login", methods=['GET'])
def log_in():
    return render_template("log_in.html")

if __name__ == '__main__':
    app.run(debug=True)
