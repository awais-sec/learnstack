with open("log.html") as f:
    L = f.readlines()

lineNo = 1
for i in L:
    if("python" in i):
        print(f"Yes {lineNo}")
        break
    lineNo += 1

else:
    print("No")