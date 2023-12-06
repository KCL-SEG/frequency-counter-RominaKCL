"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for i in items:
        keys = frequencies.keys()
        item = str(i)
        if item in keys:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies
