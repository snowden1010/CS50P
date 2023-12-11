# menu Dictionary 
dic = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# intiate a variable 
total = 0

# use dictionary comprehension to lower the keys 
new_menu = {key.lower(): val for key, val in dic.items()}

# start a while loop
while True:
    
    try:

        # prompt the user for keys and lower them
        prompt = input("Item: ").lower()
        
        # store the value of the prompt in price
        price = new_menu[prompt]

        # update total on each iteration 
        total += price
        
        print(f"Total: ${total:.2f}")
    
    # if a KeyErrors is caught then move to the next iteration 
    except KeyError:
        continue
    
    # if a EOFError is caught then break out of the loop 
    except EOFError:

        # break the  loop 
        break