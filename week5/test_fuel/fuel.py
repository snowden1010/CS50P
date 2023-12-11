# defining the main function which takes care of the side effect 
def main():
    prompt = input("Fraction: ")
    fraction = convert(prompt)
    
    gauge_1 = gauge(fraction)
    print(gauge_1)


# defining the conver which returns the fraction of the x/y and raises ValueError if (x > y )or (x and/or y isn't an int) 
# if y == 0 then it raises a ZeroDevisionError
def convert(fraction):
    x, y = fraction.split("/")
    try:
        x, y = int(x), int(y)
        
        if y == 0:
            raise (ZeroDivisionError)
        if x > y:
            raise (ValueError)
        q = (x/y)
        q = round(q * 100)
        return q
    except ValueError:
        raise (ValueError)
    

# defining the gauge func which takes in an int, and ouputs the indications f the gauge based on that int
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    else:
        return "F"


# calling main conditionally
if __name__ == "__main__":
    main()