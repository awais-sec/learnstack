#len of username, wheater it's 8 digits

username = input('Enter your username: ')

if(len(username)>8):
    print('Valid')

else:
    print('Already Taken')