from flask import Flask, jsonify

app = Flask('Meitar')

users = {
    "1": {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    "2": {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
    "3": {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com"}
}

@app.route('/users', methods=["GET"])
def get_users():
    temp = list(users.values())
    return jsonify(temp)

@app.route('/users/<userid>', methods=["GET"])
def get_user(userid):
    this_user = users.get(str(userid))
    if this_user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(this_user)

app.run()