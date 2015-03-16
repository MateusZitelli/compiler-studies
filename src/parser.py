#!/usr/bin/env python

"""
This is an implementation of a LL(1) parser for LISP systax programs. This
accepts the four basic arithmetic operations (+ - * /) and integer numbers.
e.g.: (+ (/ 2 3) 5)
"""

import re

# Terminals tokens
T_OPENPAR = 0
T_CLOSEPAR = 1
T_PLUS = 2
T_MINUS = 3
T_TIMES = 4
T_DIVIDE = 5
T_INT = 6
T_END = 7
T_INVALID = 8

# Grammar
R_STMT = 0
R_STMTS = 1
R_STMTS2 = 2
R_OP = 3

# Types
RULE = 0
TERM = 1


def getTerm(term):
    return (TERM, term)


def getRule(rule):
    return (RULE, rule)

rules = [
    # (OP STMTS)
    [getTerm(T_OPENPAR), getRule(R_OP), getRule(R_STMTS), getTerm(T_CLOSEPAR)],
    # STMT STMTS'
    [getRule(R_STMT), getRule(R_STMTS2)],
    # +
    [getTerm(T_PLUS)],
    # -
    [getTerm(T_MINUS)],
    # *
    [getTerm(T_TIMES)],
    # /
    [getTerm(T_DIVIDE)],
    # int
    [getTerm(T_INT)],
    # Empty
    []
]

table = [
    [0, -1, -1, -1, -1, -1, 6, -1],
    [1, -1, -1, -1, -1, -1, 1, -1],
    [1,  7, -1, -1, -1, -1, 1, -1],
    [-1, -1, 2, 3, 4, 5, -1, -1],
]


def lexicalanalysis(program):
    ''' lexicalanalysis
    Receive a program as raw text input and return the list of the tokens in
    result of an lexical analysis.
    '''
    buff = []
    tokens = []
    for char in program:
        if(char == ' '):
            buff = []
            continue

        buff.append(char)
        joinedBuffer = ''.join(buff)

        if joinedBuffer == '(':
            tokens.append(T_OPENPAR)
            buff = []
        elif joinedBuffer == ')':
            tokens.append(T_CLOSEPAR)
            buff = []
        elif joinedBuffer == '+':
            tokens.append(T_PLUS)
            buff = []
        elif joinedBuffer == '-':
            tokens.append(T_MINUS)
            buff = []
        elif joinedBuffer == '*':
            tokens.append(T_TIMES)
            buff = []
        elif joinedBuffer == '/':
            tokens.append(T_DIVIDE)
            buff = []
        elif re.match('[0-9]+', joinedBuffer):
            tokens.append(T_INT)
            buff = []
        else:
            tokens.append(T_INVALID)
            buff = []

    tokens.append(T_END)
    return tokens


def syntaticalanalysis(tokens):
    """ syntaticalanalysis
    It checks if a list of tokens represents a valid program based on the
    parsing table
    """
    stack = [getTerm(T_END), getRule(R_STMT)]
    position = 0
    while len(stack) > 0:
        token = tokens[position]
        if token == T_INVALID:
            print("Bad input on", token)
            return False
        (ttype, tvalue) = stack.pop()
        if ttype == TERM:
            if tvalue == token:
                position += 1
                print("Terminal", tvalue)
                if(tvalue == T_END):
                    print("Input accepted")
                    return True
            else:
                print("Bad input on", token)
                return False
        elif ttype == RULE:
            rule = table[tvalue][token]
            if(rule < 0):
                print("Bad input on", token)
                return False
            print('Rule:', rule)
            stack += reversed(rules[rule])
            print('Stack', stack)

if __name__ == "__main__":
    program = raw_input('Type an input program:\n')
    syntaticalanalysis(lexicalanalysis(program))
