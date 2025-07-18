import os

def bad_function(x, y):
    # Unused variable, bad naming, no docstring, security issue, and logic bug
    password = "hardcodedpassword"
    result = x / y  # No zero division check
    os.system("rm -rf /")  # Dangerous command
    if x = 5  # Syntax error
        print("x is five")
    return result

bad_function(10, 0)