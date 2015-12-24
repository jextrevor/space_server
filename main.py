from flask import Flask,render_template, redirect, url_for
from flask_socketio import SocketIO, emit
import os
import eventlet
from gevent import monkey
from module import Module
monkey.patch_all()
eventlet.monkey_patch()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tamalaygaolaotaykhap'
socketio = SocketIO(app, async_mode='eventlet')
@socketio.on('connect', namespace='/main')
def connect():
    emit("connected","connected", broadcast=True)
@socketio.on("ping", namespace="/main")
def ping(data):
    if data == "ping":
        emit("ping","hi")
@socketio.on_error('/main') # handles the '/chat' namespace
def error(e):
    print e
@app.route("/")
def home():
    templateData = {
        }
    return render_template('home.html', **templateData)
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))
@app.errorhandler(500)
def internalerror(error):
    return "500 Error"
@app.after_request
def no_cache(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store'
    response.headers['Pragma'] = 'no-cache'
    return response
if __name__ == '__main__':
    print "Server running"
    if 'PORT' in os.environ:
        socketio.run(app, "0.0.0.0",int(os.environ['PORT']))
    else:
        socketio.run(app, "0.0.0.0", 3000)