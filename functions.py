from functools import reduce


def add(args):
    return sum(args)


def sub(args):
    return reduce(lambda x, y: x - y, args)


def mult(args):
    return reduce(lambda x, y: x * y, args)


def div(args):
    return reduce(lambda x, y: x / y, args)


def power(args):
    return reduce(lambda x, y: x ** y, args)


def get_function(sign):
    return {'+': add,
            '-': sub,
            '*': mult,
            '/': div,
            '^': power}.get(sign, '')
