import json

def register(username, password):
    users = load_users()
    if username not in users:
        users[username] = {'password': password}
        save_users(users)
        return True
    return False
    
def login(username, password):
    users = load_users()
    if username in users and users[username]['password'] == password:
        return True
    return False
