wanted = int(input("enter number to find: "))

myList = [1,2,3,4,5,6,7,8,9,10,11]

x = len(myList)

global myList

def nfind(length):
    length = int(length)
    if length % 2 == 0:
        n = int(myList[)

    elif length % 2 != 0:
        n = int((length - 1) /2)

    return n

n = nfind(x)
found = 'n'

while found == 'n':
    if myList[n] == wanted:
        print("The number is in position:", n)
        found = 'y'
    elif myList[n] > wanted:
        x = len(myList[:n][0])
        print(myList)
        n = nfind(x)
    elif myList[n] < wanted:
        x = len(myList[n : x])
        print(myList)
        n = nfind(x)
