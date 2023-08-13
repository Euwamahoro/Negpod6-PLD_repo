import json

def register(username, password):
    users = load_users()
    if username not in users:
        users[username] = {'password': password}
        save_users(users)
        return True
    return False
