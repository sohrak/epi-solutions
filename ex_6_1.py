import string
from functools import reduce


def int_to_string(x: int) -> str:
    s = ''
    neg = False
    if x < 0:
        neg = True
        x = -x

    while True:
        s = chr(ord('0') + (x % 10)) + s
        x //= 10
        if x == 0:
            break

    if neg:
        s = '-' + s

    return s


def string_to_int(s: str) -> int:
    neg = False
    val = 0
    for c in s:
        if c == '-':
            neg = True
        elif c == '+':
            continue
        else:
            val = val * 10 + string.digits.index(c)

    if neg:
        val = -val

    return val

    # This is a nifty functools solution, but I think it is harder to read.
    # return reduce(lambda x, c: x * 10 + string.digits.index(c), s[(s[0] == '-' or s[0] == '+'):], 0) * (-1 if s[0] == '-' else 1)
