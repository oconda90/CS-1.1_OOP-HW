import random

class Student: 
    def __init__(self, name, superMove):
        Supermove = ["SMAAASH!", "Howitzer Impact!", "Recipro Burst!", "Indiscriminate Shock 1.3 Million Volts!"]
        self.name = name
        
        self.superMove = random.choice(Supermove)
    
    def saySupermove(self):
        print(f"I {self.name} will soon finish you off with My {self.superMove}")

    def intro(self):
        print(f"Narrator: Welcome {self.name}")

    def __str__(self):
        return self.name



