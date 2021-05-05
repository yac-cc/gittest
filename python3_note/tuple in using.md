## Tuple
	+ tuple in editting
		```python
		>>>my_first_tuple=('element1','element2','element3')
		('element1','element2','element3')
		```
	+ valuation
		```python
		>>>a,b,c = my_first_tuple
		>>>a
		'element1'
		>>>b
		'element2'
		>>>c
		'element3'
		```
	+ transform list type
		```python
		>>>xlist = ['Gkd','Rip']
		>>>tuple(xlist)
		('Gkd','Rip')
		```
	to multified a tuple we can use '+' or "*' like a string
		## list 
		list is another type of group with struct of [ ] ,like a set
		```python
		listK=[23,23]
		#to build a list ,the value is abled repeated 
		list_empty =[]
		#U can also build an empty one.
		list_gg= [2000,{2001,2002,2003},2004]
		```
	+ list function
		```python
		>>> list () #an empty list
		[]
		>>> tupleB = ('abb','fbb','kbb')
		>>> list (tuple)
		('abb','fbb','kbb')
		>>> list ('cat')
		['c','a','t']
		```
		Hint : tuple is an unchangeable list with sequence
				list is changeable
## list in using : 
	there are some note with string to edit more view the file
	+ split 
	+ [offset]
	+ slice
	+ append
		append an new item into a list
		```python
		>>> caseAP = ['item_1',item_2']
		>>> caseAP.append ('item_N')
		>>> caseAP
		['item_1' , 'item_2' , 'item_N' ]
		```
	+ insert
		a function to append in any siuuation
		```python
		>>> listNo1=[12,16,20]
		>>> listNo1.insert(2,18)
		>>> listNo1
		[12, 16, 18, 20]
		## if the number more than the list_num ,it will be equal to append
		```
	+ extend
		combination with 2 different list
		```python
		>>> listNo2= [23,24]
		>>> listNo1.extend(listNo2)
		>>> listNo1
		[12, 16, 18, 20, 23, 24]
		>>> listNo1 += [25,26]
		>>> listNo1
		[12, 16, 18, 20, 23, 24, 25, 26]
		>>> listNo2.append(listNo2)
		>>> listNo2
		[23, 24, [...]]
		# by using append ,a list type will be rearded as an element
		```
	+ number revaluation
		```python
		# way of using slice
		>>> numbers =[1,2,3,4]
		>>> numbers[1:3] =[8,9]
		>>> numbers
		[1,8,9,4]
		>>> numbers[1:2]= 'cat'
		[1,'c','a','t',9,4]
		# ummm... Python is smart
		```
	+ del listEx[offset]
	+ remove ('I don't know what you wanna remove')
	+ pop
		```python 
		#as Python is smart , you are able to pop any element
		>>> ok[23,43,54,56,87]
		>>>ok.pop()
		>>> ok=[23,34,45,56,67]
		>>> ok.pop()
		67
		>>> ok
		[23, 34, 45, 56]
		>>> ok.pop(1)
		34
		>>> ok.pop(0)
		23
		>>> ok
		[45, 56]
		# pop() without an int equal to pop (-1)
		#FIFO (first in first out)
		## by using pop() and append()
		```
	+ clear()
		turn list into empty
	+ index()
		find the offset sit
		```python
		>>>Alist=[1,1,2,3,5,8,13,21,34,55,89]
		>>> Alist.index(89)
		10
		>>> Alist.index(1)
		0

		#it will only return first situation

		#while offset tis not defined the program will be unexpected stop
		```
	+ in
		check a value exist.
		```python
		>>> 8 in Alist
		True
		>>> 12 in Alist
		False
		```
	+ count
		count times a value appear
		```python
		>>> Alist.count(1)
		2
		```
	+ join 
		inverse function of split
		```python 
		>>> item="a sentance that u should never read"
		>>> type(item)
		<class 'str'>
		>>> k=item.split(' ')
		>>> k
		['a', 'sentance', 'that', 'u', 'should', 'never', 'read']
		>>> item2=' '.join(k)
		>>> item2
		'a sentance that u should never read'
		>>> item == item2
		True
		```
	+ sort() and sorted()
		Sort numbers :
			in ascending order
		Sort string :
			in dictionary order
		the differences between two function is:
			sort()   : directly change the order
			sorted() : a function , return a sorted list
		```python
		>>> list_a=[4343,3454,6543,4656,3442,65678,64653,34]
		>>> sorted(list_a)
		[34, 3442, 3454, 4343, 4656, 6543, 64653, 65678]
		
		>>> list_a
		[4343, 3454, 6543, 4656, 3442, 65678, 64653, 34]
		
		# sorted won't change the var
		
		>>> list_a.sort()
		>>> list_a
		
		[34, 3442, 3454, 4343, 4656, 6543, 64653, 65678]
		
		```
	+ len() 
		
		return list length
		```python
		len  ( list )
		```
	+ valuable list
		consider the condition:
		```python
		>>> a = [1,2,3]
		>>> b = a
		>>> b[0] = 'surprice'
		>>> a
		['surprice', 2, 3]
		```
		the reason cause the situation happenend cuz the '=' gave a and b the same reference . to solve the problem we can use copy() , list ,or slice
	+ copy()
		to solve the problem using("=")
		```python
		>>> a = [1,2,3]
		>>> b = a.copy()
		>>> c = list[a]
		>>> d = a[:]
		### survival ?
		>>> a.pop()
		3
		>>> b
		[1,2,3]
		>>> c
		[1,2,3]
		>>> d
		[1,2,3]
		```
	+ deepcopy    (import copy )
		while the list incuded another reference use deepcopy to completel copy the stuff individualy
		```python
		>>> a=[1,2,[8,9]]
		>>> b=a.copy()
		>>> b
		[1, 2, [8, 9]]
		>>> a[2][1]='Hi'
		>>> b
		[1, 2, [8, 'Hi']]
		>>> import copy      ## remember
		>>> c= copy.deepcopy(a)
		>>> b[2][1]="FAQ"
		>>> b
		[1, 2, [8, 'FAQ']]
		>>> c
		[1, 2, [8, 'Hi']]
		```
	+ for in loop zip
		Basic using:
		```python
		for i in list_k:
			print (i)
		```
		multi execute
		```python
		for a,b,c,d in zip(list_a,list_b,list_c,list_d):
			print (a,b,c,d)
		## runtime follow the first end
		```
	+ tip
		tuple is smaller than list
