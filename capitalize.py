# Function to capitalize each phrase in the full name 

def solve(s):
    for name in s.split():
        s = s.replace(name,name.capitalize())
    return s
