import random

# Python classes and objects

# We can package up data into "objects"
# e.g. lists, strings, dictionaries...
# Now we can make our own.

# Objects have
#   1. data/variables/"fields" (things that the object "knows")
#   2. functions/"methods" (things that the object "can do")
#      (e.g. append(), lower(), etc.)

# Classes allow us to design our own objects.
# Classes are like "templates" or "blueprints" for objects.
# An object is an "instance of" a class.
#
# e.g. My car is an instance of the class of all cars.

class Cake:

    # __init__ is a special function that is called when
    # you make a new Cake object.  (i.e. when you call Cake() ).

    # self is a special argument which is filled in automatically
    # by Python; it is a reference to the current object.

    # We can call this by writing something like  Cake(10)
    #   The self parameter is automatically filled in,
    #   and the 10 will be given as 'init_candles'
    def __init__(self, init_candles: int):

        # Create a variable num_candles inside the object
        # we are creating.
        self.num_candles = init_candles

        # This wouldn't work: it would just create a local variable in this function
        # num_candles = init_candles

    # Pick a random number of candles to blow out between 1 and num_candles
    def blow_out(self):
        k: int = random.randint(1, self.num_candles)

        self.num_candles -= k

    # Ask whether all the candles are blown out or not
    def all_out(self) -> bool:
        # if self.num_candles == 0:
        #     return True
        # else:
        #     return False

        # better:
        return self.num_candles == 0
