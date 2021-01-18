def sortSur(nameList):
	l2 = []

	# create 2d list of names
	for ele in nameList:
		l2.append(ele.split())
	nameList = []

	# sort by last name
	for ele in sorted(l2, key=lambda x: x[-1]):
		nameList.append(' '.join(ele))

	# return sorted list
	return nameList


# Driver Code

# assign list of names
nameList = ['John Wick', 'Jason Voorhees',
			'Freddy Krueger', 'Keyser Soze',
			'Mohinder Singh Pandher']

# display original list
print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))
