height=float(input("Enter your height in cm "))
Weight=float(input("Enter your Weight in Kg "))
BMI=Weight/(height*height)
# python follows Bed mas rule same as Bod mas rule in maths
print(BMI)
if BMI <= 18.4:
    print("you are under weight")
elif BMI <= 24.9:
    print("you are Healthy")
elif BMI <= 29.9:
    print("you are over weight")
else:
    print("you are Obese")