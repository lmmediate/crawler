#coding=utf-8

import re
def remove_junk(s):
    s = s.strip()
    # Dixy's wrong non-breaking space.
    #
    s = re.sub(r'(&nbsp;?)+', ' ', s)
    # s = re.sub(r'&.+;', '', s)
    s = re.sub(r'\*+', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s


def try_float(val):
    res = []
    try:
        res = float(val)
    except ValueError:
        return val
    return res
 

def concat(left, right, sep):
    return try_float(remove_junk(left) + sep + remove_junk(right))


def process(val):
    return try_float(remove_junk(val))


# EOF

