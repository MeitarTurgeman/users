from flask import Flask, jsonify

app = Flask('Meitar')

users = [
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com"}
]

@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(users)

app.run()