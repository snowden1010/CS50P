# Define the list of vowels
vowels = ["u", "a", "e", "i", "o"]

# prompt the user for the text
text = input("Input: ")

# Create a variable as a container of the final text
omitted = ""

# iterate over each character in the text and check whether it is upper or lower.
# and then reassign the character to an empty string if it is in vowels, else append it to the omitted container
for ch in text:

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
print(f"Output: {omitted}")