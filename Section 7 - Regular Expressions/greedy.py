>>>
>>> import re
>>>
>>>
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo = batRegex.search('The Adventures of Batman')
>>> mo.group()
'Batman'
>>> mo = batRegex.search('The Adventures of Batwoman')
>>> mo.group()
'Batwoman'
>>>
>>>
>>> mo = batRegex.search('The Adventures of Batwowowowwoman')
>>> mo.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo == None
True
>>>
>>>
>>>
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('My phone number is 415-555-1234, call me tomorrow.')
>>> mo.group()
'415-555-1234'
>>>
>>> mo = phoneRegex.search('My phone number is 555-1234, call me tomorrow.')
>>> mo == None
True
>>>
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('My phone number is 415-555-1234, call me tomorrow.')
>>> phoneRegex.search('My phone number is 415-555-1234, call me tomorrow.')
<_sre.SRE_Match object; span=(19, 31), match='415-555-1234'>
>>> phoneRegex.search('My phone number is 555-1234, call me tomorrow.')
<_sre.SRE_Match object; span=(19, 27), match='555-1234'>
>>>
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> batRegex.search('The Adventures of Batman')
<_sre.SRE_Match object; span=(18, 24), match='Batman'>
>>> batRegex.search('The Adventures of Batwoman')
<_sre.SRE_Match object; span=(18, 26), match='Batwoman'>
>>> batRegex.search('The Adventures of Batwowowowowoman')
<_sre.SRE_Match object; span=(18, 34), match='Batwowowowowoman'>
>>>

>>>
>>> import re
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> batRegex.search('The Adventures of Batman')
<_sre.SRE_Match object; span=(18, 24), match='Batman'>
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> batRegex.search('The Adventures of Batman')
>>> batRegex.search('The Adventures of Batman') == None
True
>>> batRegex.search('The Adventures of Batwoman') == None
False
>>> batRegex.search('The Adventures of Batwowowowowoman') == None
False
>>> batRegex.search('The Adventures of Batwowowowowoman')
<_sre.SRE_Match object; span=(18, 34), match='Batwowowowowoman'>
>>> batRegex.search('The Adventures of Batwoman')
<_sre.SRE_Match object; span=(18, 26), match='Batwoman'>

>>> regex = re.compile(r'\+\*\?')
>>>
>>> regex.search('I learned about +*? regex syntax')
<_sre.SRE_Match object; span=(16, 19), match='+*?'>

>>> haRegx = re.compile(r'(Ha){3}')
>>> haRegx.search('He said "HaHaHa"')
<_sre.SRE_Match object; span=(9, 15), match='HaHaHa'>
>>>

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
>>> phoneRegex.search('My phone numbers are 415-555-1234,555-4242,212-555-0000')
<_sre.SRE_Match object; span=(21, 55), match='415-555-1234,555-4242,212-555-0000'>

>>> haRegex = re.compile(r'(Ha){3,5}')
>>> haRegex.search('He said "HaHaHa"')
<_sre.SRE_Match object; span=(9, 15), match='HaHaHa'>
>>> haRegex.search('He said "HaHaHaHaHa"')
<_sre.SRE_Match object; span=(9, 19), match='HaHaHaHaHa'>
>>> haRegex.search('He said "HaHaHaHaHaHaHa"')
<_sre.SRE_Match object; span=(9, 19), match='HaHaHaHaHa'>

>>> digitRegex.search('1234567890')
<_sre.SRE_Match object; span=(0, 5), match='12345'>
>>> digitRegex = re.compile(r'(\d){3,5}?')
>>> digitRegex.search('1234567890')
<_sre.SRE_Match object; span=(0, 3), match='123'>
