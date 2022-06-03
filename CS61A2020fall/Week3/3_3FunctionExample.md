# Function Example
## Describing Functions
了解函数的三个步骤：1.阅读源码；2.阅读描述信息；3.举例
```python
def like(n):
	"""Returns whether George Boole likes the non-negative integer n."""
	...

def mystery1(n):
	k = 1
	while k < n:
		if like(i):
			print(k)
		k = k + 2
```
这个函数将会打印所有的n以下的奇数如果george喜欢n
```python
def likes(n):
	#同上

def mystery2(n):
	i, j, k = 0, None, None
	while i < n:
		if likes(i):
			if j != None and (k == None or i - j < k):
				k = i - k
			j = i
		i = i + 1
	return k
```
这个函数则是返回george喜欢的n以内两个正整数之间的最小距离，但是如果喜欢的正整数小于2个（不存在这样一个距离）则返回`None`
## Generating Environment Diagram
通过右图的环境图补充下述代码![[Pasted image 20220601225517.png]]
首先可以观察到，有两个函数`flip()`和`flop()`但是在图谱中，他们分别指向了名字相反的函数，说明正好两者的函数名发生了调换，因此倒数第二行应为`flip, flop = flop, flip`，随后在图谱中调用了`flip()`函数，对应全局函数中应该是`flop()`函数名，而`flip(___)(3)`中空格前的函数名为`flip()`，因此`flop()`函数名只能在括号中被调用，它对应着`flip()`函数，观察其参数flop为1，因此暂时认为最后一行代码中括号为`flop(1)`，继续观察，flip被赋值为一个lambda函数，因此第三个空格应为`lambda flip: ***`（返回值暂空），随后又发现这个lambda函数也被调用了，而且含有参数flip为2，而这正是`flip()`函数返回的函数，它被再次调用了，返回值为3，于是姑且补充第三个空格为`lambda flip: 3`，最后一空为`flop(1)(2)`，其结果为3。即最后一行代码等同于`flip(3)(3)`，`flip(3)`调用`flop()`函数，返回值为flop，对应`flip()`函数，最终即要计算`flip(3)`，其返回值为`None`，因此可以从前两个横线入手，由前面已知，当`flip()`函数的参数flop为1时，返回值不为`None`，但是为3时则是，因此可以写为`if flop == 3: return None`或者`if flop > 2: return None`之类的，综上，所有结果如下图：
![[Pasted image 20220601231717.png]]
## Implementing Functions
```python
def remove(n, digit): 
	"""Return all digits of non-negative N 
	that are not DIGIT, for some 
	non-negative DIGIT less than 10. 
    >>> remove(231, 3) 
	21 
    >>> remove(243132, 2) 
	4313 
	""" 
	kept, digits = 0, 0
	while ________________________________: 
		 n, last = n // 10, n % 10 
		 if _______________________________: 
			 kept = _______________________ 
			 digits = _____________________ 
	return _______________________________

def remove(n, digit):
    """Return all digits of non-negative N
    that are not DIGIT, for some
    non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if digit != last:
            kept = last * pow(10, digits) + kept
            digits = digits + 1
    return kept
```
## Q&A
```python
def repeat(k):
    """When called repeatedly, print each repeated argument

    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return _____(k)

def detector(f):
    def g(i):
        if ___:
            ____
        return ___
    return g


def repeat(k):
    """When called repeatedly, print each repeated argument

    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda j: j == i or f(j))
    return g
```
首先，`repeat()`是一个柯里化的函数，它应该是一个可以不停接受新的参数的函数，因此它的返回值必定是一个有参数的函数`_____(k)`，这个地方应该就是`detector()`函数了，继续观察`detector()`函数，它含有一个函数参数f，之后接受一个数值参数i，此i应该是要比值的各个数字，因为`repeat()`要打印之前见过的数值，因此if后一句应该是`print(i)`，而if后接的应该是判断i是否重复出现过的，这里的`f`函数可以作为判断是否重复出现过的函数，return后面应该是一个有参数的函数而且不停的执行与`detector()`相同的功能，继续接受后面的数字，这个数字与前面的所有数字进行比较，首先与其相邻的上一个数字相比，然后利用递归的思想（有点形而上学）与前面的数字比较，直到前面没有数字比较了，就返回`False`