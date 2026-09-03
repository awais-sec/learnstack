a = (12, 1, 442, 928, 12, False, 'Jaguar', 'Bio') 
print(a) 

ik = a.count(12)
print(ik)

ai = a.index('Bio')
print(ai)

print(len(a))

sliced = a[3:5]
print(sliced)

a,b,c,d,e,f,g,h = a #unpacking the tuple
print(b)