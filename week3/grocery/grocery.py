# intiate an empty dict
grocery = {}

# make an infinite loop
while True:

    # cath exceptions
    try:

        # prompt user
        prompt = input().upper()

        # check if the item is in the grocery dic if true add 1
        if prompt in grocery:
            grocery[prompt] += 1

        # add the item for the first time
        else:
            grocery[prompt] = 1

    # handle the exception
    except EOFError:

        for key in sorted(grocery.keys()):
            print(grocery[key], key)
        break

