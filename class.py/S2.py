class student:
    grade=9
    name="Hozaifa"
    def intro(self):
        print("Hi I am a student")
    def detail(self):
        print("My name is ",self.name)
        print("I study in grade ",self.grade)
ob=student()
ob.intro()
ob.detail()