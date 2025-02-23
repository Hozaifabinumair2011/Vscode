class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
ob=parrot("Blue",10)
print(ob.name,ob.age)