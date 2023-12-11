import sys


# defining the main function
def main():
    filename = check_arg(sys.argv[1:])
    lines = file_reader(filename)
    print(lines)


# defining a function that counts lines of code (LOC)
def count_lines(line):

    if (line.lstrip().startswith("#") or (line.isspace())): 
        return 0
        
    else:
        return 1


# defining a function to check the argument and returns the filename
def check_arg(argument):
    
    if len(argument) == 0:
        sys.exit("Too few command-line arguments ")
    elif len(argument) > 1:
        sys.exit("Too many command-line arguments")
    else:
        argument = argument[0]
        if argument[-3:] != ".py":
            sys.exit("Not a Python file")
        
        return argument


# defining a function which opens the file and calls a counting function    
def file_reader(argument):
    try:
        # opening the file 
        with open(argument) as file:
            # defining a container var
            lines = 0
            # iterating over each line in the file
            for line in file:
                # counting by adding 1 or 0 on each iteration
                loc = count_lines(line)
                # adding the result
                lines += loc

            # retutrn the total of LOC
            return lines
        
    # if an exception occured exit
    except FileNotFoundError:
        sys.exit("File does not exist")


# calling main conditionally
if __name__ == "__main__":
    main()