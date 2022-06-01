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
