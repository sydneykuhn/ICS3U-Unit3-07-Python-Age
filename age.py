#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program tells you if you can a date womans grandchild based on age

import random


def main():
    # this function determines your answer

    # input
    user_age_as_string = input("Please enter your age : ")

    # process & output
    try:
        user_age = int(user_age_as_string)

        if user_age >= 25 and user_age <= 39:
            print("You are of a reasonable age to date my grandchild.")
        else:
            print("You are not the right age to date my grandchild.")

    except Exception:
        print("Invalid age entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
