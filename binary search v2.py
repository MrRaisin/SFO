wanted = int(input("enter number to find: "))

myList = [1,2,3,4,5,6,7,8,9,10,11]

x = len(myList)

global myList

def nfind(length):
    length = int(length)
    if length % 2 == 0:
        n = int(length / 2)

    elif length % 2 != 0:
        n = int((length - 1) /2)

    return n
                
def nhigher(n):
    x = len(myList)
    length = int(len(myList[n : x]))
    if length % 2 == 0:
        y = int(len(myList[n : x]) /2)
        n = myList[n : x][y]

    elif length % 2 != 0:
        y = int((len(myList[n : x]) - 1) /2)
        n = myList[n : x][y]

    return n



def nlower(n):
    length = int(len(myList[: n]))
    if length % 2 == 0:
        y = int(len(myList[: n]) /2)
        n = myList[: n][y]

    elif length % 2 != 0:
        y = int((len(myList[: n]) - 1) /2)
        n = myList[: n][y]

    return n

n = nfind(x)
found = 'n'

while found == 'n':
    if myList[n] == wanted:
        print("The number is in position:", n)
        found = 'y'
    elif myList[n] > wanted:
        n = nlower(n)
    elif myList[n] < wanted:
        n = nhigher(n)

