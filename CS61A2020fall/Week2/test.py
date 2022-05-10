# while n > 1:
#     k = 2
#     while n % k != 0:
#         k += 1
#     n = n // k
#     print(k)

# def fib(n):
#     """Compute the nth Fibonacci number, for N >= 1."""
#     pred, curr = 0, 1 # 0th and 1st Fibonacci numbers
#     k = 1 # curr is the kth Fibonacci number
#     while k < n: 
#         pred, curr = curr, pred + curr
#         k = k + 1
#     return curr

# """Generalization"""
# from math import pi, sqrt

# def area_square(r):
#     assert r > 0, "a length must be positive"
#     return r * r

# def area_circle(r):
#     return r * r * pi

# def area_hexagon(r):
#     return r * r * sqrt(3) * 3 / 2


# """Generalization"""
# from math import pi, sqrt

# def area(r, shape_constant):
#     assert r > 0, "a length must be positive"
#     return r * r * shape_constant

# def area_square(r):
#     return area(r, 1)

# def area_circle(r):
#     return area(r, pi)

# def area_hexagon(r):
#     return area(r, sqrt(3) * 3 / 2)

# """Generalization"""
# def cube(k):
#     return pow(k, 3)

# def identity(k):
#     return k

# def third(k):
#     return 8 / ((4 * k - 3) * (4 * k - 1))

# def summation(n, term):
#     """sum of the first n terms of a sequence
#     >>> summation(5, cube)
#     225
#     >>> summation(5, identity)
#     15
#     >>> summation(5, third)
#     3.041839618929402
#     """
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + term(k), k + 1
#     return total

# def sum_naturals(n):
#     return summation(n, identity)

# def sum_cube(n):
#     return summation(n, cube)

# def sum_third(n):
#     return summation(n, third)

# square = lambda x: x * x

# def search(f):
#     """search the number until satisfied"""
#     x = 0
#     while not f(x):
#         x += 1
#     return x

# def is_three(x):
#     return x == 3

# def positive(x):
#     return max(0, square(x) - 100) 

# def reverse(f):
#     """反函数"""
#     return lambda y: search(lambda x: f(x)==y)


# """guess out the golden ratio"""
# from tkinter import Y


# def improve(update, close, guess = 1):
#     """update the guess untill satisfied"""
#     while not close(guess):
#         guess = update(guess)
#     return guess

# def golden_update(guess):
#     """update"""
#     return 1/guess + 1

# def square_close_to_successor(guess):
#     """make use of a property of the golden ratio"""
#     return approx_eq(guess * guess, guess + 1)

# def approx_eq(a, b, tolenrance = 1e-15):
#     return abs(a - b) < tolenrance

# # if __name__ == "__main__":
# #     print(improve(golden_update, square_close_to_successor))

# def newton_update(f, df):
#     def update(x):
#         return x - f(x) / df(x)
#     return update

# def find_zero(f, df):
#     def near_zero(x):
#         return approx_eq(f(x), 0)
#     return improve(newton_update(f, df), near_zero)

# def square_root_newton(a):
#     def f(x):
#         return x * x - a
#     def df(x):
#         return 2 * x
#     return find_zero(f, df)

# def power(x, n):
#     result, times = 1, 1
#     while times <= n:
#         result, times = result * x, times + 1
#     return result

# def nth_root_of_a(a, n):
#     def f(x):
#         return power(x,n) - a
#     def df(x):
#         return n * power(x, n - 1)
#     return find_zero(f, df)

# def adder(x):
#     def make_adder(y):
#         return x + y
#     return make_adder

# add(x + y)

# from ucb import trace
# def trace(f):
#     def traced(x):
#         print(f, " takes in the arguement ", x,  
#         ", and the result is: ", f(x))
#     return traced

# @trace
# def square(x):
#     return x * x

# square = trace(square)

def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x