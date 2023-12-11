
import sys
import inflect
from datetime import datetime


def main():
    try:
        print(word_it(minutes(input("Birth Date: "))))
    except ValueError:
        sys.exit("Invalid Date")


def word_it(num: int) -> str:
    converter = inflect.engine()
    return f"{(converter.number_to_words(num, andword='')).capitalize()} minutes"


def minutes(date: str) -> int:
    today = datetime.now()
    date = datetime.strptime(date, "%Y-%m-%d")
    mins = today - date
    mins = mins.days * 24 * 60
    mins = round(mins)
    return mins






if __name__ == '__main__':
    main()
