def min(a, b):
    # exceptions
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("ParamError")
    # code
    return a if a < b else b


def max(a, b):
    # exceptions
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("ParamError")
    # code
    return a if a > b else b


def min_max(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    if len(a) == 0:
        raise ValueError("ValueError")
    # code
    mn, mx = 1e7, -1e7
    for i in a:
        mn = min(i, mn)
        mx = max(i, mx)
    return [mn, mx]


def unique_sorted(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    # code
    a = set(a)
    a = list(a)
    a.sort()
    return a


def flatten(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    # code
    b = []
    for i in a:
        if not isinstance(i, (list, set)):
            raise TypeError("TypeError")
        for j in i:
            b.append(j)
    return b
