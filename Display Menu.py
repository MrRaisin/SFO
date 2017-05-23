from Wheat_Class import *
from Potato_Class import *
from Carrot_Class import *

def Display_Menu():
    print("\nWhich seeds would you like to grow?")
    print("\n1. Potato Seeds\n2. Wheat Seeds\n3. Carrot Seeds\n")

def Option_Select():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,3):
                valid_option = True
            else:
                print("That option isn't valid. Please enter a valid option.")
        except ValueError:
            print("That option isn't valid. Please enter a valid option.")

    return choice

def Crop_Create():
    Display_Menu()
    choice = Option_Select()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    elif choice == 3:
        new_crop = Carrot()

    return new_crop

def main():
    myCrop = Crop_Create()
    Manage(myCrop)

if __name__ == "__main__":
    main()
