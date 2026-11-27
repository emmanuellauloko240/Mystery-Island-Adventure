import secrets

from flask import Flask, render_template, request
from flask_socketio import (
    SocketIO,
    join_room as socketio_join_room,
    emit
)


# -------------------------
# APP CONFIGURATION
# -------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mystery-island-secret'

socketio = SocketIO(app)

rooms = {}


# -------------------------
# HOME PAGE
# -------------------------

@app.route('/')
def home():
    return render_template('index.html')


# -------------------------
# CREATE GAME ROOM
# -------------------------

@app.route('/create-room', methods=['POST'])
def create_room():
    player_name = request.form.get('player_name')

    room_code = secrets.token_hex(3).upper()

    rooms[room_code] = {
        'players': [player_name],
        'status': 'waiting',
        'current_location': None,
        'treasure_found': False,
        'winner': None,

        'enemies': {
            'forest': {
                'name': 'Wild Beast',
                'hp': 30
            },
            'cave': {
                'name': 'Cave Monster',
                'hp': 50
            },
            'temple': {
                'name': 'Temple Guardian',
                'hp': 100
            }
        }
    }

    return render_template(
        'lobby.html',
        room_code=room_code,
        players=rooms[room_code]['players'],
        status=rooms[room_code]['status']
    )


# -------------------------
# JOIN GAME ROOM
# -------------------------

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


# -------------------------
# GAME PAGE
# -------------------------

@app.route('/game/<room_code>')
def game_page(room_code):
    if room_code not in rooms:
        return "Room does not exist!"

    return render_template(
        'game.html',
        room_code=room_code,
        players=rooms[room_code]['players']
    )


# -------------------------
# SOCKET.IO CONNECTION
# -------------------------

@socketio.on('connect')
def handle_connect():
    print('A player connected!')


# -------------------------
# JOIN SOCKET.IO ROOM
# -------------------------

@socketio.on('join_game_room')
def handle_join_game_room(data):
    print("Received join_game_room event:", data)

    room_code = data.get('room_code')

    if room_code not in rooms:
        emit('room_error', {
            'message': 'Room does not exist!'
        })
        return

    socketio_join_room(room_code)

    print(f'A player joined room {room_code}!')

    emit('room_update', {
        'players': rooms[room_code]['players'],
        'status': rooms[room_code]['status'],
        'enemies': rooms[room_code]['enemies']
    }, to=room_code)


# -------------------------
# SELECT ENEMY
# -------------------------

@socketio.on('select_enemy')
def handle_select_enemy(data):
    room_code = data.get('room_code')
    location = data.get('location')

    if room_code not in rooms:
        return

    if location not in rooms[room_code]['enemies']:
        return

    rooms[room_code]['current_location'] = location

    enemy = rooms[room_code]['enemies'][location]

    emit('enemy_selected', {
        'location': location,
        'enemy': enemy
    }, to=room_code)


# -------------------------
# ATTACK ENEMY
# -------------------------

@socketio.on('attack_enemy')
def handle_attack_enemy(data):
    room_code = data.get('room_code')

    if room_code not in rooms:
        return

    location = rooms[room_code].get('current_location')

    if not location:
        return

    enemy = rooms[room_code]['enemies'][location]

    if enemy['hp'] <= 0:
        return

    enemy['hp'] = max(0, enemy['hp'] - 5)

    emit('enemy_health_update', {
        'location': location,
        'enemy': enemy
    }, to=room_code)


# -------------------------
# RUN APPLICATION
# -------------------------

if __name__ == '__main__':
    socketio.run(app, debug=True)