def predecessor_successor(func):

    def wrapper(n):
        print("The predecessor is: ")
        func(n-1)
        print("The succesor is: ")
        func(n+1)

    return wrapper

@predecessor_successor
def number(n):
    """ Prints n """
    print(n)

number(9)
