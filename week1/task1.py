def factorial(n):
    sum = 1

    for i in range(1, n + 1):
        sum*=i

    return sum


def fibonacci(n):
    a = 1
    b = 1
    fib = []
    while len(fib) < n:
        fib.append(a)
        next_fib = a+b
        a = b
        b = next_fib

    return fib


def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = n//10

    return sum

def fact_digits(n):
    sum = 0
    while n != 0:
        a = n%10
        sum += factorial(a)
        n = n//10
    return sum

def palindrome(obj):
    return str(obj)[::-1] == str(obj)


def to_digits(n):
    digits = []
    while n!= 0:
        s = n%10
        digits.append(s)
        n = n//10

    return digits


def to_number(n):
    number = 0
    for i in n:
        number = number*10 + i
    return number

def fib_number(n):
    size = len(fibonacci(n))
    print("Size is {}".format(size))
    d = pow(10, size-1)
    result = 0
    for number in fibonacci(n):
        result += number*d
        d /= 10
    return result

def count_vowels(word):
    vowels = "aeiouy"
    count = 0
    for vowel in vowels:
        for letter in word:
            if vowel == letter:
                count +=1
    return count


def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for consonant in consonants:
        for letter in word:
            if consonant == letter:
                count +=1
    return count


def char_histogram(word):
    histogram = {}
    for ch in word:
        if ch in result:
            histogram[ch] +=1
        else:
            histogram[ch] = 1
    return histogram


def p_score(n):
    if palindrome(n):
        return 1

    number = n + int(str(n)[::-1])
    return 1 + p_score(number)

def is_increasing(seq):
    size = len(seq)
    flag = True
    for n in range(1,size):
        if seq[n] <= seq[n-1]:
            flag = False
    return flag

def is_decreasing(seq):
    size = len(seq)
    flag = True
    for n in range(1,size):
        if seq[n] >= seq[n-1]:
            flag = False
    return flag

def is_odd(n):
    return n%2 != 0

def is_hack(n):
    bin_n = bin(n)[2:]
    return palindrome(bin_n) and is_odd(bin_n.count("1"))


def next_hack(n):
    n+=1
    while not is_hack(n):
        n+=1
    return n

