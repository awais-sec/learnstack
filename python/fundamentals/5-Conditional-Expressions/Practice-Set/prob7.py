#calculate grade of the student 

marks = int(input('Enter your Marks'))

if(marks<=100 and marks>=80):
    print('A')
elif(marks<80 and marks>=60):
    print('B')
elif(marks<60 and marks>=50):
    print('C')
elif(marks<50):
    print('F')
