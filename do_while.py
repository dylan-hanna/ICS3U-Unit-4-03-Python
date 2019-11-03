#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Oct 2019
# This program uses a do while loop


def main():
    while True:
        try:
            positive_integer = int(input("Enter how many times to repeat: "))
            print("")

            # process & output
            for loop_counter in range(positive_integer + 1):
                calculation = loop_counter ** 2
                print(str(loop_counter) + "^2", "=", str(calculation))
 
                if positive_integer < 0:
                        print("Invalid Input")
                        print()
                        continue

        except ValueError:
                print()
                print("That's.....That's not a number. Do I need to get help?")
                print()
                continue

        else:
            break

if __name__ == "__main__":
    main()