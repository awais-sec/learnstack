# def Inc_into_Cen(i):
#     c = i * 2.54
#     return c

# i =float(input("Enter inches: "))
# print(round(Inc_into_Cen(i)))

##OR

def Inc_into_Cen(inch):
    return inch * 2.54

n =float(input("Enter inches: "))
print(f"Length in {n} inch = {round(Inc_into_Cen(n),2)}Cm")