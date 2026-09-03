def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

goodDay("Hasan", "Thank you for coming.")
goodDay("Ali", "Thank you for coming.")
goodDay("Hammand", "Thank you for coming.")



##OR
def goodDay(name, ending="Thank you for comiing."):
    print("Have a Good Day, " + name)
    print(ending)

goodDay("Hasan")  # Uses default value for `ending`
goodDay("Ali", "See you next time!")  # You can still override the default value
goodDay("Hammand")  # Uses default value for `ending`



##Return
def goodDay(name, ending):  # Defines a function `goodDay` that takes two arguments: `name` and `ending`
    print("Good Day, " + name)  # Prints a greeting message with the provided `name`
    print(ending)  # Prints the `ending` message
    return "Okay"  # Returns the string "Okay" to the caller

# Calls the `goodDay` function with arguments "Hasan" (name) and "Thank you for coming." (ending)
a = goodDay("Hasan", "Thank you for coming.")  
print(a)  # Prints the value returned by the `goodDay` function, which is "Okay"
