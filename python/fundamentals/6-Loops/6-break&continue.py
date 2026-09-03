for i in range(100): # till 99
    if(i == 34):     # but if i reaches 33
        break        # break the loop right now
    print(i)         # NOTE: if print is out of indentation it will only considor condition and output will be 34

print('Space')#<br>

for i in range(100):
    if(i == 34):
        continue # skip this iteration/value
    print(i)