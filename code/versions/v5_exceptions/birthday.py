import sys
BIRTHDAY = "1982-09-08"
age = None
try:
    age = int(sys.argv[1])
except ValueError:
    print("ERROR: Please enter an integer")

if age is not None:
    if age < 0:
        print("ERROR: Negative ages are not allowed")
    else:
        message = "I am born {} and I am {} years old".format(BIRTHDAY, age)
        print(message)
