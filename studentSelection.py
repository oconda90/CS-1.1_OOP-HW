
from battleground import Battleground
from student import Student
from welcome import Main
class studentSelection():
    def __init__(self, quirk, studentName):
        self.quirk = quirk
        self.studentName = studentName
    def chooseStudent(self):
        players = ["Mydoriya", "Bakugo", "Todoroki", "Iida", "Uraraka", "Ashido", "Kamanari", "Sero"]
        player1_name = input("Choose your fighter from Class 1-A!")
        for player in players:
            if player1_name == player:
                player2_name = input("Choose your opponent!")
                break
            else:
                print("This Student is with recovery girl, Try Again!")
                break
            
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
test4=studentSelection('One for all', 'Mydoriya')
print(test4.quirk)
test4.chooseStudent()
test2.intro()
test4.chooseQuirk()
print(test4.quirk)
test2.saySupermove()
test3 = Battleground('Mydoriya', 'Todoroki')
test3.fight()
test3.tapOut()
