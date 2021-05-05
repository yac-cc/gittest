## arithmetic operator
* underline and common
  ```python
  >>> 1__2__3
  123 # underline omitted
  
  >>> 1,000,000
  (1, 0, 0)  # common for number string
  ```
* devision
  ```python
  >>> 9/5
  1.8
  >>> 9//5
  1
  ```
* divmod
  ```python
  def divmod (a,b)
    return ( a//b , a % b )
  >>> divmod (567 , 7 )
  (81, 0)
  ```
* power
  ```python
  '''
  define b to the nth power b**n
  '''
  >>>2**3
  8
  >>> 2**6.3
  78.79324245407463
  ```