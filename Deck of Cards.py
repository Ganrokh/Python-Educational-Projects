from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        self.cards = [Card(value, suit) for value in values for suit in suits]
        print(self.cards)
    
    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError('All cards have been dealt')
        dealt = min(count, num)
        dealtCards = self.cards[-dealt:]
        self.cards = self.cards[:-dealt]
        return dealtCards

    def count(self):
        return len(self.cards)

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, num):
        return self._deal(num)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)