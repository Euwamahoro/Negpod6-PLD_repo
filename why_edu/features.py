import json

def get_quotes():
    with open('data/quotes.json', 'r') as file:
        return json.load(file)

def get_testimonials():
    with open('data/testimonials.json', 'r') as file:
        return json.load(file)

