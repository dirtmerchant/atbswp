#lists
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
'cat'
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0][1]
'bat'
spam[1][4]
50
spam = ['cat', 'bat', 'rat', 'elephant']
'The ' + spam[-1] + ' is afraid of the ' + spam[-3]
'The elephant is afraid of the bat'

spam = 'Hello'
spam = [10, 20, 30]
spam[1]
20
spam[1] = 'Hello'
spam
[10, 'Hello', 30]

#slice
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
spam
[10, 'CAT', 'DOG', 'MOUSE']

spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
['cat', 'bat']
spam[1:]
['bat', 'rat', 'elephant']

del spam[2]
spam
['cat', 'bat', 'elephant']
del spam[2]
spam
['cat', 'bat']

len('Hello')
5
len([1,2,3])
3

#in/notin
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
42 in ['hello', 'hi', 'howdy', 'heyas']
False
42 not in ['hello', 'hi', 'howdy', 'heyas']
True

>>> for i in range(4):
...     print(i)
...
0
1
2
3

>>> for i in [0, 1, 2, 3]:
...     print(i)
...
0
1
2
3

>>> list(range(4))
[0, 1, 2, 3]
>> list(range(0, 100, 2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
...     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
...
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders


>>> supplies = ['pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens']
>>> for i in range(len(supplies)):
...     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
...
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens

##multiple assignment

>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
>>>
>>>
>>> size, color, disposition = cat
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'

>>> a = 'AAA'
>>> b = 'BBB'
>>>
>>> a,b = b,a
>>> a
'BBB'
>>> b
'AAA'

##Augmented assignment operators

>>> spam = 42
>>> spam = spam + 1
>>> spam
43

>>> spam += 1
>>> spam
44

##methods
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'foo' is not in list
>>> spam = ['sophie', 'pooka', 'fat-tail', 'pooka']
>>> spam.index('pooka')
1

>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']

>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']

>>> spam.append('moose')
>>> spam
['cat', 'chicken', 'dog', 'bat', 'moose']
>>> spam.append('moose')
>>> spam
['cat', 'chicken', 'dog', 'bat', 'moose', 'moose']

>>> spam.remove('bat')
>>> spam
['cat', 'chicken', 'dog', 'moose', 'moose']

>>> spam
[2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam.sort(reverse=True)
>>> spam
[5, 3.14, 2, 1, -7]

>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>>
>>>
>>> spam
['a', 'A', 'z', 'Z']
