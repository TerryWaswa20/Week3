def terry():
    print("Hello there, Welcome to function class")

    #calling a function
terry()

def add():
    num = int(input("Enter First Number:"))
    num1 = int(input("Enter second number:"))
    print(f"suim of {num} and {num1} is {num + num1}")

def check_is_odd_even():
    number = int(input("Enter number"))
    if number %2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

add()


