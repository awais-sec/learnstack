#Print a table using while-loop

n = int(input("Enter the nuber: "))

i=1
while(i<11):
    print(f"{n} x {i} = {n * i}") #f string can be used in print    
    i += 1