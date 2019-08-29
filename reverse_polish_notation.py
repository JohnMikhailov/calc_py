from functions import get_function


def get_rpn(symbols: list) -> str or list:
    output = []
    stack = []
    for symbol in symbols:
        if symbol.isdigit():
            output.append(symbol)
        if symbol == '(':
            stack.append(symbol)
        if symbol == ')':
            while stack and stack[-1:][0] != '(':
                output.append(stack.pop())
            if not stack:
                return 'error: incorrect delimiter or parenthesis'
            stack.pop()
        if __type(symbol) == 'binary':
            while stack and (
                    __priority(stack[-1:][0]) > __priority(symbol) or
                             (left_associative(stack[-1:][0]) and __priority(symbol) == __priority(stack[-1:][0]))):
                output.append(stack.pop())
            stack.append(symbol)
    if not contains_only_operations(stack):
        return 'error: incorrect parenthesis'
    return output + stack[::-1]


def contains_only_operations(stack):
    return all(True if __type(i) else False for i in stack)


def left_associative(operation):
    return operation in {'^'}


def __type(symbol: str) -> str:
    return {'!': 'postfix',
            'sin': 'prefix',
            'cos': 'prefix',
            'tan': 'prefix',
            'cot': 'prefix',
            '+': 'binary',
            '-': 'binary',
            '*': 'binary',
            '/': 'binary',
            '^': 'binary'}.get(symbol, '')


def __priority(symbol: str) -> int:
    return {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '(': 0,
            ')': 0}.get(symbol, -1)


def calculate(stack, symbol) -> None or float:
    if not stack:
        return None
    func = get_function(symbol)
    if func:
        return func(stack)
    return None


def solve(rpn: str):
    stack = []
    for symbol in rpn:
        if symbol.isdigit():
            stack.append(symbol)
        else:
            stack = calculate(stack, symbol)


