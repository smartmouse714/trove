#!/usr/bin/env python
"""Calendar display functions

Circumvent ungainly format issues of ActivePython on Cygwin."""

import argparse
import calendar
import datetime

def pr1j(i, j, k):
    """Print a monthly Julian calendar."""
    (v_0, v_1), v_2, v_3 = j, ' ' * 3, k.tm_yday
    if 6 == i and v_0 < 6:
        v_4 = [v_2] * (v_0 + 1)
    elif 0 == i and 0 < v_0:
        v_4 = [v_2] * v_0
    else:
        v_4 = []
    v_4 += [str(i + v_3).rjust(3) for i in range(v_1)]
    v_0, v_1 = len(v_4) % 7, []
    if 0 < v_0:
        v_4 += [v_2] * (7 - v_0)
    for v_0 in range(0, len(v_4), 7):
        v_1.append(' '.join(v_4[v_0 : v_0 + 7]))
    return v_1

def pr3m(i, j, k):
    """Print three months in a row."""
    lst3 = [i, j, k]
    len3 = [len(lst1) for lst1 in lst3]
    max3 = max(len3)
    for (len1, lst1) in zip(len3, lst3):
        if max3 > len1:
            lst1.append('')
    for row in range(max3):
        print(''.center(6).join([lst1[row].ljust(20) for lst1 in lst3]))

def main(opt):
    """Print a calendar."""
    c = calendar.TextCalendar(calendar.MONDAY if opt.m else calendar.SUNDAY)
    formatyear = lambda y: '\n'.join(c.formatyear(y).split('\n')[0:-1])
    f = lambda y, m: c.formatmonth(y, m).split('\n')[0:-1]

    if opt.iy is None:
        print(formatyear(opt.yr))
    elif 0 < opt.iy:
        print(formatyear(opt.iy))
    elif opt.i3:
        i, j = datetime.date(opt.yr, opt.mo, 1), datetime.timedelta(days=1)
        prv = i - j
        nxt = i.replace(day=calendar.monthrange(opt.yr, opt.mo)[1]) + j
        i = f(prv.year, prv.month)
        j = f(opt.yr, opt.mo)
        k = f(nxt.year, nxt.month)
        pr3m(i, j, k)
    elif opt.j:
        print('\n'.join(c.formatmonth(opt.yr, opt.mo, 3).split('\n')[:2] +
                        pr1j(c.firstweekday,
                             calendar.monthrange(opt.yr, opt.mo),
                             datetime.date(opt.yr, opt.mo, 1).timetuple())))
    elif opt.i1:
        print('\n'.join(f(opt.yr, opt.mo)))

if __name__ == '__main__':
    FOO = datetime.date.today()
    # Ultimate goal
    #   usage: cal.py [-smjy13] [[month] year]
    # Attained insofar
    #   usage: cal.py [-h] [-s | -m] [-y [year]] [-1 | -3 | -j] [month] [year]
    BAR = argparse.ArgumentParser(description='A cal emulator')
    BAZ = BAR.add_mutually_exclusive_group()
    BAZ.add_argument('-s',
                     help='Display Sunday as the first day of the week.',
                     action='store_true', default=True)
    BAZ.add_argument('-m',
                     help='Display Monday as the first day of the week.',
                     action='store_true', default=False)
    BAR.add_argument('-y', metavar='year', type=int,
                     help='Display a yearly calendar.',
                     choices=range(datetime.MINYEAR, datetime.MAXYEAR),
                     dest='iy', nargs='?', default=0)
    BAZ = BAR.add_mutually_exclusive_group()
    BAZ.add_argument('-1', dest='i1',
                     help='Display single month output.',
                     action='store_true', default=True)
    BAZ.add_argument('-3', dest='i3',
                     help='Display prev/current/next month output.',
                     action='store_true', default=False)
    BAZ.add_argument('-j',
                     help='Display Julian dates for a month.',
                     action='store_true', default=False)
    BAR.add_argument(metavar='month', type=int,
                     choices=range(1, 13),
                     dest='mo', nargs='?', default=FOO.month)
    BAR.add_argument(metavar='year', type=int,
                     choices=range(datetime.MINYEAR, datetime.MAXYEAR),
                     dest='yr', nargs='?', default=FOO.year)

    main(BAR.parse_args())
