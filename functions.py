def greeting(name):
    print("Hello World")
    print(f"My name is {name}")

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def upper_name (name):
    return name.upper() 

user_name = input("Enter your name: ")
uppercased_name = upper_name(user_name)
greeting(uppercased_name)

(addition(100, 54))