class Human():
    def __init__(self, age = 0, name = "unknown", gender='unknown'):
        self._gender = gender
        self._age = age
        self._name = name

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def getGender(self):
        return self._gender

    def speak(self):
        print(self._name,"says 'Hello'")

    def setGender(self, gender):
        if gender.lower() == 'male':
            self._gender = gender
        elif gender.lower() == 'female':
            self._gender = gender
        else:
            self._gender = "other"

class Man(Human):
    def __init__(self,nickname='don\'t know'):
        super().__init__(gender='Male')
        self._nickname = nickname

    def getNickname(self):
        return self._nickname


class Man2(Man):
    def __init__(self,hobby='don\'t know'):
        super().__init__(nickname='Man2')
        self._hobby = hobby

    def getHobby(self):
        return self._hobby

    
    

# fred
fred = Man2()#nickname='Muppet')
print('My nicknam is',fred.getNickname())
print('Myhobby is',fred.getHobby())
fred.speak()
print('My name is',fred.getName())
print('My gender is',fred.getGender())
'''
# & wilma
wilma = Human('female')
wilma.setName('Wilma')
print(wilma.getName())
'''
# add another attribute called _name /
# create some code to add a name to an instance of the class /

# add another method to the Human class called
# speak() - which returns _name + ": says 'Hello'"
# note the single quotes


