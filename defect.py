import os

def authenticate(username, password):
    # Hard-coded password (security issue)
    if password == "admin123":
        return True
    return False

def run_command(cmd):
    # Dangerous function usage (security issue)
    os.system(cmd)

def add(a, b):
    return a + b

def subtract(a, b):
    # Missing docstring (documentation issue)
    return a - b

# Unused variable (style issue)
x = 42
