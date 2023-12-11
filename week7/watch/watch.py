import re
import sys


# defining the main func
def main():
    # printing the return value of parse func
    print(parse(input("HTML: ")))


# def the parse func which searchs for patterns in the html code and return a short sharable link, returns None if no pattern found
def parse(s: str):
    patterns = r'src=\"https?://(?:www\.)?youtube\.com/embed/(.*?)\"'

    # ignoring the case
    matches = re.search(patterns, s, re.IGNORECASE)
    # if a match caught
    if matches:
        # if the match isn't an empty string
        if matches.group(1) != "":
            # return the short YT link
            return f"https://youtu.be/{matches.group(1)}"
    # return None, no match or an empty string    
    return None


# calling main() conditionally
if __name__ == "__main__":
    main()
