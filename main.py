# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def ask_name():
    # ask the users name
    name = input("What is your name :")
    # print the users name
    print(f'Hello {name}')


def number_multiply():
    # ask the user for a number
    number = int(input("Enter a number :"))
    # multiply the users number by itself
    number_multiplied = number * number
    print("Your multiplied number is: ", number_multiplied)


def word_count():
    # ask the user for a word
    word = input("Please enter a word: ")
    # count the letters in the word and print the number
    print(len(word))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def loop():
    array = [['.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.'],
              ['.', 'O', '.', 'O', '0', '0', '.'],
              ['.', '.', '.', '.', '.', '.', '.'],
              ['.', 'O', 'O', 'O', '0', '0', '.'],
              ['.', '.', '.', '0', '.', '.', '.'],
              ['.', '.', '.', '0', '.', '.', '.'],
              ['.', 'O', '0', '0', '0', '0', '.'],
              ['.', '.', '.', '.', '.', '.', '.']]
    print("Array: ")
    for i in array:
        for j in i:
            print(j, end=" ")
        print()


def coin_flip():
    number = int(input("Heads'(0)' or Tails'(1)': "))
    flip = random.randint(0, 1)
    if flip == 0:
        print("Heads")
    else:
        print("Tails")
    if number == flip:
        print("You Win!")
    else:
        print("Sorry try again...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Connor Priest')
    # ask_name()
    # number_multiply()
    # word_count()
    loop()
    # coin_flip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
