import math
from functools import wraps
def cached(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            fun = function(*args)
            memo[args] = fun
            return fun
    return wrapper

@cached
def multiplication(a, b):
     return  a * b


@cached
def plusandpowl(a, b, c):
    return math.pow(a + b, c)


multiplication(8,4)
plusandpowl(2,2,2)
