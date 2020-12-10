import random

class Student: 
    def __init__(self, studentName, superMove):
        Supermove = ["SMAAASH!", "Howitzer Impact!", "Recipro Burst!", "Indiscriminate Shock 1.3 Million Volts!"]
        self.studentName = studentName
        self.superMove = random.choice(Supermove)
    
    def saySupermove(self):
        print(f"I {self.studentName} will soon finish you off with My {self.superMove}")

    def intro(self):
        print(f"Narrator: Welcome {self.studentName}")

    def __str__(self):
        return self.studentName



