weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")