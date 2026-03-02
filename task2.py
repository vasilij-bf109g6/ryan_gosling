def rectangle_area(a, b=None):
    if a <= 0 or (b is not None and b <= 0):
        return 0

    if b is None:
        return a * a
    else:
        return a * b