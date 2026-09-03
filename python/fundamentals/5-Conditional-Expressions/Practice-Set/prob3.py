#ask input for 3 subjects and 49% is passing marks

a1 = int(input('Enter marks 1: '))
a2 = int(input('Enter marks 2: '))
a3 = int(input('Enter marks 3: '))

#total percentage

total_percentage = (100*(a1 + a2 + a3))/300

if(total_percentage>100):   #to be safe from invalidity
    print('Invalid Marks')

elif(total_percentage>=49 and a1>49 and a2>49 and a3>49):
    print('Congrats!', total_percentage)

else:
    print('Try Again...', total_percentage)