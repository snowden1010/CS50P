# Ask for input from the user, and format the greeting, 
ss = input("Greeting: ")
ss = ss.lower().strip()

# Develop a logic to handel the hello and h cases as well as strings without h at the beginning
if ss[0] == "h":
    if ss[:5] == "hello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")