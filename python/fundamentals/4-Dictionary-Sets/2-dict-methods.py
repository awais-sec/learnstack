marks = {
    'Sultan': 80,
    'Ali': 70,
    'Usama': 84,
    'Note': 'Be Cyberaware',
    0: False
}

print(marks.items()) 
print(marks.keys())
print(marks.values())

marks.update({'Note': 5000, 'Ahmar': 93}) #existing element can be updated & new element can be added
print(marks)

print(marks.get("Ahmar")) #prints none
print(marks['Ahmar']) #returns an error