#!/usr/bin/python
#GOAL: EXTRACT Phone Numbers and Emails.
import re
import urllib

url = 'https://www.nostarch.com/contactus.htm'
uh = urllib.urlopen(url)
print "Retrieving ", url
#data = uh.read()
data = 'Contact Us No Starch Press, Inc. 245 8th Street San Francisco, CA 94103 USA Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST) Fax: +1 415.863.9950 Reach Us by Email General inquiries: info@nostarch.com Media requests: media@nostarch.com Academic requests: academic@nostarch.com (Please see this page for academic review requests)	Help with your order: info@nostarch.com Reach Us on Social Media Twitter Facebook'

phoneNumRegex = re.compile(r'''(
																(\d{3}|\(\d{3}\))?	#area code.
																(\s|-|.)?						#separator
																(\d{3})							#first 3 digits
																(\s|-|.)?						#separator
																(\d{4})							#last 4 digits.
																(\s*(ext|ext.|x)\s*(\d{2,5}))?  #extensions
																)''',re.VERBOSE)

emailRegex = re.compile(r'([\w\S]*)@(\w*).(\w{2,5})',re.DOTALL)
result = emailRegex.search('My email is michelle.y.ho@gmail.edu')
print "username:" + result.group(1)
print "host:" + result.group(2)
print "domain:" + result.group(3)
result = emailRegex.search('For Queries. Please send to  123.And-Me64@research.uk')
print "username:" + result.group(1)
print "host:" + result.group(2)
print "domain:" + result.group(3)
print result.group()

phoneNumList = []
emailList = []

print data
phoneResult = phoneNumRegex.findall(data)
if phoneResult:
	for elem in phoneResult:
		print "Found phone #:" + elem[0]
emailResult = emailRegex.search(data)
if emailResult:	
	print "Found email:" + emailResult.group()



	
