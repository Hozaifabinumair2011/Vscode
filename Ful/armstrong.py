a=int(input("Enter a Number: "))
t=a
sum=0
while a>0:
    d = a % 10
    sum= sum +(d*d*d)
    a = a // 10
if sum == t :
    print("Yes")
else:
    print("No")