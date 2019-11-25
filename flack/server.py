from flask import Flask, render_template, request, session, redirect, url_for, Markup
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.secret_key = "RandOM PasSwoRd"
socketio = SocketIO(app)

channels = [];
messages = dict()

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/")
def inital_emit():
    emit("getChannels", {"channel": channels});

@socketio.on("addMessage")
def add_message(data):
    channel = data['channel']
    name = data['name']
    message = data['message']
    messages[channel].append([name,message])
    channel_names = [c[0] for c in channels]
    channels[int(channel_names.index(channel))][1] += 1
    print(channels)
    socketio.emit("newMessage", {"message": [name,message,channel], "channels": channels}, broadcast=True)
    return ""


@socketio.on("addChannel")
def add_channel(data):
    channels.append([data['channel'],0])
    print(channels)
    messages[data['channel']] = []
    socketio.emit("getChannels", {"channel": channels}, broadcast=True)
    return ""

@app.route("/getChannels", methods=['GET'])
def get_channels():
    print(channels)
    return {'channels': channels}

@app.route("/getMessages", methods=['POST'])
def get_messages():
    channel = json.loads(list(request.form.to_dict())[0])['channel']
    return {'messages': messages[channel]}

if __name__ == '__main__':
    app.run(debug=True,port=5000)
