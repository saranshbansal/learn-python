class Person:
    def __init__(self, firstname="[no first name]", lastName="[no last name]"):
        self.firstname = firstname
        self.eyecolor = "[no eye color]"
        self.age = -1


myPerson1 = Person()
print(myPerson1.firstname)

myPerson2 = Person(firstname="Jack")
print(myPerson2.firstname)

myPerson3 = Person("Linda")
print(myPerson3.firstname)
