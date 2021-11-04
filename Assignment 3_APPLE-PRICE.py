import math

def getMoney():
    myMoney=float(input("\nEnter the amount of money you have: \n= "))
    return myMoney

def getApplePrice():
    applePrice=float(input("\nEnter your desired price for one apple: \n= "))
    return applePrice

def getAppleAmount(getMoneyF, getApplePriceF):
    maxApple=(getMoneyF/getApplePriceF)
    return maxApple

def changeAmount(getMoneyF, getApplePriceF):
    totalPrice=(totalApple * getApplePriceF)
    changePrice=(getMoneyF - totalPrice)
    return changePrice

def neededAmount(getApplePriceF, getMoneyF):
    needed=(getApplePriceF-getMoneyF)
    return needed

def finalTotal(getAppleAmountF,changeTotal):
    if (getAppleAmountF > 1) and (changeTotal > 1):
        return print(f"\nYou can buy {getAppleAmountF} apples and your change is {changeTotal:,.2f} pesos.\n")
    elif (getAppleAmountF > 1) and (changeTotal == 1):
        return print(f"\nYou can buy {getAppleAmountF} apples and your change is {changeTotal:,.2f} peso.\n")
    elif (getAppleAmountF == 1) and (changeTotal > 1):
        return print(f"\nYou can buy {getAppleAmountF} apple and your change is {changeTotal:,.2f} pesos.\n")
    elif (getAppleAmountF == 1) and (changeTotal == 1):
        return print(f"\nYou can buy {getAppleAmountF} apple and your change is {changeTotal:,.2f} peso.\n")
    else:
        return print(f"\nYou cannot buy any apples. You need {need:,.2f} more peso to complete a purchase.\n")

money=getMoney()
apple=getApplePrice()
totalApple=math.floor(getAppleAmount(money,apple))
changeTotal=float(changeAmount(money,apple))
need=float(neededAmount(apple,money))
finalTotal(totalApple,changeTotal)