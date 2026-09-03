def generateTable(n):
    table = ""
    for i in range (1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f"Tables/Table_{n}.txt", "w") as f:
        f.write(table)



for i in range(2, 11):
    generateTable(i)