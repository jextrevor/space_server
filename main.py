from flask import Flask,render_template, redirect, url_for
from flask_socketio import SocketIO
import os
from gevent import monkey
monkey.patch_all()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tamaalgasdfasd;fajsdfkljasdfkljasdf'
socketio = SocketIO(app, async_mode='gevent')
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