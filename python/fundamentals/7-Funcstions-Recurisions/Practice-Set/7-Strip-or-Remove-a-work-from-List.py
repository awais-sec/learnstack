def rem(l, word):  # Function to remove 'word' from items in list `l`
    n = []  # Create an empty list to store modified items
    for item in l:  # Loop through each item in the list `l`
        if not(item == word):  # Check if the current item is NOT equal to `word`
            n.append(item.strip(word))  # Remove occurrences of `word` from the current item and add it to list `n`
    return n  # Return the modified list `n`

l = ["ali", "alan", "anil", "lana", "anushka"]  # Input list
print(rem(l, "an"))  # Call the function and print the result


##OR


# def rem(l, word):
#     n=[]
#     for item in l:
#         if item != word:
#             n.append(item.strip(word))
#     return n
# l=["jiji", "kiji", "kuji"]
# print(rem(l, "ji"))