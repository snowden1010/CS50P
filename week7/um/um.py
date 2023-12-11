import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = "um"
    regex = re.compile(r"\b" + re.escape(pattern) + r"\b", re.IGNORECASE)
    times = len(regex.findall(s))
    return times


if __name__ == "__main__":
    main()
