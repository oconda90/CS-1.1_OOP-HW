from Main import main
from battleground import battleground
from student import student
class students:
    def __init__(self, name, quirk):
        self.name = name
        self.quirk = quirk
    def chooseStudent(self):
        players = ["Mydoriya", "Bakugo", "Todoroki", "Iida", "Uraraka", "Ashido", "Kamanari", "Sero"]
        player1_name = input("Choose your fighter from Class 1-A /n")
        for player in players:
            if player1_name == player:
                player2_name = input("Choose Another Character")
                break
            else:
                print("Not Yet Implemented, Try Again!")
                break
        player1 = student(player1_name, "hi")
        player2 = student(player2_name, "ji")
        self.battleground = battleground(player1, player2)
        self.battleground.fight()