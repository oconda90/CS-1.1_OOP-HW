

class Main:
    """ Meeting the user """

    def __init__(self, name, available):
        self.name = name
        self.available = available
        
    def greetings(self):
        """greeting user"""

        print(f'Hello {self.name}, Welcome to our My Hero Academia fight simulator.')

    def userAvailability(self):
        while True:

            life_availability = input("What is your current availability?")
        
            if life_availability == "Busy":
                self.available = "Busy"
                print('No worries, we can fight later!')
                break
            
            elif life_availability == "I'm Free":
                self.available = "I'm Free"
                print('Let us fight to the death, with anime charcters of course!')
                break
            
            else:
                print('Please let us know your availability!')
               
       

"""
OmarConda = Main("Omar","free")
OmarConda.greetings()
print(OmarConda.available)
OmarConda.userAvailability()
print(OmarConda.available)
"""



