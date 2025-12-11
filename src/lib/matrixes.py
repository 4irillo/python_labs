def transpose(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    if len(a) == 0:
        return []
    if len(a) != 0:
        l = len(a[0])
    for i in a:
        if len(i) != l:
            raise TypeError("ValueError")

    # actual code
    ans = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(a[j][i])
        ans.append(temp)
        temp = []
    return ans


def row_sums(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    if len(a) == 0:
        return []
    l = len(a[0])
    for i in a:
        if len(i) != l:
            raise TypeError("ValueError")

    # actual code
    ans = []
    for i in a:
        sum = 0
        for j in i:
            sum += j
        ans.append(sum)
    return ans


def col_sums(a):
    # exceptions
    if not isinstance(a, list):
        raise TypeError("TypeError")
    if len(a) == 0:
        return []
    l = len(a[0])
    for i in a:
        if len(i) != l:
            raise TypeError("ValueError")

    # actual code
    ans = []
    for m in range(len(a[0])):
        temp = 0
        for n in range(len(a)):
            temp += a[n][m]
        ans.append(temp)
    return ans
