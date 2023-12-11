import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def regex(string):
    pattern = r"(?:^(1[0-2]|\d)(?:\:(5\d|[0-4]\d))? (AM|PM) to (1[0-2]|\d)(?:\:(5\d|[0-4]\d))? (AM|PM)$)"
    matches = re.search(pattern, string)
    if matches:
        if matches.group(1) != "0":
            return list(matches.groups())
    raise ValueError()


def reformat(hours: list):
    whole = [hours[0:3], hours[3:]]
    for item in whole:
        if item[2] == "AM":
            if len(item[0]) < 2:
                item[0] = f"{int(item[0]):02}"
            else:
                if item[0] == "12":
                    item[0] = "00"
        else:
            if item[0] != "12":
                item[0] = str(int(item[0]) + 12)
        if not item[1]:
            item[1] = "00"
    twenty_four = []
    for i in whole:
        i.pop(-1)
        result = ":".join(i)
        twenty_four.append(result)
    return twenty_four


def convert(s):
    time = regex(s)
    formatted = reformat(time)
    return " to ".join(formatted)


if __name__ == "__main__":
    main()
