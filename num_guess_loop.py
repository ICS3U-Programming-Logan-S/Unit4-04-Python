#!/usr/bin/env python3
# Created by: Logan S
# Created on: Jan 17, 2022
# This program asks the user to guess a
# number and if they get it wrong they are told so and asks for
# a number between 1 and 10 till they get the right answer.
import random


def main():
    # initialize the counter
    counter = 0
    # generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        # Get the user number as string
        user_number_str = input("Enter a number between 0 and 9: ")
        try:
            # Changing string to integer
            user_number = int(user_number_str)
            # Check to see if they inputted a positive number
            if user_number >= 0 and user_number <= 9:
                # Increment counter
                counter = counter + 1
                if user_number == random_number:
                    # Display result to user
                    print()
                    print("{} is correct!".format(user_number))
                    print()
                    print("Thanks for playing!")
                    break
                else:
                    # Display result to user
                    print()
                    print("{} is incorrect. Try again!".format(user_number))
                    print()
                    print("Tracking {0} times through the loop."
                          .format(counter))
                    print()
            else:
                print("This number is not between 0 and 9")
                print()
        # Catches any exceptions
        except Exception:
            print()
            print("{} is invaild.".format(user_number_str))
            print()


if __name__ == "__main__":
    main()