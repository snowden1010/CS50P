# Define the list of vowels
vowels = ["u", "a", "e", "i", "o"]


def main():
    print(shorten(input("Input: ")))


def shorten(word: str):

    omitted = ""

    for ch in word:

        if ch.isupper():

            if ch.lower() in vowels:

                ch = ""
                omitted += ch
            else:

                omitted += ch
        else:

            if ch in vowels:
                ch = ""
                omitted += ch

            else:
                omitted += ch

    return omitted



if __name__ == "__main__":
    main()