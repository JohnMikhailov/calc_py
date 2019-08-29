from reverse_polish_notation import get_rpn


def get_inputs(path: str) -> list:
    with open(path, 'r') as file:
        return file.readlines()


def parse_symbols_to_list(input_string: str) -> list:
    return list(i for i in list(input_string) if not i.isspace())


path = 'input.txt'
b, rpn = get_rpn(parse_symbols_to_list(get_inputs(path)[0]))
print(rpn)
