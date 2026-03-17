# Autore: Shahid
# Refactoring TOTALE: tutti

from Sign.addInfinite import addInfinite
from Sign.test import test
from Sign.analizer import analizer

def createSign(f, x):

    intervals = analizer(f, x)

    intervals = [i for i in set(intervals) if intervals.count(i) >= 1]
    intervals = sorted(intervals)

    addInfinite(intervals)

    print("Final intervals:")
    print(intervals)

    signs = test(intervals, f, x)
    print("Signs: ")
    print(signs)

    return intervals, signs