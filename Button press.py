from gpiozero import Button

button = Button(17)

def buttonPress():
    '''
    x = 0
    valid = False
    while not valid:
        try:
            amount = int(input("Amount of button presses: "))
            if 1 <= amount:
                valid = True
            else:
                print("\nNot valid. Please enter your value again\n")
        except ValueError:
            print("\nNot valid. Please enter your value again\n")
    '''
    while True: #x < amount:
        button.wait_for_press()
        print("\nButton Pressed :)\n")
        #x = x + 1

buttonPress()
