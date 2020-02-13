import random

class Card():
    def __init__(self, value, face, suit):
        self.value = value
        self.face = face
        self.suit = suit #diamonds (♦), clubs (♣), hearts (♥) and spades (♠)
        #self.visible = visible

    def __repr__(self):
        return "<Value: %s, Face: %s, Suit: %s>" % (self.value, self.face, self.suit)

    def __str__(self):
        return "The value of the card is: %s\nThe face is: %s\nThe suit is: %s" % (self.value, self.face, self.suit)

class Deck():
    def __init__(self):
        self.deck = [] #each deck is 52

    def createDiamonds(self):
        suit = "Diamonds"
        self.deck.append(Card(1, "Ace", suit))
        for i in range(2, 10):
            self.deck.append(Card(i, str(i), suit))
        self.deck.append(Card(11, "Jack", suit))
        self.deck.append(Card(12, "Queen", suit))
        self.deck.append(Card(13, "King", suit))
        #print("Done creating", suit)

    def createClubs(self):
        suit = "Clubs"
        self.deck.append(Card(1, "Ace", suit))
        for i in range(2, 10):
            self.deck.append(Card(i, str(i), suit))
        self.deck.append(Card(11, "Jack", suit))
        self.deck.append(Card(12, "Queen", suit))
        self.deck.append(Card(13, "King", suit))
        #print("Done creating", suit)

    def createHearts(self):
        suit = "Hearts"
        self.deck.append(Card(1, "Ace", suit))
        for i in range(2, 10):
            self.deck.append(Card(i, str(i), suit))
        self.deck.append(Card(11, "Jack", suit))
        self.deck.append(Card(12, "Queen", suit))
        self.deck.append(Card(13, "King", suit))
        #print("Done creating", suit)

    def createSpades(self):
        suit = "Spades"
        self.deck.append(Card(1, "Ace", suit))
        for i in range(2, 10):
            self.deck.append(Card(i, str(i), suit))
        self.deck.append(Card(11, "Jack", suit))
        self.deck.append(Card(12, "Queen", suit))
        self.deck.append(Card(13, "King", suit))
        #print("Done creating", suit)

    def create(self, size):
        for i in range(size):
            self.createDiamonds()
            self.createClubs()
            self.createHearts()
            self.createSpades()

    def shuffle(self):
        random.shuffle(self.deck)

    def destroyDeck(self):
        self.deck = []

    def showDeck(self):
        print(self.deck)

    def takeCard(self):
        return self.deck.pop()

    def blackjack(self):
        for i in range(len(self.deck)):
            if self.deck[i].value > 10:
                self.deck[i].value = 10
