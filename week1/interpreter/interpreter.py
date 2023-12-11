# Ask for Expressions
p = input("Expression: ")

# Split the input 
x, y, z = p.split()

# Convert the numerical values to float
x = float(x)
z = float(z)

# Develop the Logic
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)