import sys
from PIL import Image, ImageOps


def validate(argument):
    """
    validate(argumnet) 
    accepts exactly 2 CL-arguments and returns them if passed all the checks 
    """
    argument = argument[1:]
    valid = ["jpeg", "jpg", "png"]

    args = list(map(lambda f: f.lower(), argument))

    if (len(args) < 2):
        sys.exit("Too few command-line arguments")
    if (len(args) > 2):
        sys.exit("Too many command-line arguments")
    in_file, out_file = args
    exts = []
    for _file in args:
        ext = _file.split(".")[-1]
        
        if ext not in valid:
            sys.exit("Invalid input")
        
        else:
            exts.append(ext)

    if exts[0] != exts[1]:
        sys.exit("Input and output have different extensions") 

    return (in_file, out_file)   
    

def crop(file):
    """
    `crop(file)`
    takes in an image file, then crops(resizes) it to 600x600 
    """
    try:
        # opening the file
        person = Image.open(file)
        # croping it
        person = ImageOps.fit(person, (600, 600))
        return person
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay(shirt, person, output):
    """
    overlay(shirt, person, output)
    takes in 3 positional arguments
    shirt:(Image)I took CS50 shirtificate
    person:(Image)an image object 
    output:(Image)the output file
    """
    shirt = Image.open(shirt)
    person.paste(shirt, (0, 0), shirt)
    # saving the final image with the output filename
    person.save(output)


def main():
    # validating the CL-args, and storing the tuple in the student and the output filename
    student, output = validate(sys.argv)
    student = crop(student)
    overlay("shirt.png", student, output)


# calling main() conditionally
if __name__ == "__main__":
    main()