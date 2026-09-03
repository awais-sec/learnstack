#program to detect spam comments

c1 = 'make money'   #spams comments
c2 = 'subscribe'
c3 = 'fake'
c4 = 'link'

comment = input('Comment Here: ')

if(c1 in comment, c2 in comment, c3 in comment, c4 in comment):
    print('Spam!')

else:
    print('Valid')
