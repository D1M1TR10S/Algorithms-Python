#!/usr/bin/python3
'''
    Write multiple functions
    that encode a string
    with square_string encoding
'''
import math


def rot_90_clock(strng):
    s = strng.replace('\n', '')
    new_str = ''
    l = len(s)
    n = math.floor(math.sqrt(l))
    if n != math.sqrt(l):
        n+= 1
    for i in range(n):
        sub = []
        for j in range(n):
            sub.append(s[(j*n)+i])
        sub.reverse()
        new_str += ''.join(sub)
        if i < n-1:
            new_str += '\n'
    return new_str
    
def diag_1_sym(strng):
    s = strng.replace('\n', '')
    new_str = ''
    l = len(s)
    n = math.floor(math.sqrt(l))
    if n != math.sqrt(l):
        n+= 1
    for i in range(n):
        sub = []
        for j in range(n):
            sub.append(s[(j*n)+i])
        new_str += ''.join(sub)
        if i < n-1:
            new_str += '\n'
    return new_str

def selfie_and_diag1(strng):
    s = strng.replace('\n', '')
    new_str = ''
    l = len(s)
    n = math.floor(math.sqrt(l))
    if n != math.sqrt(l):
        n+= 1
    for i in range(n):
        sub = []
        selfy = []
        for j in range(n):
            selfy.append(s[(i*n)+j])
            sub.append(s[(j*n)+i])
        new_str += ''.join(selfy) + '|' + ''.join(sub)
        if i < n-1:
            new_str += '\n'
    return new_str

def oper(fct, s):
    return fct(s)
