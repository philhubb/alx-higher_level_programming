#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for x in range(len(list)):
        if list[x][1] != '_':
            print(list[x])
