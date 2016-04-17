# 11 April 2016
# Blackjack!

import random

class Card:

    # Variables:
    #   - suit (string: S, H, D, C)
    #   - rank (string)
    #   - face_up  (boolean)

    # Other ideas:
    #   - where the card is

    # Functions:
    #   - 3 "getter" methods:
    #     - get_suit()
    #     - get_rank()
    #     - is_face_up()
    #   - Other methods:
    #     - blackjack_value()
    #     - flip()
    #     - __repr__

    # Create a card which is face-down by default.
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = False

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def is_face_up(self):
        return self.face_up

    def flip(self):
        self.face_up = not self.face_up        

    # Returns a string representation of the object
    def __repr__(self):
        if self.face_up:
            return self.rank + self.suit
        else:
            return '**'

    def blackjack_value(self):
        if self.rank == 'A':
            return 1
        elif self.rank.isdigit():
            return int(self.rank)
        else:
            return 10

        # Alternatives:
        # "A23456789TJQK" -- look up index
        # dictionary rank -> value

    # Decide whether one card is less than another.
    def __lt__(self, other):
        # Standard bridge ordering:
        #   A-K S, A-K H, A-K D, A-K C.

        # clever hack: suits happen to be ordered
        #   reverse alphabetically!
        if (self.suit > other.suit):
            return True
        elif (self.suit < other.suit):
            return False
        else:
            # suits are the same
            ranks = "A23456789TJQK"
            return ranks.find(self.rank) < ranks.find(other.rank)

    # Really should also implement:
    # __gt__    (greater)
    # __eq__   (equal)
    # __ge__   (greater or equal)
    # __le__    (less or equal)
    # __ne__   (not equal)
    #
    # But sort() only uses lt.

# A deck is a sequence of cards.
class Deck:

    # Variables:
    #   - cards: list of Card objects.

    # Methods:
    #   - shuffle
    #   - sort
    #   - add_card
    #   - draw: return one card
    #   - deal: return a list of n cards
    #   - deal_hands: return a list of hands

    # Create a standard 52-card deck.
    # suits and ranks are *optional* parameters.
    def __init__(self, suits = "SHDC", ranks = "A23456789TJQK"):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append( Card(rank, suit) )

    def __repr__(self):
        output = ""
        for card in self.cards:
            output += str(card) + " "
        return output

    # Flip all the cards face-up
    def reveal(self):
        for card in self.cards:
            if not card.is_face_up():
                card.flip()

    # Shuffle the cards.
    def shuffle(self):
        random.shuffle(self.cards)

    # Sort the cards.
    def sort(self):
        self.cards.sort()
        # But how does Python know how to sort cards?
        # We need to tell it --- by adding another method
        #   to Card

    # Remove the top (leftmost) card from the deck
    # and return it
    def draw(self):
        return self.cards.pop(0)
        # TODO: fix so this doesn't crash for an empty Deck

    # Draw the top n cards from the Deck and return them
    # in a list
    def deal(self, n):
        cards = []
        for i in range(n):
            cards.append(self.draw())
        return cards

    # Add c to the end of the deck
    def add_card(self, c):
        self.cards.append(c)

    # Add a list of cards to the end of the deck
    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)

# A Hand "is-a" special kind of deck
# Hand "inherits from" Deck
# Hand objects automatically have everything
#   that a Deck object has, plus some extra stuff
#   that is specific to Hands.
class Hand(Deck):

    # An extra method specific to Hand:

    def value(self):
        total = 0
        for c in self.cards:
            total += c.blackjack_value()
        return total

    # A method that we want to work differently
    # for Hands.  By redefining it we "override"
    # the definition that we would have inherited
    # from Deck.

    def __init__(self):
        self.cards = []

#########################

# A general blackjack player
class Player:

    # Variables:
    #   - hand

    # Create a player with an initial hand
    def __init__(self, hand):
        self.hand = hand

    # Add a card to a player's hand
    def add_card(self, card):
        self.hand.add_card(card)

    # Decide whether to hit:
    #   True --> another card
    #   False  --> stop
    def hit(self):
        return True

    # Idea: more specific Players should override
    # the hit() method with their own way of playing.
    # Every kind of Player will always have a hit() method.

# A ComputerPlayer is a kind of Player
class ComputerPlayer(Player):

    # Override (redefine) hit
    def hit(self):
        return (self.hand.value() < 17)

# A HumanPlayer is also a kind of Player
class HumanPlayer(Player):

    def hit(self):
        self.hand.reveal()
        print "Your hand: ",
        print self.hand
        h = raw_input("Do you want to hit? ")
        return (h.lower() == 'y')

##########################

# Play a game of human vs computer blackjack.
def play_blackjack():
    d = Deck()
    d.shuffle()

    compHand = Hand()
    compHand.add_cards(d.deal(2))

    humanHand = Hand()
    humanHand.add_cards(d.deal(2))

    comp = ComputerPlayer(compHand)
    human = HumanPlayer(humanHand)

    one_player(human, d)

# Ask a player repeatedly until they are done hitting
def one_player(player, deck):
    while player.hit():
        player.add_card(deck.draw())
