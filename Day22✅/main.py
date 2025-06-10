class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return f"Student name is {self.name}, and age is {self.age}"

obj1 = Student("Maroof","17")
print(obj1.show())

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def dev(x,y):
    return x/y

print(add(2,6))
print(sub(15,8))
print(mul(24,87))
print(dev(77,7))