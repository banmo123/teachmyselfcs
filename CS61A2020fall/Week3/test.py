# def remove(n, digit):
#     """Return all digits of non-negative N
#     that are not DIGIT, for some
#     non-negative DIGIT less than 10.
#     >>> remove(231, 3)
#     21
#     >>> remove(243132, 2)
#     4313
#     """
#     kept, digits = 0, 0
#     while n > 0:
#         n, last = n // 10, n % 10
#         if digit != last:
#             kept = last * pow(10, digits) + kept
#             digits = digits + 1
#     return kept


# def repeat(k):
#     """When called repeatedly, print each repeated argument

#     >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
#     7
#     1
#     5
#     1
#     """
#     return detector(lambda j: False)(k)

# def detector(f):
#     def g(i):
#         if f(i):
#             print(i)
#         return detector(lambda j: j == i or f(j))
#     return g

# def mint(y):
#     return print(-2)
##print(mint(print)) #-2&None

def snooze(e, f):
    if e and f():
        print(e)
    if e or f():
        print(f)
    if not e:
        print('naughty')

def lose():
    return -1

#print(snooze(1, lose)) #1&Func&None

def alarm():
    print('Midterm')
    1 / 0
    print('Time')
#snooze(print(1), alarm) #1&Midterm$Error

def sim(b, a):
    while a > 1:
        def sc(ar):
            a = b + 4
            return b
        a, b = a // 2, b - 2
        print(a)
    print(sc(b - 1), a)
#sim(3, 3) #1&1 1

pumbaa = lambda f: lambda x: f(f(x))
pumbaa = pumbaa(pumbaa)
rafiki = 1
timon = lambda y: y + rafiki
rafiki = -1
#pumbaa(timon)(5) #    

