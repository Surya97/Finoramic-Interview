import json
dependencies = []
f = open('package.json', 'r+')

d = json.load(f)

dependencies = d['Dependencies']

'''
for each in dependencies:
	print(each)
'''

import pip

flag = True
for each in dependencies:
	try:
		pip.main(['install', each])
	except:
		print('Failed to install', each)
		flag = False
		continue

if flag:
	print('Success')
