# defining a function to handle the cases 
def func(lst):

    if len(lst) == 0:
        return ""
    elif len(lst) == 1:
        return text + lst[0]
    elif len(lst) == 2:
        return text + lst[0] + " and " + lst[1]
    else:
        return f"{text}{', '.join(lst[:-1])}, and {lst[-1]}"


# the first text 
text = "Adieu, adieu, to "

# enpty list 
names = []

# infinite loop
while True:

    try:

        prompt = input("Name: ")

        # on each iteration adding the  input from the user 
        names.append(prompt)

    # handling the (ctrl-D) error
    except EOFError:
        # calling and storing the return of the func
        output = func(names)

        # printing the output
        print(output)
        
        # breaking out of the loop
        break