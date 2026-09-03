s = {2,3,553, 'solar'}
print(s, type(s))

s.add('Sly')   
print(s)

length= len(s)
print(length, s)   #output: 5 (cuz we added ont element later)

s.remove('Sly')
print(s)

s.pop() #removes a random number
print(s)

s.clear() #empties the set
print(s)