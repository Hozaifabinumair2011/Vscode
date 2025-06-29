numberlargest = int(input("Enter the Largest number :"))
numbersmallest = int(input("Enter the smallest number :"))
while numbersmallest:
    numberStore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberStore

print("HCF is:",numberlargest)