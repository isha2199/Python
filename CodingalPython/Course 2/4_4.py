a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Middle number is:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Middle number is:", b)
else:
    print("Middle number is:", c)