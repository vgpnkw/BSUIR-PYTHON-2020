import math

def cached(func):
    previous_args = [None, None]
    file = open("result.txt",'a')
    def wrapper(*args, **kwargs):
        if(previous_args[0] == args):
            returned = previous_args[1]
            file.write(str(returned))
            return returned
        else:
            previous_args.clear()
            previous_args.append(args)
            previous_args.append(func(*args, **kwargs))
            returned = previous_args[1]
            file.write('\n' + str(returned))
            return returned
    return wrapper

@cached
def multiplication(a, b):
     return  a * b


@cached
def plusandpowl(a, b, c):
    return math.pow(a + b, c)

multiplication(8,4)
plusandpowl(2,2,2)