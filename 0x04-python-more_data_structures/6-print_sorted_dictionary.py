#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for keys in sorted(my_dict.keys()):
        print('{:s}: {}'.format(keys, my_dict[keys]))
