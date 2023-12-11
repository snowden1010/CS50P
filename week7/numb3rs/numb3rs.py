import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(Ip: str) -> bool: 

    # defining the pattern prefixed with the r for a raw string
    pattern = r'^(:?25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(:?25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(:?25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(:?25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
 
    # using re.search() to search the patterns in the ip while ignoring the case
    matches = re.search(pattern, Ip, re.IGNORECASE)
    if matches:
        return True
    else:
        return False


# calling main() conditionally
if __name__ == "__main__":
    main()