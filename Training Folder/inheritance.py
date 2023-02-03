# class Person(object):
   
#   # Constructor
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id
 
#   # To check if this person is an employee
#   def show(self):
#     print(self.name, self.id)

# class Emp(Person):
   
#   def details(self):
#     print("Emp class called")
     
# Emp_details = Emp("Mayank", 103)
# Emp_details.show()
# Emp_details.details()
class Employee:
    def __init__(self,name,age,eid,role):
        self.name = name
        self.age = age
        self.eid = eid
        self.role = role
    def saySomething(self):
        print("Hello, My name is ",self.name," and I am a ",self.role)

class Developer(Employee):
    def __init__(self,name,age,eid,role):
        super().__init__(name,age,eid,role)

d1 = Developer("John",43,"Developer",["Python","Java"])
d1.saySomething()