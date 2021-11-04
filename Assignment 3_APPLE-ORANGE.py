
def getApple():
    appleAmount = int(input("How many apples do you want to purchase? \n= "))
    return appleAmount

def getOrange():
    orangeAmount = int(input("\nHow many oranges do you want to purchase? \n= "))
    return orangeAmount

def get_applePrice():
    applePrice=20
    return applePrice

def get_orangePrice():
    orangePrice=25
    return orangePrice

def get_totalPrice():
    apple=(getApple() * get_applePrice())
    orange=(getOrange() * get_orangePrice())
    totalPrice=float(apple+orange)
    printTotal(_totalPrice=totalPrice)

def printTotal(_totalPrice):
    print(f"\nThe total amount of your purchase is {_totalPrice:,.2f} pesos.\n")

get_totalPrice()
