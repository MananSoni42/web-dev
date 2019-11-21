from flask import Flask, render_template, request, session, redirect, url_for, Markup
app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"

names = []

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/addName", methods=['GET'])
def add_name():
    name = request.args.get('name')
    print(name)
    names.append(name)

@app.route("/getNames", methods=['GET'])
def get_name():
    return names

if __name__ == '__main__':
    app.run(debug=True,port=5000)
