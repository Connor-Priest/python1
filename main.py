# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ask_name():
    #ask the users name
    name = input("What is your name :")
    #print the users name
    print(f'Hello {name}')

def number_multiply():
    #ask the user for a number
    number = int(input("Enter a number :"))
    #multiply the users number by itself
    number_multiplied = number * number
    print("Your multiplied number is: ",number_multiplied)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('Connor Priest')
    ask_name()
    number_multiply()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
