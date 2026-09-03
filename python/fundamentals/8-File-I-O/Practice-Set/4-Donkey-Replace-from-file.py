word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

new_content = content.replace("Donkey", "******")

with open("donkey.txt", "w") as f:
    f.write(new_content)