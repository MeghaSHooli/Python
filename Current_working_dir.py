# Python program to explain os.getcwd() method

# importing os module
import os


# Get the current working
# directory (CWD)
cwd = os.getcwd()

# Print the current working
# directory (CWD)
print("Current working directory:", cwd)



# I need to check whether the given file is exist or not with case sensitive.

file = "C:\Temp\test.txt"
if os.path.isfile(file):
    print("exist...")
else:
    print("not found...")
