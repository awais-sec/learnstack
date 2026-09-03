## Print the greatest number

def greatest(a,b,c):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    elif(c>b or c>a):
        return c
a=3
b=1
c=2
print(greatest(a,b,c))


### OR


def greatest(a=2,b=1,c=4):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    elif(c>b or c>a):
        return c

print(greatest())
