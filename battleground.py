import random


from student import Student 


class Battleground: 
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
    
    def fight(self):
        winners = [self.character1, self.character2]
        winner = random.choice(winners)
        print(f"And the winner is {winner}")