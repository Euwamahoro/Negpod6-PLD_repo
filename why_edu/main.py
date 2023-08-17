#!/usr/bin/env python3

import user
import features
import random
import json
import webbrowser
import os




def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user.register(username, password):
        print("Registration successful!")
    else:
        print("Username already exists.")

def login_user(video_data):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user.login(username, password):
        print("Login successful!")
        user_features(username, video_data)
    else:
        print("Login failed. Incorrect username or password.")


def watch_videos(video_data):
    print("\nAvailable Videos:")
    for i, video in enumerate(video_data, start=1):
        print(f"{i}. {video['title']}")

    video_choice = input("Enter the number of the video you want to watch: ")
    try:
        video_choice = int(video_choice)
        if 1 <= video_choice <= len(video_data):
            selected_video = video_data[video_choice - 1]
            print(f"Now watching: {selected_video['title']}")
            print("Video URL:", selected_video['url'])
            webbrowser.open(selected_video['url'])  # Open the video URL in a web browser
        else:

             print("Invalid video number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def user_features(username, video_data):
    while True:
        print("\nWelcome, " + username + "!")
        print("1. Get Educational Quote")
        print("2. Get Testimonial")
        print("3. Watch Videos")
        print("4. Chat with Users")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            quotes = features.get_quotes()
            random_quote = random.choice(quotes)
            print("Educational Quote:")
            print(random_quote)

        elif choice == '2':
            testimonials = features.get_testimonials()
            random_testimonial = random.choice(testimonials)
            print("Testimonials:")
            print(random_testimonial)

        elif choice == '3':
            watch_videos(video_data)
        elif choice == '4':
            chat_with_users(username)

        elif choice == '5':
            print("Logout successful!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


def chat_with_users(username):

    # Check if chat messages file exists
    if not os.path.exists('chat_messages.txt'):
        with open('chat_messages.txt', 'w'):
            pass

    # Read chat messages from file
    with open('chat_messages.txt', 'r') as file:
        chat_messages = file.readlines()

    # Print chat messages
    for chat in chat_messages:
        sender, message = chat.split(':')
        if sender == username:
            print(f"You: {message}")
        else:
            print(f"{sender}: {message}")

    # Get new message from user
    new_message = input("Enter your message (or 'exit' to return to features): ")

    # Check if user wants to exit
    if new_message.lower() == "exit":
        print("Exiting chat...")
        return

    # Save new message to file
    with open('chat_messages.txt', 'a') as file:
        file.write(f"{username}: {new_message}\n")


def get_messages():
    connection = connect_to_database()

    cursor = connection.cursor()
    query = "SELECT * FROM chat_messages"
    cursor.execute(query)
    messages = cursor.fetchall()

    return messages

def save_message(message, sender):
    connection = connect_to_database()

    query = "INSERT INTO chat_messages (message, sender) VALUES (%s, %s)"
    values = (message, sender)
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()

def main():
    global chat_messages
    chat_messages = []  # Initialize chat messages

    with open('data/videos/video_data.json', 'r') as video_file:
        video_data = json.load(video_file)

    while True:
        print("Welcome to Why Edu!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            with open('data/videos/video_data.json', 'r') as video_file:
                video_data = json.load(video_file)
            login_user(video_data)
        elif choice == '3':
            print("Thank you for using Why Edu. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    
if __name__ == "__main__":
    main()
