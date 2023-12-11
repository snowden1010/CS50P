from tabulate import tabulate
import csv
import sys

# defining the main function
def main():
    filename = check_arg(sys.argv)
    data = read_file(filename)
    table = table_data(data)
    print(table)


# defining a function that only allows for one command-line argument, otherwise an exit erro will be displayed
def check_arg(argument):
    """
    takes in a argument specifically a sys.argv argument.
    if more than one CL argument entered an exit message will be displayed, else it returns that one argument
    """
    # slicing the comand-line argument's list
    argument = argument[1:]
    # if 0 arguments entered
    if len(argument) == 0:
        sys.exit("Too few command-line arguments ")
    # if more than 1
    elif len(argument) > 1:
        sys.exit("Too many command-line arguments")
    # if one command-line arg entered
    else:
        # storing the filename ina var
        filename = argument[0]
        # if it doesn't have a .csv extention then exit
        if filename[-4:] != ".csv":
            sys.exit("Not a CSV file")
        # return the file name
        return filename


# defining a read file function    
def read_file(filename):
    """
    takes in a file name or file path. 
    and returns a data formated in a list of lists, or an exit error
    """
    try:
        # oepening the file in read mode
        with open(filename) as file:
            data = []
            # using csv.reader
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

            # return the data
            return data
    # if an exception occured
    except FileNotFoundError:
        sys.exit("File does not exist")


def table_data(data):
    """
    takes in a data formated as a list of lists, the it returns that data, in a table using ascii art
    """
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    return table

if __name__ == "__main__":
    main()
