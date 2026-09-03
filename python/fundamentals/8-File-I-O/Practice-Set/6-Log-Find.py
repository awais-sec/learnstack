with open("log.html") as f:
    c = f.read()

if("python" in c):
    print("Yes")
else:
    print("No")