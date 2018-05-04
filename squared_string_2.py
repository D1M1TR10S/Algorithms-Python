#!/usr/bin/python3
'''
    Write multiple functions
    that encode a string
    with square_string encoding.
    This file has alternative
    one-liner solutions.
'''
def rot_90_clock(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n')[::-1]))      
def diag_1_sym(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n'))) 
def selfie_and_diag1(strng):
    return '\n'.join('|'.join(x) for x in zip(strng.split('\n'), diag_1_sym(strng).split('\n')))
def oper(fct, s):
    return fct(s)
