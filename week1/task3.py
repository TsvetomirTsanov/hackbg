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
    return sum([1 for key in count_words(arr)])


def nan_expand(n):
    if n == 0:
        return ""
    else:
        return  "Not a "*n + "NaN"


def iterations_of_nan_expand(str):
    s = "NaN"
    n = len(str)
    count = 0
    if n == 0:
        return 0
    else:
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
            if n%i == 0:
                while n%i == 0:
                    step +=1
                    n /= i
                res.append((i,step))
            step = 0
    return res



def group(smt):
    s = []
    res = []
    length = len(smt)
    i = 0
    while i != length-1:
        if smt[i] == smt[i+1]:
            while smt[i] == smt[i+1]:
                    s.append(smt[i])
                    i+=1
                    if i == length-1:
                        break
                        s.append(smt[i])
            s.append(smt[i])
        else:
            s.append(smt[i])
            i+=1
        res.append(s)
        s = []

    if smt[-2] != smt[-1]:
        res.append([smt[-1]])

    return res

def max_consecutive(smt):
    s = []
    res = 0
    length = len(smt)
    i = 0
    while i != length-1:
        if smt[i] == smt[i+1]:
            while smt[i] == smt[i+1]:
                    s.append(smt[i])
                    i+=1
                    if i == length-1:
                        break
                        s.append(smt[i])
            s.append(smt[i])
        else:
            s.append(smt[i])
            i+=1

        if len(s) > res:
            res = len(s)
        s = []

    return res

def groupby(func, seq):
    result = {}
    for item in seq:
        result[func(item)] = [item]
    return result

def prepare_meal(number):
    res = ""
    count = -1
    while number%3 == 0:
        number = number//3
        count +=1
        if count != 0:
            res += " "
        res += "spam"

    if number % 5 == 0:
        if res != '':
            res +=" and "
        res += "eggs"

    return res

def reduce_file_path(path):
    result = []
    parts = [part for part in path.split("/") if part not in [".", ""]]

    while len(parts) != 0:
        part = parts.pop()

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            result.insert(0, part)

    return "/" + "/".join(result)

def is_an_bn(word):
    length = len(word)
    count1 = 0
    check1 = True
    count2 = 0
    check2 = True
    if word == "":
        return True
    if word[0] != 'a':
        return False

    for ch in word:
        if ch == 'a':
            if check1 == True:
                count1 += 1
        else:
            check1 = False

        if check1 == False:
            if ch == 'b':
                if check2 == True:
                    count2 +=1
            else:
                check2 = False

    return count1 == count2 and count1*2 == length

def count_digits(n):
    return sum([1 for x in to_digits(n)])


def is_credit_card_valid(number):
    s = 0
    numbs = to_digits(number)

    if count_digits(number) % 2 != 0:
        for i in range(len(str(number))):
            if i % 2 == 0:
                s += numbs[i]
            else:
                s += sum(to_digits(numbs[i] * 2))

        return s % 10 == 0

    return False





