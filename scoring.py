import json
import getpass


class Scoring():
    def __init__(self, playerID):
        self.playerID = playerID
        self.password = ""
        self.totalScore = 0
        self.money = 0
        self.totalRounds = 0

        self.user = [self.playerID, self.password, self.totalScore, self.money, self.totalRounds]

        with open("score.txt", "r") as file:
            self.scores = json.load(file)

        self.doesntExist = True
        for i in range(len(self.scores)):
            if self.scores[i][0] == self.playerID:
                self.doesntExist = False
                self.user = self.scores[i]

    def save(self):
        with open("score.txt", "w") as file:
            json.dump(self.scores, file)

    def findPlayer(self):
        found = False
        for i in range(len(self.scores)):
            if self.scores[i][0] == self.playerID:
                self.scores[i] = self.user
                found = True
        return found

    def createPlayer(self):
        if self.doesntExist:
            password2 = ""
            print("Please enter the password you wish to have for this account.")
            while self.password != password2 and self.password > 0:
                self.password = getpass.getpass()
                self.password2 = getpass.getpass()
                if self.password != password2:
                    print("You didn't enter the passwords correctly.")
            self.scores.append(self.user)
            self.save()
            print("User successfully created.")
        else:
            print("The user already exists.")

    def login(self):
        password2 = ""
        while self.password != password2:
            password2 = getpass.getpass()
            if self.password != password2:
                print("You entered your password incorrectly.")
        print("Logged in successfully")
        return True

    def saveUser(self, totalScore, money, totalRounds):
        self.user[1] += totalScore
        self.user[2] += money
        self.user[3] += totalRounds
        if self.findPlayer():
            self.save()
        else:
            print("Error whilst saving - didn't save.")

    def destroyData(self, boolean):
        confirmation = input("Are you sure you want to destroy the data?: 'Yes' to confirm: ")
        if boolean and confirmation == "Yes":
            with open("score.txt", "w") as file:
                json.dump([], file)
