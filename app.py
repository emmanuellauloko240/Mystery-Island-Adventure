
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mystery-island-secret'

socketio = SocketIO(app)
rooms = {}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create-room', methods=['POST'])
def create_room():
    player_name = request.form.get('player_name')

    return f"Welcome {player_name}! Your room is being created."


@app.route('/join-room', methods=['POST'])
def join_room():
    player_name = request.form.get('player_name')
    room_code = request.form.get('room_code')

    return f"Welcome {player_name}! You entered room {room_code}."


if __name__ == '__main__':
    socketio.run(app, debug=True)
