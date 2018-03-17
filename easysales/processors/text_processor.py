# coding=utf-8

import re
from time import gmtime, strftime


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


def split_by(val, delim):
    return val.split(delim)


def make_date(raw):
    year = strftime('%Y', gmtime())
    month = raw.split('/')[1]
    day = raw.split('/')[0]

    return '{Y}-{m}-{d}'.format(Y=year, m=month, d=day)


def parse_date_in(s):
    raw = re.findall(r'\d{2}/\d{2}', s)
    return make_date(raw[0])


def parse_date_out(s):
    raw = re.findall(r'\d{2}/\d{2}', s)
    if len(raw) > 1:
        return make_date(raw[1])
    else:
        return make_date(raw[0])


# EOF

