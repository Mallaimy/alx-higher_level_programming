#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k in a_dictionary:
        print("{}: {}".format(k, a_dictionary[k] * 2))
