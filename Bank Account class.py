class bankAccount():
    '''This is a bank account class'''
    def __init__(self, account_name = "Current Account", balance = 200):
        self.__account_name = account_name
        self.__balance = balance

    def getbalance(self):
        return self.__balance

class savingsAccount(bankAccount):
    def __init__(self, account_name = "Savings Account", balance = 200):
        super().__init__()
        self.__account_name = account_name
        self.__interest_rate = 1.03
        self.__Ibalance = balance

    def deposit(self, value):
        self.__Ibalance = self.__Ibalance + (value * self.__interest_rate)

    def getIbalance(self):
        return self.__Ibalance

    def getInterestRate(self):
        return self.__interest_rate

class currentAccount(bankAccount):
    def __init__(self, balance = 200):
        super().__init__()
        self.__balance = balance


    def Withdraw(self, value):
        if value > 250:
            print("\nYou cannot withdraw that much from here. Please call your bank manager.")

        else:
            if self.__balance - value < 0:
                print("\nYou do not have the funds to withdraw.")
            else:
                self.__balance = self.__balance - value

    def newbal(self):
        return self.__balance

sa = savingsAccount()
ca = currentAccount()

while True:
    print("\n1. Current Account\n2. Savings Account\n")
    option = int(input("Please input your choice: "))
    while option != 1 and option != 2:
        print("That isn' a valid option")
        option = int(input("Please input your choice:"))

    if option == 1:
        print("\nYou have chosen to withdraw")
        value = int(input("\nHow much would you like to withdraw? "))
        ca.Withdraw(value)
        print("\nYour new balance is:",ca.newbal())

    else:
        print("\nYou have chosen to deposit")
        value = int(input("\nHow much would you like to deposit? "))
        sa.deposit(value)
        print("\nYour new balance is:",sa.getIbalance())
