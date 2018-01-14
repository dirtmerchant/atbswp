#! /usr/bin/env python3

import re

>>> import re
>>> phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneNumberRegex.search('My number is 415-555-4242')
<_sre.SRE_Match object; span=(13, 25), match='415-555-4242'>
>>> mo = phoneNumberRegex.search('My number is 415-555-4242')
>>> mo.group()
'415-555-4242'
>>> phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumberRegex.search('my number is 415-555-4242')
>>> mo.group()
'415-555-4242'
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-424

>>> import re
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo = batRegex.search('Batmotorcycle lost a wheel')
>>> mo == None
True
>>> mo.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo = batRegex.search('Batmotorcycle lost a wheel')
>>>
>>>
>>>
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group(1)
'mobile'
>>>
