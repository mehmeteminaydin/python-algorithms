def reverse_nested(mylist):
    if type(mylist[-1]) is not list:
        return [mylist[-1]] + reverse_nested(mylist[:-1])
    elif type(mylist[-1]) is list:
        return [mylist[-1][::-1]] + reverse_nested(mylist[:-1])

