import random
import time
import card
import scoring


class Blackjack():
    def __init__(self, size):
        self.deck = card.Deck()
        self.deck.create(size)
        self.deck.shuffle()
        self.deck.blackjack()

        self.playerDeck = []
        self.playerDeckBust = False
        self.playerSplitBust = False
        self.playerSplit = []
        self.playerSplitBool = False
        self.playerDouble = False
        self.dealerDeck = []

        self.playerTotal = 0
        self.playerSplitTotal = 0
        self.dealerTotal = 0

    def deal(self, pause):
        #Pause is how long between each card is dealt
        for i in range(2):
            self.playerDeck.append(self.deck.takeCard())
            self.dealerDeck.append(self.deck.takeCard())
            if self.dealerDeck[i].face.lower() == "ace":
                randomNum = random.randint(0, 1)
                dealerValue = self.countDealer()
                if randomNum == 1 and dealerValue < 12:
                    self.dealerDeck[i].value = 11


        print("\nDealer's card:", self.dealerDeck[0].face)
        time.sleep(pause)
        print("\nYour cards:\n" + self.playerDeck[0].face)
        if self.playerDeck[0].face.lower() == "ace":
            choice = int(input("You got an ace, do you want it as 1 or 11 (1/11): "))
            if choice == 11:
                self.playerDeck[0].value = 11

        time.sleep(pause)

        print(self.playerDeck[1].face)
        if self.playerDeck[1].face.lower() == "ace":
            choice = int(input("You got an ace, do you want it as 1 or 11 (1/11): "))
            if choice == 11:
                self.playerDeck[1].value = 11
        print("\nThe total value is:", self.countPlayer())

    def reset(self):
        self.playerDeck = []
        self.playerDeckBust = False
        self.playerSplitBust = False
        self.playerSplit = []
        self.playerSplitBool = False
        self.playerDouble = False
        self.dealerDeck = []

        self.playerTotal = 0
        self.playerSplitTotal = 0
        self.dealerTotal = 0

    def hit(self):
        if not self.playerDeckBust:
            self.playerDeck.append(self.deck.takeCard())
            if self.playerDeck[-1].face.lower() == "ace":
                choice = int(input("You got an ace, do you want it as 1 or 11 (1/11): "))
                if choice == 11:
                    self.playerDeck[-1].value = 11

        self.countPlayer()
        print("\nYou got a:", self.playerDeck[-1].face)

    def hitSplit(self):
        self.playerSplit.append(self.deck.takeCard())
        if self.playerSplit[-1].face.lower() == "ace":
            choice = int(input("You got an ace, do you want it as 1 or 11 (1/11): "))
            if choice == 11:
                self.playerSplit[-1].value = 11

    def printResults(self):
        if self.playerSplitBool:
            print("In your first hand you have:")
            for i in range(len(self.playerDeck)):
                print(self.playerDeck[i].face)
            print("In your second hand you have:")
            for i in range(len(self.playerSplit)):
                print(self.playerSplit[i].face)
        else:
            print("Your cards are:")
            for i in range(len(self.playerDeck)):
                print(self.playerDeck[i].face)

    def countPlayer(self):
        self.playerTotal = 0
        for i in range(len(self.playerDeck)):
            self.playerTotal += self.playerDeck[i].value
        return self.playerTotal

    def countPlayerSplit(self):
        self.playerSplitTotal = 0
        for i in range(len(self.playerSplit)):
            self.playerSplitTotal += self.playerSplit[i].value
        return self.playerSplitTotal

    def countDealer(self):
        self.dealerTotal = 0
        for i in range(len(self.dealerDeck)):
            self.dealerTotal += self.dealerDeck[i].value
        return self.dealerTotal

    def dealerHit(self):
        self.dealerDeck.append(self.deck.takeCard())
        if self.dealerDeck[-1].face.lower() == "ace":
            randomNum = random.randint(0, 1)
            dealerValue = self.countDealer()
            if randomNum == 1 and dealerValue < 12:
                self.dealerDeck[-1].value = 11
        self.countDealer()
        print("\nThe dealer got a:", self.dealerDeck[-1].face)

    def stand(self):
        print("Ok")

    def doubleDown(self):
        self.playerDeck.append(self.deck.takeCard())
        self.playerDouble = True
        self.stand()

    def split(self):
        if self.playerDeck[0].value == self.playerDeck[1].value and len(self.playerDeck) == 2:
            self.playerSplit.append(self.playerDeck.pop())
            self.playerSplitBool = True
            self.hit()
        else:
            print("You can't do that.")


blackjack = Blackjack(8)
play = True
loggedIn = False

