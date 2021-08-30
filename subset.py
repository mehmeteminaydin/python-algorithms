# It creates the subset of the given list.
def subset(mylist):
    if mylist == []:
        return [[]]
    return subset(mylist[:-1]) + helper(mylist[-1],subset(mylist[:-1]))

# This function helps us to add element into the list items recursively
def helper(element,lst):
    if len(lst) == 0:
        return []
    return [lst[0]+[element]] + helper(element,lst[1:])
