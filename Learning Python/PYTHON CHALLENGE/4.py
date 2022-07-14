# http://www.pythonchallenge.com/pc/def/linkedlist.php

string = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

import urllib.request
from urllib.parse import urljoin

def solve4(url):
    a = url
    for _ in range(400):
        b = urllib.request.urlopen(a)
        for line in b:
            nothing = line.decode("utf-8").split(' ')
        if nothing[-5:-1] == ['the', 'next', 'nothing', 'is']:
            a = urljoin('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing', 'linkedlist.php?nothing=' + nothing[-1])
            continue
        else:
            print(' '.join(nothing))
            return a.split('=')[-1]

print(solve4(string))

string2 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044'

def solve4pt2(value):
    a = int(nothing)
    b = a/2
    while True:
        print(b)
        url = urljoin('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing', 'linkedlist.php?nothing=' + str(b))
        c = urllib.request.urlopen(a).decode("utf-8").split(' ')
        if c[-5:-1] == ['the', 'next', 'nothing', 'is']:
            b = b/2
            continue
        else:
            print(' '.join(c))
            return b

print(solve4pt2(16044))