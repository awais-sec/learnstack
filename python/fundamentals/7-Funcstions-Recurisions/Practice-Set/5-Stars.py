def pattern(n):
    if n == 0:  # Base case: If n is 0, stop the recursion.
        return  # Return means to leave it/ stop
    print("*" * n)  # Print n stars on the current line.
    pattern(n - 1)  # Recursive case: Call the function with (n-1).

pattern(3)  # Call the function with n=3 to start the pattern.
