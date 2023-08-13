import user
import features
import random
import json
import webbrowser



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
        print("1. Get Random Quote")
        print("2. Get Testimonials")
        print("3. Watch Videos")
        print("4. Chat with Users")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            quotes = features.get_quotes()
            random_quote = random.choice(quotes)
            print("Random Quote:")
            print(random_quote)

        elif choice == '2':
            testimonials = features.get_testimonials()
            print("Testimonials:")
            for testimonial in testimonials:
                print(testimonial)

        elif choice == '3':
            watch_videos(video_data)
        elif choice == '4':
            chat_with_users()

        elif choice == '5':
            print("Logout successful!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

def chat_with_users(username):
    global chat_messages
    while True:
        print("\nChat with Users:")
        for message in chat_messages:
            print(message)
        new_message = input("Enter your message (or 'exit' to return to features): ")
        if new_message.lower() == 'exit':
            break
        chat_messages.append(f"{username}: {new_message}")
def main():
    
    global chat_messages
    chat_messages = []  # Initialize chat messages
    
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
            login_user(video_data)  # Pass video_data argument here
        elif choice == '3':
            print("Thank you for using Why Edu. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
