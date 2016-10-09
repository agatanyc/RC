"""`Given an input string and a dictionary of words,
segment the input string into a space-separated
sequence of dictionary words if possible. For
example, if the input string is "applepie" and
dictionary contains a standard set of English words,
then we would return the string "apple pie" as output."""

from nltk.corpus import words

engdict = ["apple", "pie", "brown", "green", "blue", "red"]

def divide(s):
	first = ''
	for i in range(len(str(s))):
		first += s[i]
		print first
		if first in words.words() and s[i + 1:] in words.words():
			return ' '.join([first, s[i + 1:]])
	return False

print divide('applepie')

# recursive solution
def rec_divide(s, engdict):
	if s in engdict:
		return s
	for i in range(len(s)):
		prefix = s[:i]
		if prefix in engdict:
			suffix = s[i:]
			divide_suffix = rec_divide(suffix, engdict)
			if divide_suffix:
				return prefix + ' ' + divide_suffix
	
	return None

print rec_divide('applepie', engdict=engdict), 'YAAAY'
print rec_divide('appleboo', engdict=engdict), 'NOOOO'

# other solutions:

def r_divide0(s):
	if s == "":
		return []
	else:
		mw = r_divide0(s[1:])
		mysum = 0
		for w in mw:
			mysum += len(w)

		if mysum == 0:
			wordCandidate = s
		else:
			wordCandidate = s[:(-1 * mysum)]
		if wordCandidate in engdict:
			mw.insert(0, wordCandidate)
		return mw
def r_divide(s):
	return ' '.join(r_divide0(s))

def divahead0(s, pointer):
	if s == "":
		return []
	else:
		if s[:pointer] in engdict:
			myword = s[:pointer]
			restOfTheText = s[pointer:]
			otherWords = divahead0(restOfTheText, 1)
			otherWords.insert(0, myword)
			return otherWords
		else:
			return divahead0(s, pointer + 1)

def divahead(s):
	return ' '.join(divahead0(s, 1))


print r_divide('bluebrownred')
print r_divide("applepiegreen")
print divahead('bluebrownred')
print divahead("applepiegreen")
	
