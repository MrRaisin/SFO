class Human():
    def __init__(self, gender= "unknown", age = 0, name = "unknown"):
        self._gender = gender
        self._age = age
        self._name = name

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setGender(self, gender):
        if gender.lower() == 'male':
            self._gender = gender
        elif gender.lower() == 'female':
            self._gender = gender
        else:
            self._gender = "other"

    def getGender(self):
        return self._gender

    def speak(self):
        print(self._name,"says 'Hello'")

# fred
fred = Human('Male')
fred.setName('Fred')
fred.speak()
print(fred.getName())
# & wilma
wilma = Human('female')
wilma.setName('Wilma')
print(wilma.getName())

# add another attribute called _name /
# create some code to add a name to an instance of the class /

# add another method to the Human class called
# speak() - which returns _name + ": says 'Hello'"
# note the single quotes
