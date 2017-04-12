# Blackjack!

class Card:
    # Variables:
    #    - suit (e.g. spades, hearts ...) (string)
    #    - rank (e.g. 2, Q, ...) (string)
    #    - color (black, red)   -- we can easily compute this
    #       from the suit, so no need to store it separately
    #    - blackjack value?   - maybe we want to keep this separate
    #    - face up / face down

    # Methods/functions:
    #   - flip()
    #   - reveal()
    #   - display()
    #   - get_color()
    #   - get_suit()
    #   - get_rank()
    #   - is_face_up()

    # Create a face-down card with the given rank and suit
    def __init__(self, rank, suit):
        self.rank = str(rank)    # just in case rank isn't a string
        self.suit = str(suit)      
        self.face_up = False

    # Return a string, e.g. '3H' OR '**'
    def display(self):
        if not self.face_up:
            return '**'
        else:
            return self.rank + self.suit

    # Flip the card over.
    def flip(self):
        self.face_up = not self.face_up

    # Make sure the card is face up.
    def reveal(self):
        self.face_up = True

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def get_color(self):
#        if self.get_suit() == 'S' or self.get_suit() == 'C':
        if self.get_suit() in ['S', 'C']:
            return 'black'
        else:
            return 'red'


class Deck:
    # Variables:
    #   - cards (list of card objects)
    #      - note dictionary (key = card object? string?, value = boolean)?
    #        doesn't work because it doesn't let us keep track of the order.

    # Methods:
    #   - shuffle()  --> put the cards into a random order
    #   - draw()  --> remove top card from the deck and return it
    #   - burn()  --> remove top card and don't return it
    #   - deal(n)   --> remove and return top n cards
    #   - add()    --> add a card (to the top?)
    #   - get_size()
    #   - display()

    # Make a new standard 52-card deck.
    def __init__(self):
        ranks = 'A23456789TJQK'
        suits  = 'SHDC'

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

        # TOO TEDIOUS
        # self.cards = [Card('A', 'S'), Card('2', 'S'), Card('3', 'S'), ......

    # Return a string representation of a deck like  AS 2S 3S ...
    def display(self):
        result = []
        for card in self.cards:
            result.append(card.display())
        return ' '.join(result)







    





