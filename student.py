import random

class Student: 
    def __init__(self, name, motto):
        mottos = ["omae", "wa", "mou", "shinderiu"]
        self.name = name
        # self.origin = origin 
        # self.ability = ability
        self.motto = random.choice(mottos)
    
    def sayMotto(self):
        print(f"As {self.name} enters he says {self.motto}")

    def intro(self):
        print(f"Narrator: Welcome {self.name}")

    def __str__(self):
        return self.name



