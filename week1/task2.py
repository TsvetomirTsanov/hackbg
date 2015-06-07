def sum_of_divisors(n):
    a = 1
    sum = 0
    while a <= n:
        if n%a == 0:
            sum += a
        a+=1
    return sum

def is_prime(n):
    a = 1
    count = 0
    if n == 1:
        return False
    else:
        while a <= n:
            if n%a == 0:
                count +=1
            a +=1

    return count == 2

def prime_number_of_divisors(n):
    divisors = [n%x == 0 for x in range(1,n+1)]
    return is_prime(divisors.count(True))

def is_zero(a,b):
    return a == b or (a+b)%10 == 0

def zero_list(n):
    digits = to_digits(n)
    length = len(digits)
    start = 0
    result = []
    while start != length -1:
        result.append(digits[start])
        if is_zero(digits[start],digits[start+1]):
            result.append(0)
        start +=1
    result.append(digits[start])

    return result


def sum_matrix(matr):
    return sum([sum(row) for row in matr])


def fibonacci(n):
    result = []

    a = 1
    b = 1

    while len(result) < n:
        result.append(a)

        next_fib = a+b
        a = b
        b = next_rib

    return result

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


#def grouping(list1):
 #   return [x for ]

def sum_of_digits(n):
    return sum(to_digits(n))

def to_digits(n):
    return [int(x) for x in str(n)]

def factorial_digits(n):
    return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):
    return str(obj)[::-1] == str(obj)

def count_digits(n):
    sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result*(10**digits_count) + digit

    return result

def fibonacci_number(n):
    return to_number(fibonacci(n))

def count_vowels(string):
    vowels = "sdadSDADdgher"
    count = 0
    for ch in string:
        if ch in vowels:
            count+=1
    return count

def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] +=1
        else:
            result[ch] = 1
    return result

def p_score(n):
    if(palindrome(n)):
        return 1

    s = n + int(str(n)[::-1])

    return 1 + p_score(s)

def is_even(n):
    return n%2 == 0

def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n +=1
    while not is_hack(n):
        n+=1

    return n



def contains_digit(number, digit):
    return str(digit) in str(number)

def contains_digits(number, digits):
    for n in digits:
        if n not in to_digits(number):
            return False

    return True

def is_number_balanced(n):
    a = to_digits(n)
    sum1 = 0
    sum2 = 0
    if(is_even(n)):
        for num in a:
            if num < len(n)/2:
                sum1 += num
            else:
                sum2 += num


def count_substrings(haystack, needle):
    count = 0
    for ch in len(haystack):
        if needle in haystack[ch:]:
            count += 1
    return count
