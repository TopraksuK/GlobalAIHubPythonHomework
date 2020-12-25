# Toprak Su Karakaya
# toprak_karakaya@hotmail.com
# First homework for Global AI Hub, Introduction to Python Course


variables = list(range(5))


# Using try/except will help us to determine if the inputted value is either a number or a string
# This method will also work for negative numbers unlike isnumeric() or isdigit() functions
def determine_type(var):
    try:
        if float(var) % 1 != 0:
            return "Float"
        else:
            return "Integer"
    except ValueError:
        if var.upper() == "TRUE" or var.upper() == "FALSE":
            return "Bool"
        else:
            return "String"


# Here the user is inputting the variables
for i, a in enumerate(variables):
    variables[a] = input(f"Enter {str(i+1)}. value: ")


# Here we are printing the values with their type using the function above.
for i, b in enumerate(variables):
    print("{}. Value: {} | Type: {}".format(str(i+1), b.upper() if determine_type(b) == 'Bool' else b, determine_type(b)))

