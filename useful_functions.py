def find_max(values):
    """ It returns the biggest value of a list"""
    best = values[0]
    for a in values:
        if a > best:
            best = a
    return best

def count_occurrences(items,target):
    """It returns how many times the target is in items"""
    n = 0
    for x in items:
        if x == target:
            n += 1
    return n

def filter_by_value(d,minimum):
    """ Returns the pairs with value >= minimum"""

    return {k:v for k, v in d.items()
            if v >= minimum}

print(find_max([45,89,100,265]))
print(count_occurrences(["b","a","c","c","e"],"c"))
print(filter_by_value({"Ben": 12,"Hari":8},10))
