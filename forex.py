#!/usr/bin/env python

# 1. standard library imports, compatible with Python 2 & 3
from __future__ import print_function
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
# 2. related third party imports
from bs4 import BeautifulSoup, SoupStrainer
from colorama import Fore, Back, Style

basket = ('AED', 'AUD', 'CAD', 'GBP', 'HKD', 'JPY', 'USD')

def report_rates():
    """Quote delayed exchange rates."""
    data, url = {}, 'https://www.boc.cn/sourcedb/whpj/enindex_1619.html'
    try:
        html = urlopen(url).read()
        table = SoupStrainer('table', bgcolor='#EAEAEA')
        soup = BeautifulSoup(html, 'html.parser', parse_only=table)
        for tr in soup.findAll('tr')[1:]: # Skip the header.
            td = [i.get_text() for i in tr.findAll('td')]
            if td[0] in basket:
                data[td[0]] = td[1:-1]
    except Exception as e:
        print(e)
    return data

if __name__ == '__main__':
    indices = report_rates()
    toggle = True
    for i in indices.keys():
        if toggle:
            print(Style.BRIGHT, end="")
        else:
            print(Style.DIM, end="")
        print(i + " " + indices[i][2] + Style.RESET_ALL)
        toggle = not toggle
