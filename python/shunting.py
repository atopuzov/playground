#!/usr/bin/env python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import sys

digits           = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
binary_operators = {'^', '*', '/', '+', '-'}
unary_operators  = {'~'}
operators        = unary_operators.union(binary_operators)
ignore           = {' ', '\t', '\n'}

def get_precedence(token):
    '''
    Returns operator precedence
    :param token: Operator token
    '''
    if token == '~':
        return 5
    elif token == '^':
        return 4
    elif token == '*' or token == '/':
        return 3
    elif token == '+' or token == '-':
        return 2
    else:
        return 0

def tokenize(input):
    '''
    Returns a tokenized expression
    :param input: String expression
    '''
    output = []
    buffer = []

    for char in input:
        if char in ignore:
            if buffer:
                output.append(int(''.join(buffer)))
                buffer = []
            continue
        elif char in digits:
            buffer.append(char)
        elif char in operators or char in {'(', ')'}:
            if buffer:
                output.append(int(''.join(buffer)))
                buffer = []
            else:
                if char == '-':
                    char = '~'
            output.append(char)
    if buffer:
        output.append(int(''.join(buffer)))
        buffer = []
    return output

def shunting_yard(input):
    '''
    Returns RPN of an expression using shunting yard algorithm

    :param input: Tokenized input
    '''
    operator_stack = []
    output = []
    tokens = tokenize(input)

    for token in tokens:
        if type(token) is int:
            output.append(token)
        elif token in operators:
            while operator_stack and \
                  get_precedence(operator_stack[-1]) > get_precedence(token):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and \
                  operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        if operator_stack[-1] == ')':
            print "Unbalanced parantheses."
        output.append(operator_stack.pop())

    return output

def eval_rpn(input):
    '''
    Evaluates rpn expressions
    :param input: Input RPN
    '''
    output = []
    for token in input:
        if type(token) is int:
            output.append(token)
        elif token in operators:
            if token in unary_operators:
                op1 = output.pop()
                if token == '~':
                    val = -op1
            else:
                op1 = output.pop()
                op2 = output.pop()
                if token == '^':
                    val = op1 ** op2
                elif token == '*':
                    val = op1 * op2
                elif token == '/':
                    val = op1 / op2
                elif token == '+':
                    val = op1 + op2
                elif token == '-':
                    val = op1 - op2
            output.append(val)
    return output.pop()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()

    input = sys.argv[1]
    rpn = shunting_yard(input)
    val = eval_rpn(rpn)

    print ' '.join(map(str, rpn)), '=', str(val)
