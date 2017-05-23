class Animal():
    def __init__(self, species = "Undiscovered", age = 0, threat_lvl = "Peaceful", hunger_lvl = 0):
        self._species = species
        self._age = age
        self._threat_lvl = threat_lvl
        self._hunger_lvl = hunger_lvl

    def setSpecies(self, species):
        self._species = species

    def getSpecies(self):
        return self._species

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

    def setHunger(self, hunger):
        self._hunger_lvl = hunger

    def getHunger(self):
        return self._hunger_lvl

    def setThreat(self):
        if self._hunger_lvl <= 3:
            self._threat_lvl = "Peaceful"
        elif self._hunger_lvl >= 4 and self._hunger_lvl < 8:
            self._threat_lvl = "Narky"
        else:
            self._threat_lvl = "Aggressive"

        return self._threat_lvl

cat = Animal()
cat.setSpecies("Cat")
cat.setAge(5)
cat.setHunger(7)
print("Species:",cat.getSpecies(),"\nAge",cat.getAge(),"\nHunger Level:",cat.getHunger(),"\nThreat Level:",cat.setThreat())

