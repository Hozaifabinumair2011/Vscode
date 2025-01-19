a=str(input("Enter your medical cos: Y or N "))
b=float(input("Enter your Attendence "))
if (a=="Y"):
    print("You are eligible")
elif a=="N":
    if b>=75.0:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("invalid")      