while True:
    while not loggedIn:
        username = input("Please enter your username: ")
        player = scoring.Scoring(username)
        existingPlayer = player.findPlayer()
        if existingPlayer:
            player.login()
            break
        else:
            choice = input("Would you like to create the account %s? (Y/N): " % username).lower()
            if choice == "y":
                player.createPlayer()
            else:
                choice = input("Would you like to quit? (Y/N): ")
                if choice == "y":
                    break

    player.stats()

    while True:
        won = False
        wonSplit = False
        tie = False
        tieSplit = False
        decision = input("Do you want to play (Y/N): ")
        if decision.lower() == "n":
            break

        bet = round(float(input("Please make your bet: ")), 2)
        print(bet)

        blackjack.deal(1)

        while blackjack.playerTotal < 21:
            time.sleep(1)
            move = input("What do you want to do? (Hit/Stand/Double Down/Split): ").lower()
            if move == "hit":
                blackjack.hit()
            elif move == "stand":
                break
            elif move == "double down":
                blackjack.doubleDown()
            elif move == "split":
                betSplit = round(float(input("Please make your bet on the split: ")), 2)
                blackjack.split()
            time.sleep(1)
            print("Your total value is:", blackjack.countPlayer())
            if blackjack.playerSplitBool:
                #FINISH THE CODE HERE

        if blackjack.playerTotal == 21:
            time.sleep(2)
            print("\nYou got blackjack!")
            won = True

        if blackjack.playerTotal > 21:
            time.sleep(2)
            print("\nYou went bust.")

        while blackjack.dealerTotal < 17:
            time.sleep(1)
            blackjack.dealerHit()
            time.sleep(1)
            print("The dealer has:", blackjack.countDealer())

        time.sleep(2)

        if blackjack.dealerTotal < blackjack.playerTotal < 21 or (blackjack.dealerTotal > 21 and blackjack.playerTotal < 21):
            print("\nYou won the round!")
            won = True
        elif blackjack.dealerTotal > 21:
            print("\nThe dealer went bust.")
        elif blackjack.playerTotal < blackjack.dealerTotal <= 21 and blackjack.playerTotal < 21:
            print("\nYou lost to the dealer.")
        elif blackjack.playerTotal == blackjack.dealerTotal and blackjack.playerTotal < 21:
            print("\nYou tied.")
            tie = True

        if won:
            moneyWon = bet*1.5
            player.saveUser(1, moneyWon, 0)
            print("You won £%.2f!" % moneyWon)
        elif tie:
            print("You got your money back.")
        else:
            moneyWon = -bet
            player.saveUser(0, moneyWon, 0)
            print("You lost £%.2f" % bet)

        if blackjack.playerSplitBool:
            if blackjack.playerSplitTotal == 21:
                time.sleep(2)
                print("\nYou got blackjack!")
                wonSplit = True

            if blackjack.playerSplitTotal > 21:
                time.sleep(2)
                print("\nYou went bust.")

            while blackjack.dealerTotal < 17:
                time.sleep(1)
                blackjack.dealerHit()
                time.sleep(1)
                print("The dealer has:", blackjack.countDealer())

            time.sleep(2)

            if blackjack.dealerTotal < blackjack.playerSplitTotal < 21 or (
                    blackjack.dealerTotal > 21 and blackjack.playerSplitTotal < 21):
                print("\nYou won the round!")
                wonSplit = True
            elif blackjack.dealerTotal > 21:
                print("\nThe dealer went bust.")
            elif blackjack.playerSplitTotal < blackjack.dealerTotal <= 21 and blackjack.playerSplitTotal < 21:
                print("\nYou lost to the dealer.")
            elif blackjack.playerSplitTotal == blackjack.dealerTotal and blackjack.playerSplitTotal < 21:
                print("\nYou tied.")
                tieSplit = True

            if wonSplit:
                moneyWon = betSplit * 1.5
                player.saveUser(1, moneyWon, 0)
                print("You won £%.2f from your split!" % moneyWon)
            elif tieSplit:
                print("You got your money back from your split.")
            else:
                moneyWon = -betSplit
                player.saveUser(0, moneyWon, 0)
                print("You lost £%.2f from your split." % betSplit)

        player.saveUser(0, 0, 1)
        blackjack.reset()
        time.sleep(1)
        print("")
        player.stats()
        print("")
        time.sleep(2)

    decision = input("Do you want to quit? (Y/N): ").lower()
    if decision == "y":
        break






'''
Hit
Stand
Double Down
Split
Surrender

Hit: Take another card from the dealer.
Signal: Scrape cards against table (in handheld games); tap the table with finger or wave hand toward body (in games dealt face up).
Stand: Take no more cards, also known as "stand pat", "stick", or "stay".
Signal: Slide cards under chips (in handheld games); wave hand horizontally (in games dealt face up).
Double down: The player is allowed to increase the initial bet by up to 100% in exchange for committing to stand after receiving exactly one more card. The additional bet is placed in the betting box next to the original bet. Some games do not permit the player to increase the bet by amounts other than 100%. Non-controlling players may double their wager or decline to do so, but they are bound by the controlling player's decision to take only one card.
Signal: Place additional chips beside the original bet outside the betting box, and point with one finger.
Split: If the first two cards of a hand have the same value, the player can split them into two hands, by moving a second bet equal to the first into an area outside the betting box. The dealer separates the two cards and draws an additional card on each, placing one bet with each hand. The player then plays out the two separate hands in turn; except for a few restrictions, the hands are treated as independent new hands, with the player winning or losing their wager separately for each hand. Occasionally, in the case of ten-valued cards, some casinos allow splitting only when the cards have the identical ranks; for instance, a hand of 10-10 may be split, but not one of 10-king. However, usually all 10-value cards are treated the same. Doubling and further splitting of post-split hands may be restricted, and an ace and ten value card after a split are counted as a non-blackjack 21. Hitting split aces is usually not allowed. Non-controlling players may follow the controlling player by putting down an additional bet or decline to do so, instead associating their existing wager with one of the two post-split hands. In that case they must choose which hand to play behind before the second cards are drawn. Some casinos do not give non-controlling players this option, and require that the wager of a player not electing to split remains with the first of the two post-split hands.
Signal: Place additional chips next to the original bet outside the betting box; point with two fingers spread into a V formation.
Surrender (only available as first decision of a hand): Some games offer the option to "surrender" directly after the dealer has checked for blackjack (see below for variations). When the player surrenders, the house takes half the player's bet and returns the other half to the player; this terminates the player's interest in the hand.
Signal: The request to surrender is made verbally, there being no standard hand signal.
'''