import sys


def task1(name):
    file = open(name, "r")
    contents = file.read().split("\n")
    for line in contents:
        print(line)

    file.close()


def task2(*names):
    for name in names:
        task1(name)


def task3(filename, number):
    file = open(filename, 'w')
    from random import randint
    contents = []

    for i in range(1, number):
        file.write(str(randint(1,1000)) + " ")
    file.close()
