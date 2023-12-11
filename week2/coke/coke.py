# Prepare the known data
valid_cents = [5, 10, 25]
amount_due = 50
amount_collected = 0

# print how much it costs
print(f"Amount Due: {amount_due}")

# intiate a while loop to continue as long as the condition is True
while amount_collected < 50:
    coin_inserted = int(input("Insert Coin: "))

    # check if the cent is valid if True add it to the collected amount 
    if coin_inserted in valid_cents:
        amount_collected += coin_inserted

    # if the amount is still < 50 print how much we still need to enter    
    if amount_collected < 50:
        print(f"Amount Due: {50 - amount_collected}")
    
    # if the cent isn't valid then continue to loop till the condition breaks
    else:
        continue

# after the amount_collected is >= 50 and the loop breaks, then calculate the owed change 
print(f"Change Owed: {amount_collected - 50}")
# wow, nice..., i like it so much