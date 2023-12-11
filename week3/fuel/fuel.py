# intiate a while loop
while True:
    # prompt the user
    prompt = input("Fraction: ").strip()

    # use the try statement in case a exception might occure 
    try:

        # cases where's an exception might occur
        a, b = prompt.split("/")
        a = int(a)
        b = int(b)

        # just to keep thing logically 
        if a > b:
            continue  # reprompt the user 

        # calculate the quantity filled
        q = a / b * 100

        q = round(q)  # roud it to the nearest int

    # Catch exceptions
    except ValueError:
        continue  # if catched reprompt the usr
    else:
        break  # if no exception occured then break out of the loop


# Make how to ouput the result



