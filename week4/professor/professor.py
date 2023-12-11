import random


# Defining the get level func which accepts only one of :[1, 2, 3], and returns it 
def get_level():
    while True:
        try:
            prompt = int(input("Level: "))
            if prompt not in [1, 2, 3]:
                continue
            else:
                return prompt
        except ValueError:
            continue


def generate_integer(level):
    """
    generate:integer func which takes in the level and represent it as the number of digits
    and returns a tuple of two random integers, with the n digits of level.
    if the level n isn't in [1, 2, 3], a ValueError will be raised

    """
    if level in [1, 2, 3]:
        value = 0
        if level == 1:
            min_value = value
            max_value = 10 ** level - 1
        elif level > 1:
            min_value = 10 ** (level - 1)
            max_value = 10 ** level - 1

        return (random.randint(min_value, max_value), random.randint(min_value, max_value))
    else:
        raise ValueError("Expected 1, 2, 3")
    

# Defining the main function
def main():
    # intializing number of questions and the intial score 
    questions = 0
    score = 0

    level = get_level()

    # making a loop that will break after 10 questions 
    while questions < 10:
        
        # in each iteraton add 1 to the questions variable
        questions += 1
        # store the integers from the tuple
        x, y = generate_integer(level)
        # store the correct answer 
        solution = x + y       

        # intial a trails var which's going to be the number of trials the user has 
        trials = 0
        
        # a loop that will break when the number of trials is == 3
        while trials < 3:
            # addding one to in each iteration
            trials += 1

            # handling errors 
            try:
                # prompting for answers
                prompt = int(input(f"{x} + {y} = "))
                if prompt == solution:

                    # adding one the the score if the answer is correct, then break out 
                    score += 1
                    break 
                else:
                    # print the "EEE" message, if the answer is wrong
                    print("EEE")
                    continue
            
            except ValueError:
            
                print("EEE")
                continue

        # when trails is == 3, then print the correct answer       
        if trials == 3:
            print(f"{x} + {y} =", solution)
    
    # after 10 addition problems, print the score 
    print("Score:", score)


if __name__ == "__main__":
    main()