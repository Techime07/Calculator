#  +, -, *, /

number_one = int(input("First Numer: "))
operation = input("Operation: ")
number_two = int(input("Number: "))


if operation == "+":
    sum = number_one + number_two 
    print("Sum is " + str(sum))

elif operation == "-":
    sum = number_one - number_two
    print("Sum is " + str(sum))

elif operation == "*":
    sum = number_one * number_two
    print("Sum is " + str(sum))

elif operation == "/":
    sum = number_one / number_two
    print("Sum is " + str(sum))

else :
    print("Operation not found")