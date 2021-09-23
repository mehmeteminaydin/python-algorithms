#It checks two elements of the given list
#if the previous one is greater than the next one, they are replaced
#When nothing is changed, it returns "bubble" sorted list.
def bubble_sorting(mylist):
    another_tour = True
    while another_tour:
        another_tour = False
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                mylist[i],mylist[i+1] = mylist[i+1],mylist[i]
                another_tour=True
    return mylist
