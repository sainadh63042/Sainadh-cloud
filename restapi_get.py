from flask import Flask, jsonify

app = Flask(__name__)

# Sample cricket players data
cricket_players = [
    {"id": 1, "name": "Virat Kohli", "country": "India", "role": "Batsman"},
    {"id": 2, "name": "Kane Williamson", "country": "New Zealand", "role": "Batsman"},
    {"id": 3, "name": "Joe Root", "country": "England", "role": "Batsman"},
    # Add more players here
]


@app.route('/api/cricket/players', methods=['GET'])
def get_all_cricket_players():
    return jsonify(cricket_players)


@app.route('/api/cricket/players/<int:player_id>', methods=['GET'])
def get_player_by_id(player_id):
    player = next((p for p in cricket_players if p['id'] == player_id), None)
    if player:
        return jsonify(player)
    return jsonify({"message": "Player not found"}), 404


@app.route('/api/cricket/players/country/<country>', methods=['GET'])
def get_players_by_country(country):
    players_in_country = [p for p in cricket_players if p['country'].lower() == country.lower()]
    if players_in_country:
        return jsonify(players_in_country)
    return jsonify({"message": "No players found for the given country"}), 404


if __name__ == '__main__':
    app.run(debug=True)
 
