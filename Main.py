

class Hello:
    """ Meeting the user """

    def __init__(self, name, status):
        self.name = name
        self.status = status
        
    def greetings(self):
        """greeting user"""
    print(f'Hello {self.name}, Welcome to our My Hero Academia fight simulator.')

    def UserStatus(self):
        
        life_status = input("What is your current Status?")

        if life_status == "Busy":
            self.status = "Busy"
            print('We can play later')
        elif life_status == "I'm Free":
            self.status = "I'm Free"
            print('Let us fight to the death, with anime charcters of course!')
            


        
       

      
"""
OmarConda = Hello("omar conda", "none", 0)
print (OmarConda.status)
OmarConda.KnownUser()
print (OmarConda.status)
"""
