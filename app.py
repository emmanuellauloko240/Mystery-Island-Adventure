import secrets
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room as socketio_join_room, emit

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

    room_code = secrets.token_hex(3).upper()

    rooms[room_code] = {
    'players': [player_name],
    'status': 'waiting'
}

    return render_template(
        'lobby.html',
        room_code=room_code,
        players=rooms[room_code]['players'],
        status=rooms[room_code]['status']
    )
@app.route('/join-room', methods=['POST'])
def join_room():
    player_name = request.form.get('player_name')
    room_code = request.form.get('room_code')

    if room_code not in rooms:
        return "Room does not exist!"

    if len(rooms[room_code]['players']) >= 2:
        return "Room is full!"

    rooms[room_code]['players'].append(player_name)

    rooms[room_code]['status'] = 'ready'

    return render_template(
        'lobby.html',
        room_code=room_code,
        players=rooms[room_code]['players'],
        status=rooms[room_code]['status']
    )

@socketio.on('connect')

def handle_connect():
    print('A player connected!')

@socketio.on('join_game_room')
def handle_join_game_room(data):
    print("Received join_game_room event:", data)
    room_code = data.get('room_code')

    if room_code not in rooms:
        emit('room_error', {'message': 'Room does not exist!'})
        return

    socketio_join_room(room_code)

    print(f'A player joined room {room_code}!')

if __name__ == '__main__':
    socketio.run(app, debug=True)
