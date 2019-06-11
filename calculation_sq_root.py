# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# A decorator is a function that takes one function as input and returns another function.

import math


c = 50
h = 30
value = []


def debug_calculation(calc_fn):
    def print_input_output(*args):
        print("c = %d" % c)
        print("D= ", *args)
        print("H=%d" % h)
        result = calc_fn(*args)
        print("result = ", result)
    return print_input_output


@debug_calculation
def calculate_sq_root(items):
    for d in items:
        value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    return ','.join(value)


def main():
    items = [x for x in input("Enter comma separated values for calculation").split(',')]
    try:
        calculate_sq_root(items)
    except:
        print("Invalid input?")


if __name__ == '__main__':
    main()



