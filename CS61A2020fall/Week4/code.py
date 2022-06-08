
def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)

def luhn_sum(n):
    all_but_last, last = split(n)
    if n < 10:
        return n
    else:
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    last_double = sum_digits(2 * last)
    if n < 10:
        return last_double
    else:
        return luhn_sum(all_but_last) + last_double