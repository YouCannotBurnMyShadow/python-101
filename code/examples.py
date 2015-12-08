# Example 1
print("Hello World!")
variable_name = 1
print(variable_name)

# Example 2
my_string = "Hello World!"
my_string = my_string.upper()
print(my_string)

# Example 3
my_age = 33
my_string = "I am {} years old".format(my_age)
print(my_string)

# Example 4
import datetime
now = datetime.datetime.now()
print(now)

# Example 5
from datetime import datetime
print(datetime.now())

# Example 6
if 1 > 2:
    print("One is bigger than two")
    # This code is actually never reached
else:
    print("One is not bigger than two")

# Example 7
my_string = "5"
my_number = int(my_string)
print(my_number)

# Example 8
value1 = 1
value2 = 0
try:
    result = value1 / value2
except ZeroDivisionError:
    print("ERROR: You can't divide by zero")


# Example 9
def function_name(arg1, arg2, kwarg1=None, kwarg2=None):
    result = arg1 + arg2
    return result
result = function_name(1, 2, kwarg1="Hello")
print(result)

# Example 10
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
all_numbers = numbers + more_numbers
print(all_numbers)
all_numbers.reverse()
print(all_numbers)
all_numbers.append(7)
print(all_numbers)
all_numbers.sort()
print(all_numbers)

# Example 11
import datetime
my_date = datetime.datetime(2015, 12, 8)
print(my_date)

# Example 12
import datetime
my_string = "2015-12-08"
my_date = datetime.datetime.strptime(my_string, "%Y-%m-%d")
print(my_date)

# Example 13
import datetime
my_date = datetime.datetime(2015, 9, 8)
print(my_date.isoweekday())
