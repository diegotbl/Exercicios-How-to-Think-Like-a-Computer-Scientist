import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_multiple(a, b):
    """ Checks if 'a' is a multiple of 'b' """
    if a % b == 0:
        return 1
    return 0

test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))

# Yes, we can use is_factor from Exercise 6.9.16 in the definition of
# is_multiple like this:
#
# def is_multiple(a, b):
#     """ Checks if 'a' is a multiple of 'b' """
#     return is_factor(b, a)
