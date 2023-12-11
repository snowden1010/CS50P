# ask for input & make it cas-insensitive as well as striping the spaces
user = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
user = user.lower().strip()

# matching the user's input with the favorable answers 
match user:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")