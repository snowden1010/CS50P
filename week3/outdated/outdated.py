months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Dict comprehension
# new = {num[i]: months[i] for i in range(len(months))}
months = dict(map(lambda x, y: (y, x), num, months))
    
# intiating an infinite loop  
while True:

    try:

        # prompting the user for input
        user = input("Date: ").capitalize().strip()

        # confirming the user's format 
        if "/" in user:

            # spliting the sring to a list
            user_input = user.split("/")

            # converting
            # [MM/DD/YYYY] to [YYYY/MM/DD]
            year = user_input[-1]

            # adding leading zeros
            day = f"{int(user_input[1]):02d}"
            month = user_input[0]

            # checking the value of the day
            if (int(month) > 12) or (int(day) > 31):
                continue
            
            month = f"{int(user_input[0]):02d}"

            date = [year, month, day]

            # printing the outpus
            print("-".join(date))

            # breaking out of the loop
            break

        # if the user used the other format 
        if "," in user:

            # splitting the user's input
            full_date = user.split(",")
            mmdd = full_date[0]
            year = full_date[-1]

            month, day = mmdd.split()

            month = months[month]

            # checking thevalues of days and months
            if (month > 12) or (int(day) > 31):
                continue
        
            date = [year, month, day]
            edited = []

            # converting operations
            for i in date:
                i = int(i)
                i = f"{i:02d}" 
                edited.append(i)

            date = "-".join(edited)

            # printing and breaking out of the loop
            print(date)
            break
            
    # dealing with caught exceptions
    except ValueError:
        continue
    except KeyError:
        continue
    except EOFError:
        break
    
