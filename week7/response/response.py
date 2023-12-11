import validators
import  validator_collection  as col

def main():
    email = input("email :")

    resp = response(email)

    if resp:
        print("Valid")
    else:
        print("Invalid")


def response(s):
    email = validators.email(s)
    if email:
        return True


if __name__ == "__main__":
    main()



