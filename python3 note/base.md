## base

* base N 

  ```python
  '''
  	rule
  		binary  : 0b or 0B
  		base 8  : 0o or 0O
  		base 16 : 0x or 0X
  '''
  >>> 0b10
  2
  >>> 0o10
  8
  >>> 0x19
  25
  >>> value = 65
  >>> bin (value)
  '0b1000001'
  >>> oct (value)
  '0o101'
  >>> hex (value)		
  '0x41'
  >>> chr (value)		#int to string 
  'A'
  >>> ord ('A')			#string of lengh 1 to int
  65
  ```
  
  