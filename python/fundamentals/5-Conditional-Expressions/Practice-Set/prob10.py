try:
    pocket = int(input("Enter ur roulette number : "))
except ValueError:
    print("Invalid")
else:
    if pocket in range(1, 11):
        print("odd-numbered red & even-numbered black")
        a = pocket % 2
        if a == 1:
            print("red")
        else:
            print("black")

    elif pocket in range(11, 19):
        print("odd-numbered black & even-numbered red")
        a = pocket % 2
        if a == 1:
            print("black")
        else:
            print("red")

    elif pocket in range(19, 29):
        print("odd-numbered red & even-numbered black")
        a = pocket % 2
        if a == 1:
            print("red")
        else:
            print("black")

    elif pocket in range(29, 37):
        print("odd-numbered black & even-numbered red")
        a = pocket % 2
        if a == 1:
            print("black")
        else:
            print("red")

    elif pocket == 0:
        print("green")
    else:
        print("Invalid")
