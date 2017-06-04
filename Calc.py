"""
This is simple calculator based on regexp.
Someday I will rewrite using recursive descent parser/
"""

import re
import math


def replace_unary_minus(term):
    pass


def parser_arithmetic(term):
    digit = r'(\#?\d+(\.\d+)?)'
    plus = r'([\+-])'
    mult_div = r'([\*/])'

    while re.search(digit+mult_div+digit, term):
        operation = re.search(digit+mult_div+digit, term)
        if operation.group(3) == '*':
            result = float(operation.group(1)) * float(operation.group(4))
            pattern = operation.group(1) + '\\' + operation.group(3) + operation.group(4)
        else:
            try:
                result = float(operation.group(1)) / float(operation.group(4))
            except ZeroDivisionError:
                term = 'Error expression'
            pattern = operation.group()
        term = re.sub(pattern, str(result), term)

    while re.search(digit+plus+digit, term):
        operation = re.search(digit+plus+digit, term)
        if operation.group(3) == '+':
            result = float(operation.group(1)) + float(operation.group(4))
            pattern = operation.group(1) + '\\' + operation.group(3) + operation.group(4)
        else:
            result = float(operation.group(1)) - float(operation.group(4))
            pattern = operation.group()
        term = re.sub(pattern, str(result), term)
    return term


def find_bkt(term):
    """
    Search for brackets.
    """
    pattern = r'\(([^\(\)]+?)\)'
    operation = re.search(pattern, term)
    if not operation:
        return False
    else:
        result = parser_arithmetic(operation.group())[1:-1]
        return re.sub(pattern, result, term)


def parser_function(term):
    pattern = r'\(.+?\)'
    list_functions = ['cos', 'sin', 'tan', 'log']
    for func in list_functions:
        while re.search(func+pattern, term):
            expression = re.search(func+pattern, term).group()
            operation = re.search(pattern, expression)
            result = parser_arithmetic(operation.group()[1:-1])
            result = float(result)
            if func == 'cos':
                result = math.cos(result)
            elif func == 'sin':
                result = math.sin(result)
            elif func == 'tan':
                result = math.tan(result)
            elif func == 'log':
                result == math.log2(result)
            term = re.sub(func + r'.+?\)', str(result)[:4], term)
    return term


def parser_expression(term):
    term = parser_function(term)
    while find_bkt(term):
        term = find_bkt(term)

    return parser_arithmetic(term)

if __name__ == '__main__':
    term = 0
    while term != 'exit':
        print('Press enter math expression or help:')
        term = input()
        if term != 'help':
            print('Result:')
            print(parser_expression(term))
        else:
            print('This is my first calc.\nIt understands arithmetical operation, trig function and log.'
                   '\nExample:\n3*(3+3)-2\n<Press Enter>')
