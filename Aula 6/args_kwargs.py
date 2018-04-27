def map_obj_to_key_value(*args, **kwargs):
    """ Input: n strings or numbers and m key-value pairs
        Output: Corresponding values to each string given """

    for arg in args:
        if arg in kwargs.keys():
            print("Object given: {0}\nMapped to: {1}".format(arg, kwargs[arg]))

map_obj_to_key_value("banana", "laranja", "abacaxi",
                     banana = 3, laranja = 5, abacaxi = 8)
