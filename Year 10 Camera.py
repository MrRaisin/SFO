import time
import picamera
import os
import datetime

def nameProject(cam):
    name = str(input("\n\nEnter project name: "))
    date = datetime.datetime.now()
    now = date.strftime("%Y-%m-%d")
    mypath = "/home/pi/camera/"+now+"-"+name
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    else:
        pass

    print("\nProject folder made successfully.\n")

    return mypath
    
#put def takePicture here
#put def preview here

def display(num):
    if num == 0:
        print("\nWelcome to the image capture program for year 10s.")
    elif num == 1:
        print("\nBefore beginning please create your project file.")
    elif num == 2:
        print("\nOptions\n\n1. Preview camera view\n2. Start taking pictures\n3. Quit")

def choice():
    valid = False
    while not valid:
        try:
            option = int(input("\nEnter option: "))
            if 1 <= option <= 3:
                valid == True
            else:
                print("\n\nOption not valid. Please enter option again.\n")
        except ValueError:
            print("\n\nOption not valid. Please enter option again.\n")
            
    return option
            


    
def main():
    cam = picamera()
    display(0)
    display(1)
    path = nameProject(cam)
    valid = False
    while not valid:
        display(2)
        x = choice()
        if x == 1:
            #preview(cam)
            print('1')
        elif x == 2:
            #takePicture(cam)
            print('2')
        elif x == 3:
            valid = True
    print("\n\nProgram ended.")
