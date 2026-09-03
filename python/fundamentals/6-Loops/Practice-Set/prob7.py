# Calculate the factorial number of a given number using loop
# Factorial of 5 is 1x2x3x4x5 

n = int(input('Enter Number: '))
product=1
for i in range(1, n+1):
    product = product * i

print(f'The factorial of {n} is {product}')
