
from battleground import Battleground
from student import Student
class studentSelection:
    def __init__(self, name, quirk):
        self.name = name
        self.quirk = quirk
    def chooseStudent(self):
        players = ["Mydoriya", "Bakugo", "Todoroki", "Iida", "Uraraka", "Ashido", "Kamanari", "Sero"]
        player1_name = input("Choose your fighter from Class 1-A!")
        for player in players:
            if player1_name == player:
                player2_name = input("Choose Another Character")
                break
            else:
                print("This Student is with recovery girl, Try Again!")
                break
            player1 = Student(player1_name, "hi")
            player2 = Student(player2_name, "ji")
            self.battleground = Battleground(player1, player2)
            self.battleground.fight()
     


