"""
Demonstration of some of the features of the import
"""

import datetime



# Create some dates
print("Creating Dates")
print("==============")

date1 = datetime.date(1999, 12, 31)
date2 = datetime.date(2000, 1, 1)

# Today's date
today = datetime.date.today()

print(date1)
print(date2)


print("")

# Compare dates
print("Comparing Dates")
print("===============")

print(date1 < date2)
print("")

# Subtracting dates
print("Subtracting Dates")
print("=================")

diff = date2 - date1
print(diff)
print(diff.days)
print("")


print("Implementing  Practice Project")


#from datetime import datetime

now = datetime.datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

"""
Implementing  Practice Project
"""


def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4


print(name_to_number("myname"))  # output - 0
print(name_to_number("Spock"))  # output - 1
print(name_to_number("paper"))  # output - 2
print(name_to_number("lizard"))  # output - 3
print(name_to_number("scissors"))  # output - 4