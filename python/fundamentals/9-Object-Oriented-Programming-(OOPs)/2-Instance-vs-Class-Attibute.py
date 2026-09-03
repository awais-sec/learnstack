class Employee:
    age = 25
    language = "Python" #this is an class attribute
    salary = 50000

Ben = Employee()
Ben.name = "Ben Tenison" #this is an object attribute
Ben.language = "CSS"

print(Ben.name,Ben.language, Ben.age, Ben.salary)
