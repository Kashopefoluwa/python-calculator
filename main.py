user_name = input("Enter your name: ")
message = f"\nWelcome {user_name}, to our calculator app"
print(message)

num_one = input("Enter first number to add")
num_two = input("Enter second number to add")

result = int(num_one) + int(num_two)

answer = f"The addition of {num_one} and {num_two} is {result}"
print(answer)
print ("Thank you for using our calculator app")