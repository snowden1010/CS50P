# importing the emoji package
import emoji


# creating a function to convert
def emojize_it(string):
    value = emoji.emojize(string, language="alias")
    return "Output: " + value


# prompt the user
prompt = input("Input: ")

# use the func and print the result
print(emojize_it(prompt))

