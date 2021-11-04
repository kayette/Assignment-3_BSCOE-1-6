def getName ():
    _name = input("Enter your name: ")
    return _name

def getAge ():
    _age = int(input("Enter your age: "))
    return _age

def getAddress ():
    _address = input("Enter your address: ")
    return _address

def display(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.")

name = getName()
age = getAge()
address = getAddress()
display(name, age, address)