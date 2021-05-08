## string

* conbined

  ```python
  >>> ('aa'+'bb')*3
  'aabbaabbaabb'
  >>> letters = 'asdfghjkl'
  >>> letters[-1]
  'l'
  #  -size<k<size
  ```
* length

  ```python
  >>> len(letters)
  9
  ```

* slice

  ```python
  '''
  [:] all string
  [ start : ] 
  [ : end ] 
  [start : end]
  [stert : end : step]
  '''
  >>> letters [8 :]
  'l'
  >>> letters[:3]
  'asd'
  >>> letters[2:-2]
  'dfghj'
  >>> letters[2:-2:3]
  'dh'
  >>> 
  ```


* strip

  ```python
  >>> str1 = "      eeeb   "
  >>> str1.strip(" ")
  'eeeb'
  >>> str1.lstrip(" ")
  'eeeb   '
  >>> str1.rstrip(" ")
  '      eeeb'
  
  ```

* split

  ```python
  >>> str2="a dog,a cat,an apple"
  
  >>> str2.split(",")
  ['a dog', 'a cat', 'an apple']
  
  >>> str2.split()   # spzce and "\n" ...
  ['a', 'dog,a', 'cat,an', 'apple']
  ```

* join

  ```python
  >>> ', '.join(str2.split())
  'a, dog,a, cat,an, apple'
  	#string.join(array)
  ```

* replace

  ```python
  >>> str2.replace("a ","a famous",1)
  'a famousdog,a cat,an apple'
  >>> str2.replace("a","a famous")
  'a famous dog,a famous ca famoust,a famousn a famouspple'
  	#count omitted
  ```

* find

  ```python
  >>> str3
  'a bb cc dd sds\nds\n fd fds\n fd\n dsds '
  >>> str3.find('\n')      #\n 第一次出現位置
  14
  >>> str3.index('\n')
  14
  >>> str3.rfind('\n')     #倒著數
  29
  >>> str3.rindex('\n')
  29
  >>> str3.count('\n')
  4
  >>> str3.find('z')      #find 回傳-1
  -1                      #index抱錯
  >>> str3.index('z')
  Traceback (most recent call last):
    File "<pyshell#84>", line 1, in <module>
      str3.index('z')
  ValueError: substring not found
  >>> 
  ```

  

