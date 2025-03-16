class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def  info(self):
        print(self.name,self.age)
    def sound(self):
        print("Meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
    def sound(self):
        print("bark")
cat1=cat("Todo",2.5)
dog1=dog("jarvis",8)
for animal in (cat1,dog1):
    animal.sound()
    animal.info()