def count_words(arr):
    dict = {}
    count = 0
    for el in arr:
        for el2 in arr:
            if el == el2:
                count +=1
        dict[el] = count
        count = 0
    return dict


def unique_words_count(arr):
    return len(set(words))


def nan_expand(n):
    if n == 0:
        return ""
    else:
        return  "Not a "*n + "NaN"


def iterations_of_nan_expand(str):
    s = "NaN"
    n = len(str)
    count = 0
    while len(s) < n:
        s = "Not a " + s
        count +=1
    if str == s:
        return count
    else:
        return False


def prime_factorization(n):
    res = []
    step = 0
    while n != 1:
        for i in range(2, n+1):
            while n%i == 0:
                step +=1
                n /=i
            res.append((i,step))
            step = 0
    return res


def grouping(list1):
    return [x for ]


def group(smt):
    s = []
    res = []
    for i in smt:
        for i in smt
