#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print('0 arguments.')
    if len(sys.argv) == 2:
        print('1 argument:')
    if len(sys.argv) > 2:
        print('{} arguments:'.format(len(sys.argv) - 1))
    for x in range(len(sys.argv)):
        if x > 0:
            print('{}:'.format(x), str(sys.argv[x]))
            x = x + 1
