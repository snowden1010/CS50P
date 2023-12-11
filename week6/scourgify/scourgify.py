import sys
import csv


def main():
    before, after = check_arg(sys.argv)
    red_wrt_file(before, after)
    


def check_arg(argument):
    argument = argument[1:]

    if len(argument) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(argument) > 2:
        sys.exit("Too many command-line arguments")
    else:
        for file in argument:
            if file[-4:] != ".csv":
                sys.exit("Not a csv")
        
        before, after = argument
        return before, after


def red_wrt_file(before, after):
    try:
        with open(before) as before:
            reader = csv.DictReader(before)
            with open(after, "w") as output_file:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {before}")


if __name__ == "__main__":
    main()