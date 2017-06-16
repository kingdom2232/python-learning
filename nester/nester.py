import sys
"""
This is a function for print list
"""
def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent, level+1, file)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=file)
            print(item)
