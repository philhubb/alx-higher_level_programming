#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    if idx < len(new_list) and idx >= 0:
        del(new_list[idx])
    return new_list
