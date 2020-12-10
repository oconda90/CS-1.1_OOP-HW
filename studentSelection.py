
from battleground import Battleground
from student import Student
from welcome import Main
class studentSelection(Battleground, Student):
    def __init__(self, quirk, studentName):
        self.studentName = studentName
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
            player2 = Student(player2_name, "hi")
            self.battleground = Battleground(player1, player2)
            self.battleground.fight()
    def chooseQuirk(self):
        Quirks = ["One for all", "Explosion", "half-cold half-hot", "Engine", "Zero Gravity", "Acid", "Electricity", "Tape Shot"]
        Choose_Quirk = input("Choose your quirk! Dont be afriad to mix it Up! ")
        for quirk in Quirks:
            if Choose_Quirk == quirk: 
                self.quirk = Choose_Quirk
                print(f'{self.quirk} is now possessed by {self.studentName}')

test1= Main('Omar', 'N/A')
test1.greetings()
test1.userAvailability()
test2= Student('Mydoriya', 'N/A')
test2.saySupermove()
test2.intro()
test3 = Battleground('Mydoriya', 'Todoroki')
test3.fight()
test3.tapOut()
