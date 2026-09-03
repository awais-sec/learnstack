class Employee:
    age = 25
    language = "Python" #this is an class attribute
    salary = 50000

Ben = Employee()
print(Ben.age, Ben.salary)

Ben = Employee()
Ben.name = "Ben Tenison" #this is an object attribute
print(Ben.name, Ben.age, Ben.salary)

#Here, Ben is an object of the class Employee. We can access the class attributes using the object as well as the class name.
#But, we can access the object attributes only using the object name.
