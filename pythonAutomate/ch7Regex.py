#!/usr/bin/python

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print "Phone number found:" + mo.group()
print "Area code is:" + mo.group(1)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batcopter does not exist')
print mo.group()
print mo.group(1)

batRegex = re.compile(r'Bat(wo)?man')
moMen = batRegex.search('The adventures of Batman')
moWomen = batRegex.search('The adventures of Batwoman')
print moMen.group()
print moWomen.group()

haRegex = re.compile(r'(ha){3}')
haRangeRegex = re.compile(r'(ha){3,5}')
ha1 = haRegex.search('ha')
ha2 = haRegex.search('haha')
ha3 = haRegex.search('hahaha')
ha10 = haRangeRegex.search('ha'*10)
if ha1: print ha1.group()
if ha2: print ha2.group()
if ha3: print ha3.group()
print 'ha'*10

vowelRegex = re.compile(r'[aeiouAEIOU1-9]')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
vowelList = vowelRegex.findall('2 RoboCop eats 19 jars of baby food and 4 bottles of milk. BABY FOOD.')
consonantList = consonantRegex.findall('2 RoboCop eats 19 jars of baby food and 4 bottles of milk. BABY FOOD.')
print vowelList
print consonantList


#case insensitivity
robocop = re.compile(r'robocop',re.I)
result = robocop.search('RoboCop is part man, part machine, all cop.').group()
print result

result = robocop.search('ROBOCOP protects the innocent').group()
print result

result = robocop.search('Al,why does your programmign book talk about robocop so much?').group()
print result

namesRegex = re.compile(r'Agent \w+')
result = namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
print result

agentNamesRegex = re.compile(r'Agent (\w)\w*')
result = agentNamesRegex.sub(r'\1***','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print result

ultimatePhoneRegex = re.compile(r'''(
										(\d{3}|\(\d{3}\))?							#area code 415 or (415)
										(\s|-|\.)?											#separator ' ' or '-' or '.'
										\d{3}														#first 3 digits
										(\s|-|\.)												#separator ' ' or '-' or '.'
										\d{4}														#last 4 digits
										(\s*(ext|x|ext.)\s*\d{2,5})?		#possible extension. 'ext' or 'x' or 'ext.'
										)''',re.VERBOSE)
