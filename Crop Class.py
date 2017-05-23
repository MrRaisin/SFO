import random
class Crop():
    '''This is the blueprint for the crops'''

    #constructor
    def __init__(self, growth_rate, light_need, water_need):

        #defining the default attributes
        self._growth = 0
        self._days_grow = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        
    def setType(self, Type):
        self._type = Type
        
    def Needs(self):
        #Returns crop needs that were stored in a dictionary
        return{"Light Need": self._light_need, "Water Need": self._water_need}

    def Report(self):
        #Returns the crops info that were kept in a dictionary
        return{"Type": self._type, "Status": self._status, "Growth": self._growth, "Days Growing": self._days_grow}

    def _Update(self):
        #Updates the status of the crop
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        else:
            self._status = "Seed"

    def Grow(self, light, water):
        #Grows the crop then calls upon _Update in order to change the crop's status
        if light >= self._light_need and water >= self._water_need:
            self._growth = self._growth + self._growth_rate

        self._days_grow = self._days_grow + 1

        self._Update()

def Auto(crop, days):
    #This automatically grows the crop
    for day in range(days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.Grow(light,water)

def Manual(crop):
    #This Manually grows the crop using user input
    valid = False
    while not valid:
        try:
            light = int(input("Enter light value(1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("\nValue not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue not valid. Please enter your value again.\n")
    valid = False
    while not valid:
        try:
            water = int(input("Enter water value(1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("\nValue not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue not valid. Please enter your value again.\n")
    crop.Grow(light, water)

def menuDisplay():
    print("\nThis is the crop managing program.")
    print("\nOptions:")
    print("1. Grow Crops Manually for 1 day")
    print("2. Grow Crops Automatically for 30 days")
    print("3. Report growth status")
    print("4. Exit the program\n")

def menuChoice():
    option = False
    while not option:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option = True
            else:
                print("Option not valid. Please enter your option again.")
        except ValueError:
            print("Option not valid. Please enter your option again.")
    return choice

def Manage(crop):
    y = input("Enter your crop type: ")
    crop.setType(y)
    noexit = True
    while noexit:
        menuDisplay()
        option = menuChoice()
        print()
        if option == 1:
            Manual(crop)
            print()
        elif option == 2:
            Auto(crop, 30)
            print()
        elif option == 3:
            print(crop.Report())
            print()
        else:
            noexit = False
            print("Thank you for using the crop managing system.")

crop1 = Crop(1,6,5)
Manage(crop1)

