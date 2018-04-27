def write_equal(xs, ys):
    """ Returns only those items that are present in both lists """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): # If xs list is finished,
            return result # We're done.
        if yi >= len(ys): # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] > ys[yi]:
            yi += 1

#_____________________________________________________________________________#

def only_in_first(xs, ys):
    """ Returns items present in the first list but not in the second """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): # If xs list is finished,
            return result # We're done.
        if yi >= len(ys): # Same again, but swap roles
            while xi < len(xs): # Append what's left in xs
                result.append(xs[xi])
                xi = xi + 1
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
        else:
            yi += 1

#_____________________________________________________________________________#

def only_in_second(xs, ys):
    """ Return items present in the second list but not in the first """
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys): # If ys list is finished,
            return result # We're done.
        if xi >= len(xs): # Same again, but swap roles
            while yi < len(ys): # Append what's left in ys
                result.append(ys[yi])
                yi = yi + 1
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        elif xs[xi] == ys[yi]:
            yi += 1
        else:
            xi += 1

#_____________________________________________________________________________#

def either_first_or_second(xs, ys):
    """ Return items present in the first list or in the second but not both """
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys): # If ys list is finished,
            while xi < len(xs): # Append what's left in xs
                result.append(xs[xi])
                xi = xi + 1
            return result # We're done.
        if xi >= len(xs): # Same again, but swap roles
            while yi < len(ys): # Append what's left in ys
                result.append(ys[yi])
                yi = yi + 1
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        else:
            yi += 1

#_____________________________________________________________________________#

def bagdiff(xs, ys):
    """ Returns result of bagdiff operation between first and second lists """
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys): # If ys list is finished,
            while xi < len(xs): # Append what's left in xs
                result.append(xs[xi])
                xi = xi + 1
            return result # We're done.
        if xi >= len(xs): # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        else:
            yi += 1

#_____________________________________________________________________________#
# Defining 2 lists to test the functions
xs = [1, 2, 4, 7, 9]
ys = [1, 2, 2, 3, 6, 8, 9, 10]

print('> The lists are: ' + str(xs) + ' and ' + str(ys) + ' <\n')
print('Elements in both lists: ' + str(write_equal(xs, ys)))
print('Elements in the first list and not in the second: ' +
      str(only_in_first(xs, ys)))
print('Elements in the second list and not in the first: ' +
      str(only_in_second(xs, ys)))
print('Elements in the first or second lists but not both (either): ' +
      str(either_first_or_second(xs, ys)))
print('Bagdiff between the first and second lists: ' + str(bagdiff(xs, ys)))
