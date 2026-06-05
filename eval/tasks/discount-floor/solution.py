def discount_price(price, pct):
    """Return price after applying a pct% discount.

    Quick check: discount_price(100, 10) == 90.
    """
    return price * (100 - pct) // 100
