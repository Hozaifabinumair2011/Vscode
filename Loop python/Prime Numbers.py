num=int(input("Enter a Number: "))
if num > 1:
    for i in range(2, int(num**0.5) +1 ):
        if num % i == 0:
            print(f"{num} is not a prime num.")
            break
    else:
        print(f"{num} is a prime num.")
else:
    print(f"{num} is not a prime num.")