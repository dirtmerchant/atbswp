#! /usr/bin/env python3

import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-1234.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))
