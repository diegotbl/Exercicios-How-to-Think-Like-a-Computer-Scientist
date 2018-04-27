import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def reverse(string):
    """ reverses the string """
    i = len(string)
    new_string = ""
    while i > 0:
        new_string = new_string + string[i-1]
        i = i - 1

    return new_string

def is_palindrome(string):
    """ Checks if string is a palindrome """
    if reverse(string) == string:
        return 1
    return 0

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome("")) # Is an empty string a palindrome?

# Yes, an empty string is a palindrome
