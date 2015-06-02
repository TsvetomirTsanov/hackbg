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
    a = str(obj)
    return a == reversed(a)


def to_digit(n):
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

def now():
    sum1 = 0
    n = 10
    s = [1,2,3,4,5,6]
    for k in s:
        sum1 += (pow(4, n-2*k)*factorial(n))/(pow(6, n)*factorial(k)*(factorial(n-2*k)))

    print(sum1)

#def p_score(n):
 #   count = 0
  #  if palindrome(n):
   #     return 1
   # else:
#        while not palindrome(n):
 ##          n = 1 + n + int(s)
   #         count +=1
#
 #   return count
#
#print(p_score(121))
