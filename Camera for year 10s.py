#imports
import time
import picamera
import os
import datetime

def nameProject(cam):
    #Nmaes the folders
    name = str(input("\nEnter project name: "))
    date = datetime.datetime.now()
    now = date.strftime("%Y-%m-%d")
    mypath = "/home/pi/camera/"+now+"-"+name
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    else:
        pass

    print("\nProject folder made successfully.\n")

    return mypath
    
def takePicture1(cam , filePath):
    #Subproceedure that takes the pictures UNTIL a key is pressed
    print("\nWARNING: Pictures may blur when there is lots of movement")
    filePath = filePath + "/"
    valid = False
    while not valid:
        try:
            inter = int(input("\nInterval between pictures in seconds(1 or above): "))
            if 1 <= inter:
                print("\nTo stop taking pictures press 'c' and 'Ctrl' together")
                valid = True
            else:
                print("\nValue not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue not valid. Please enter your value again.\n")

    x = False

    while not x:
        try:
            currentTime = datetime.datetime.now()
            picTime = ("{:%H:%M:%S}".format(currentTime))
            picName = picTime + '.jpg'
            completeFilePath = filePath + picName
            cam.capture(completeFilePath)
            time.sleep(inter)
                
        except KeyboardInterrupt:
            x = True

def takePicture2(cam , filePath):
    #Subproceedure that takes the pictures WHEN a key is pressed
    filePath = filePath + "/"
    print("\nPress 'enter' to take an image")
    print("To stop taking pictures press 'c' and 'Ctrl' together")

    x = False
    y = False

    while not x:
        try:
            while not y:
                input("")
                currentTime = datetime.datetime.now()
                picTime = ("{:%H:%M:%S}".format(currentTime))
                picName = picTime + '.jpg'
                completeFilePath = filePath + picName
                cam.capture(completeFilePath)
                
        except KeyboardInterrupt:
            x = True

def preview(cam):
    #Camera preview
    cam.start_preview()
    time.sleep(10)
    cam.stop_preview()
        

def display(num):
    #Different displays
    if num == 0:
        print("\nWelcome to the image capture program for year 10s.")
    elif num == 1:
        print("\nBefore beginning please create your project file.")
    elif num == 2:
        print("Options\n\n1. Preview camera view\n2. Take pictures automatically\n3. Take pictures manually\n4. Quit")

def choice():
    #Sorts the choice
    valid = False
    while not valid:
        try:
            option = int(input("\nEnter option: "))
            if 1 <= option <= 4:
                valid = True
            else:
                print("\n\nOption not valid. Please enter option again.\n")
        except ValueError:
            print("\n\nOption not valid. Please enter option again.\n")
            
    return option
    
def main():
    #Main program
    cam = picamera.PiCamera()
    display(0)
    display(1)
    path = nameProject(cam)
    valid = False
    while not valid:
        display(2)
        opt = choice()
        if opt == 1:
            preview(cam)
        elif opt == 2:
            takePicture1(cam, path)
        elif opt == 3:
            takePicture2(cam, path)
        elif opt == 4:
            valid = True
            print("\n\nProgram ended.")
    
main()
