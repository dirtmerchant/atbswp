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

 
