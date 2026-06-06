from decimal import Decimal, ROUND_HALF_UP


def round_money(x):
    return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
