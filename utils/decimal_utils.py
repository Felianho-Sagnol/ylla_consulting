from decimal import Decimal 

TWOPLACES = Decimal(10) ** -2


def multiplier(x, y, fp=TWOPLACES):
    return (x * y).quantize(fp)


def diviser(x, y, fp=TWOPLACES):
    return (x / y).quantize(fp)