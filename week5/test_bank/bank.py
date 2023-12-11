

def main():
    prompt = input("Greeting: ")
    prompt = prompt.lower()
    greeting = value(prompt)
    print(f"${greeting}")



def value(greeting):


    if len(greeting) == 0:
        return 100
    else:

        if greeting[0] == "h":
            if greeting[:5] == "hello":
                return 0
            else:
                return 20
        else:
            return 100


if __name__ == "__main__":
 
    main()
