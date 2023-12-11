# Take Inputs from the usr
usr = input("camelCase: ")

# Intiate an empty string as a container
snake_case = ""

# now iterate over each charchter
for ch in usr:
    if ch.isupper():
        ch = "_" + ch.lower()
        snake_case += ch
    else:
        snake_case += ch


print(f"snake_case: {snake_case}")