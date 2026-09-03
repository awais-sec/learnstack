#progarm to find which of the 4 numbers given by user is greatest

a1 = int(input('Enter the number: '))
a2 = int(input('Enter the number: '))
a3 = int(input('Enter the number: '))
a4 = int(input('Enter the number: '))

if(a1>a2 and a1>a3 and a1>a4):
    print('Greatest no is a1', a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print('Greatest no is a2', a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print('Greatest no is a3', a3)

elif(a4>a2 and a4>a3 and a4>a1):
    print('Greatest no is 41', a4)
