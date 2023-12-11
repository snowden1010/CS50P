import random
import sys
import pyfiglet as fglt


# store all available fonts in a variable
options = fglt.FigletFont.getFonts()

# allowed commands
commands = ["-f", "--font"]


# defining the rendering function
def render(font, something):
    f = fglt.Figlet(font=font)
    return f.renderText(something)


# defining the main function
def main():
    
    # if the user gave < 2 arguments
    if len(sys.argv) < 2:
        D = input("Input: ")
        # choose a random font
        font = random.choice(options)
        # call the function
        output = render(font, D)
        print("Output:\n", output)

    # if the user entered 2 arguments then check if they are valid
    elif len(sys.argv) == 3:
        if (sys.argv[1] not in commands) or (sys.argv[2] not in options):
            sys.exit("Invalid usage")

        # if valid:
        else:
            # prompt
            D = input("Input: ")
            # store the value returned by the render function
            output = render(sys.argv[2], D)

            print("Output:\n", output)
    # if the user enterd more than 3 arguments exit with error message
    else:
        sys.exit("Invalid usage")


# call the main function    
if __name__ == "__main__":
    
    main()
