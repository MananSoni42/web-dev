from flask import Flask, render_template, request
import datetime

def clean_input(s):
    return s.replace('\n','').replace('\r','').strip()

notes = dict()
now = datetime.datetime.now()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("notes.html", name='anonymous')

@app.route("/<string:name>", methods=['GET', 'POST'])
def name_page(name):
    try:
        notes[name]
    except KeyError:
        notes[name] = []

    if request.method == 'POST':
        title = clean_input(request.form.get("note-title"))
        body = clean_input(request.form.get("note-body"))
        if body!='' and title!='':
            notes[name].append({
            "date": f"{now.day} {now.strftime('%b')} {now.year} - {now.hour} : {now.minute}",
            "title": title,
            "body": body
            })

    return render_template("notes.html", name=name, notes=notes[name])

if __name__ == "__main__":
    app.run(debug=True)
