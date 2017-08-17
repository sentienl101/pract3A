"""
CP1404/CP5632 - Practical
Get a valid name and display parts of it
"""


def version_1():
    #Get name thing, without functions.
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")

    print(name[::2])

def main():
    #Get and print name
    name = get_name()
    print_parts(name, 3)


def print_parts(name, step=2):
    #Display step character of name.
    print(name[::step])


def get_name():
    #Get a valid name.
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name


main()