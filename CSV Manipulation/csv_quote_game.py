# http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = 'http://quotes.toscrape.com'

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    guesses_left = 4
    print("Here's a quote: ")
    print(quote['text'])
    guess = ''
    while guess.lower() != quote['author'].lower() and guesses_left > 0:
        guess = input(f'Who said this quote? Guesses remaining: {guesses_left}\n')
        if guess.lower() == quote['author'].lower():
            print('Correct!')
            break
        guesses_left -= 1
        if guesses_left == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_place = soup.find(class_='author-born-location').get_text()
            print(f"Here's a hint: The author was born on {birth_date} in {birth_place}")
        elif guesses_left == 2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
        elif guesses_left == 1:
            last_initial = quote['author'].split(' ')[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry, you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        print("Okay! Starting...")
        return start_game(quotes)
    else:
        print("Okay, goodbye!")

quotes = read_quotes("quotes.csv")
start_game(quotes)