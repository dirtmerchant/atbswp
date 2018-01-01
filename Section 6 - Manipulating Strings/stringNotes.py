... """
>>> print(len(spam))
132213
>>> spam = 'Hello world!'
>>>
>>>
>>>
>>> spam[1:5]
'ello'
>>> spam[-1]
'!'
>>> 'x' in spam
False
>>> 'Hello' in spam
True
>>>
>>>
>>>
>>> spam = 'Hello world'
>>> spam.upper()
'HELLO WORLD'
>>> answer = input()
yes
>>> if answer == 'yes':
...     print('Playing again')
...
Playing again
>>> answer.lower() == 'yes'
True
>>>
>>>
>>>
>>> spam = "Hello world!/home/attask/bin/maintenance -d/home/attask/bin/maintenance -d'
KeyboardInterrupt
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>>
>>> spam.isupper()
False
>>> spam = ''
>>> spam.isupper()
False
>>> spam.islower()
False
>>>
>>>
>>>
>>>
>>> spam
''
>>>
>>>
>>>
>>> 'Hello world!'.isspace()
False
>>> 'Hello world!'[5].isspace()
True
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.startswith('H')
True
>>> 'Hello world!'.startswith('ello')
False
>>>
>>>
>>> 'Hello world!'.endswith('world'
... )
False
>>> 'Hello world!'.endswith('world!')
True
>>>


>>> 'Hello'.rjust(10)
'     Hello'
>>>  'Hello'.rjust(10)
KeyboardInterrupt
>>> 'Hello'.ljust(10)
'Hello     '
>>>

>>>
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
>>> name = 'Al'
>>> name.center(20, '=')
'=========Al========='
>>>


>>> spam = spam.strip()
>>> spam
'Hello'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>>
>>> spam.strip('ampS')
'BaconSpamEggs'
>>>
>>>
>>> spam = 'Hello there!'
>>> spam.repplace('e', 'XYZ')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'repplace'
>>> spam.replace('e', 'XYZ')
'HXYZllo thXYZrXYZ!'



>> import pyperclip
>>>
>>> pyperclip.copy('Hello!!!!')
>>> pyperclip.paste()
'Hello!!!!'
>>>


>>> name = 'Alice'
>>> place = 'Main Street'
>>> time = '6 pm'
>>> food = 'turnips'
>>> 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
'Hello Alice, you are invited to a party at Main Street at 6 pm. Please bring turnips.'
>>>
>>>
>>>
>>> 'Hello %s, you are invited to a part at %s at %s. Please bring %s.' % (name, place, time, food)
'Hello Alice, you are invited to a part at Main Street at 6 pm. Please bring turnips.'
>>>
