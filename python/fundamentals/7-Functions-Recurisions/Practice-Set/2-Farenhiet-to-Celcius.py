def F_into_C(f):
    c=5*(f-32)/9
    return c

f=int(input("Enter temperature into F: "))
print(round(F_into_C(f), 2))

# OR # print(f"{round(F_into_C(f), 2)}")


