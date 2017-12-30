>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat
{'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'

>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> ham
{'species': 'cat', 'name': 'Zophie', 'age': 8}
>>> eggs == ham
True

>>> list(eggs.keys())
['name', 'species', 'age']
>>> list(eggs.values())
['Zophie', 'cat', 8]
>>> list(eggs.items())
[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]

>>> list(eggs.keys())
['name', 'species', 'age']
>>> list(eggs.values())
['Zophie', 'cat', 8]
>>> list(eggs.items())
[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
>>> eggs.keys()
dict_keys(['name', 'species', 'age'])
>>>
>>> for k in eggs.keys():
...     print(k)
...
name
species
age
>>>
>>> for i in eggs.items():
...     print(i)
...
('name', 'Zophie')
('species', 'cat')
('age', 8)
>>>
>>> eggs['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'color'
>>>
>>>
>>>
>>> if 'color' in eggs:
...     print(eggs['color'])
...
>>>
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')
I am bringing 0 to the picnic.

>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> if 'color' not in eggs:
...     eggs['color'] = 'black'
...
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}


>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
>>>
>>> eggs.setdefault('color', 'orange')
'black'
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
