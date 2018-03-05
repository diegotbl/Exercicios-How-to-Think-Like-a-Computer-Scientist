import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_factor(a, b):
    """ Checks if 'a' is a factor of 'b' """
    if b % a == 0:
        return 1
    return 0

test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))

# Yes, as we can see in the tests at lines 22 and 23 we do treat 1 and 15 as
# factors of 15
