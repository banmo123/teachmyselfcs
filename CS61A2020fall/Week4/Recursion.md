# Recursion
## Recursive Functions
定义：一个函数直接或间接的调用函数自己的函数叫递归函数
含义：执行递归函数又会要求应用这个函数
### Sum digits without a while statement
```python
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
```
递归函数需要有一个基础事件，一般都是最简单的示例，可以直接算出结果的，其它条件则是要通过重复调用递归函数![[Pasted image 20220608124832.png]]
### Recursion in Environment Diagrams
```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

fact(3)
```
![[Pasted image 20220608130419.png]]![[Pasted image 20220608130444.png]]
### Verifying Recursive Functions
![[Pasted image 20220608130811.png]]
### Mutual Recursion
![[Pasted image 20220608132254.png]]
```python
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
```
### Converting Recursion to Iteration & Converting Iteration to Recursion
![[Pasted image 20220608133342.png]]![[Pasted image 20220608133353.png]]
-