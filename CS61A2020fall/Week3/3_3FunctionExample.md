# Describing Functions
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