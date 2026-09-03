with open("donkey.txt")as f:
    content1 = f.read()

with open("donkey_copy.txt")as f:
    content2 = f.read()

if(content1==content2):
    print("Files are identical")
else:
    print("Files are not identical")