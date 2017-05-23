from Crop_Class import *

class Carrot(Crop):
    '''This is a child class of crop'''
    #constructor
    def __init__(self):
        super().__init__(1, 6, 7)
        self._type = "Carrot"

    def Grow(self, light, water):
        #Overwrites the grow function
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seed" and water > self._water_need:
                self._growth = self._growth + self._growth_rate * 2
                
            elif self._status == "Seedling" and water > self._water_need:
                self._growth = self._growth + self._growth_rate * 1.75
                
            elif self._status == "Young" and water > self._water_need:
                self._growth = self._growth + self._growth_rate * 1.5
                
            else:
                self._growth = self._growth + self._growth_rate

        else:
            pass

        self._days_grow = self._days_grow + 1
        
        self._Update()
