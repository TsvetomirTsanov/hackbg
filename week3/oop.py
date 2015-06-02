

class Bill:
    def __init__(self, amount):
        self.total = amount

    def __int__(self):
        return self.total

    def __str__(self):
        return "A {}$ bill".format(self.total)

    def __eq__(self, other):
        return self.total == other.total

    def __hash__(self):
        return hash("A {}$ bill".format(str(self.total)))

    def __repr__(self):
        return self.__str__()

class BatchBill:

    def __init__(self, other):
        self.batch = other

    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        return self.batch[index]



class CashDesk:

    def __init__(self):
        self.amount = {}

    def __check1(thing):
        if type(thing) == type(Bill):
            return 1
        else:
            return 2

    def __take_money__(self, money):
        if __check1(__take_money__y) == 1:
            if money in self.amount:
                self.amount[money] +=1
            else:
                 self.amount[money] = 1
        else:
            for i in money:
                if i in self.amount:
                    self.amount[i] +=1
            else:
                self.amount[i] = 1

    def __total__(self):
        total = 0
        for i in self.amount:
            total += i

        return total

    def __inspect__(self):
        for key, value in self.money.items():
            print("{}$ bills - {}".format(key,value))



class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

