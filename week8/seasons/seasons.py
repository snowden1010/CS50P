
import sys
import inflect
from datetime import date, datetime


def main():
    try:
        print(word_it(minutes(input("Birth Date: "), date.today())))
    except ValueError:
        sys.exit("Invalid Date")


def word_it(num: int) -> str:
    converter = inflect.engine()
    return f"{(converter.number_to_words(num, andword='')).capitalize()} minutes"


def minutes(date: str, today) -> int:
    date = datetime.strptime(date, "%Y-%m-%d").date()
    years = today - date
    days = years.days
    hours = days * 24
    mins = hours * 60
    return round(mins)


if __name__ == '__main__':
    main()
