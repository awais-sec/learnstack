with open("donkey.txt")as f:
    content = f.read()

with open("donkey_copy.txt", "w") as f:
    f.write(content)