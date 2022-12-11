import math
from scipy.misc import *

class Derivative():

    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        #return derivative(self.func, x)
        return math.cos(x)

@Derivative
def sin_(x):
    return math.sin(x)

print(sin_(math.pi/3))