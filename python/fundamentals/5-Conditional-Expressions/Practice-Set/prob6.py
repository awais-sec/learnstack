#whether your name is in the list or not

l = ['Ahmar', 'Sultan', 'Ali', 'Usama', 'Ash']      #NOTE: pythoncase sensitive

a = input('Enter your name: ')

if(a in l):
    print('You are in list.')

else:
    print('Your name is not in the list.')

