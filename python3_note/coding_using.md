## some useful tools for using python

- input
	```python
	try :
		while True:
			input()
	except EOFError:
		pass
	```
- GCD
	```python
	def gcd(a,b)
	if (b==0):
		return a
	else :
		return gcd(b,a%b)
	```
