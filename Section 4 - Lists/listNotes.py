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
