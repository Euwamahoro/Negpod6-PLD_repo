import mysql.connector
import json
import os

def connect_to_database():
    connection = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        database="sql6640257",
        user="sql6640257",
        password="eGZJlSaF6b",
        port=3306
    )

    if connection.is_connected():
        print("Connection successful!")
    else:
        print("Connection failed!")

    return connection

def close_connection(connection):
    connection.close()

def register(username, password):
    connection = connect_to_database()

    # Check if the username already exists
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)
    users = cursor.fetchall()

    if len(users) == 0:
        # Username does not exist, so we can register the user
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        connection.commit()
        return True
    else:
        # Username already exists
        return False

def login(username, password):
    connection = connect_to_database()

    # Check if the username and password match
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    users = cursor.fetchall()

    if len(users) == 1:
        # Username and password match
        return True
    else:
        # Username and password do not match
        return False

def load_users():
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if the file is missing or empty


def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file)




