from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def index():
    print("hello index")
    #return "hello world"
    return render_template('index.html')

@socketio.event
def my_event(message):
    emit('my response', {'data': 'got it!'})

@socketio.event
def chatMessage(message):
    print(message)
    emit("response", {'data': time.time()})

if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", 5000)
    print("app start")