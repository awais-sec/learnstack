f = open("word.txt")
file_content = f.read()
print(file_content)
f.close()

#The same code can be written using with statement as follows:

with open("word.txt") as f:
    print(f.read())

#You don't have to explicitly close the file when using with statement. It is done automatically.
#The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers.