>>> allCats = []
>>> allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
>>> allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
>>> allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'orange'})
>>> allCats.append({'name': '???', 'age': -1, 'color': 'orange'})
>>>
>>> allCats
[{'name': 'Zophie', 'age': 7, 'color': 'gray'}, {'name': 'Pooka', 'age': 5, 'color': 'black'}, {'name': 'Fat-tail', 'age': 5, 'color': 'orange'}, {'name': '???', 'age': -1, 'color': 'orange'}]

>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
...             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
...             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>>

>>> print(theBoard)
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

>>> import pprint
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}

 >> def printBoard(board):
...        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
...        print('-+-+-')
...        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
...        print('-+-+-')
...        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
...
>>>
>>> printBoard(theBoard)
 | |
-+-+-
 | |
-+-+-
 | |

##type

>>> type(42)
<class 'int'>
>>> type('hello')
<class 'str'>
>>> type(3.14)
<class 'float'>
>>> type(theBoard)
<class 'dict'>
>>> type(theBoard['top-R'])
<class 'str'>
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
