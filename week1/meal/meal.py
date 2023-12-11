# def the main function where prompts the user for time and convert it using convert func
def main():
    time = input("what time is it? ").strip()
    num = convert(time)
    
    #  Develop a logic
    if num >= 7 and num <= 8:
        print("breakfast time")

    elif num >=12 and num <= 13:
        print("lunch time")

    elif num >= 18 and num <= 19:
        print("dinner time")


# def the convert func     
def convert(time):
    a, b = time.split(":")
    num = a + "." + b
    h, m = int(a), int(b)
    time_float = h + m / 60
    return time_float
    


# call the main func
if __name__ == "__main__":
    main()