#!/usr/bin/env python

peter_dice = 4
colin_dice = 6

peter_rolls = 9
colin_rolls = 6

def memoize(fn):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            res = fn(*args)
            cache[args] = res
            return res
    return inner

@memoize
def colin(peter_values, colin_values):
    if len(colin_values) == colin_rolls:
        if sum(peter_values) > sum(colin_values):
            return 1
        else:
            return 0
    else:
        count = 0
        for i in range(1, colin_dice + 1):
            count += colin(peter_values, tuple(sorted(colin_values + (i,))))
        return count

@memoize
def peter(peter_values):
    if len(peter_values) == peter_rolls:
        return colin(peter_values, ())
    else:
        count = 0
        for i in range(1, peter_dice + 1):
            count += peter(tuple(sorted(peter_values + (i,))))
        return count

print "%.7f" % (peter(()) * 1.0 / (pow(4, 9) * pow(6, 6)))
