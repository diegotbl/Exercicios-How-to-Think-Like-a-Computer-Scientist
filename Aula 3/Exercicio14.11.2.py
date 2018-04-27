import random
import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calc the absolute y distance
    dx = abs(x1 - x0) # CXalc the absolute x distance
    return dx == dy # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    board_size = [8, 12, 16]
    rng = random.Random() # Instantiate a generator
    tries = 0
    board_size_index = 0
    while board_size_index < len(board_size):
        bd = list(range(board_size[board_size_index])) # Generate the initial permutation
        start = time.time()
        num_found = 0
        tries = 0
        print('Board size: ' + str(board_size[board_size_index]))
        while num_found < 1:
            rng.shuffle(bd)
            tries += 1
            if not has_clashes(bd):
                end = time.time()
                elapsed_time = end - start
                print('Found solution {0} in {1} tries.'.format(bd, tries))
                print('Time elapsed: ' + str(elapsed_time) + ' seconds\n')
                num_found += 1
        board_size_index += 1

main()
