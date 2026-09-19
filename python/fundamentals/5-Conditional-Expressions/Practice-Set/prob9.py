fruit = input("Choose your fruit :")
liq = input("Choose your liquid :")

if liq == "milk":
    print(fruit,"shake")
elif liq == "water":
    print(fruit,"juice")
else:
    print ("Invalid drink requested")