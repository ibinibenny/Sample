def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("you are dividing a number by ZERO!!:",ze)
except:
    print("Any other exception")
