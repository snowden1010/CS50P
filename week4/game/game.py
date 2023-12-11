import random

# a random num generator by random module


def rand_num(num):
    num = random.randint(1, num)
    return num


# inifinite loop 
while True:

    try:
        # prompt
        D = int(input("Level: "))

        # if prompt is not valid
        if D < 0:
            continue

        else:

            # generating the random integer
            l = rand_num(D)
            
            # second loop that get broken when the guess is right
            while True:

                # prompting the user for guesses
                guess = int(input("Guess: "))

                # if the guess is wrong
                if guess != l:

                    # if it's smaller
                    if guess < l:
                        print("Too small!")
                        continue

                    # if it's bigger
                    elif guess > l:
                        print("Too large!")
                
                # if it's right 
                else:
                
                    print("Just right!")

                    # break out of the inner loop
                    break
            
            # break out of the outter loop
            break    
                    
    except ValueError:
        continue
    