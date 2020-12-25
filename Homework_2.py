# Toprak Su Karakaya
# toprak_karakaya@hotmail.com
# Second homework for Global AI Hub, Introduction to Python Course


# We will use a list like so in order use for-loops easier
data = ['First Name: ', 'Last Name: ', 'Age: ', 'Year of Birth: ']
info = list(range(4))


# Here the user is inputting the values
for i, a in enumerate(info):
    info[i] = input(f"Enter your {data[i]}")


# Here we are displaying the values
for i, b in enumerate(info):
    print(data[i] + b)


# Here we are telling the user if they can go out or not depending on their age
if int(info[2]) >= 18:
    print("You can go out the street.")
else:
    print("You can't go out because it's too dangerous.")

