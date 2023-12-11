# main function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check the length of the Plate
    if len(s) < 2 or len(s) > 6:
        return False
    
    if s.isalnum() == False:
        return False
    # check if the 1st two letters are alpha
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    # check if the 1st enountered digit is not 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            
            # check if the plate contains,digits inside letters
            if s[i:].isdigit() == False:
                return False
            else:
                break
        i += 1

    # check if each character is alphanumeric 
    for c in s:
        if c in [" ", ",", ".", "?", "!"]:
            return False
        
    return True


# call the main
if __name__ == "__main__":
    main()