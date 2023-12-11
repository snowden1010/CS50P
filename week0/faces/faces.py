def main():
    user = input("Enter something: ")
    converted = convert(user)
    print(converted)


ico_to_emo = {
    ":)": "🙂",
    ":(": "🙁"
}


def convert(user_in):
    text = user_in
    for ico, emo in ico_to_emo.items():
        text = text.replace(ico, emo)
    return text

if __name__ == "__main__":
    main()