# http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        res = requests.get(f'{BASE_URL}{url}')
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            all_quotes.append({
                'text': quote.find(class_='text').get_text(),
                'author': quote.find(class_='author').get_text(),
                'bio-link': quote.find('a')['href']
            })

        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
        sleep(1)
    return all_quotes

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

quotes = scrape_quotes()
start_game(quotes)