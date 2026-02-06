import re 

# a regular expression is a special text string that helps find patterns in data
# a regex can be used to check if some pattern exists in a different data type
# re modules
# .match() = searches only in the beginning of the first line of the string and returns objects if found, else returns None
# .search() = return a match object if there is one anywhere in the string, include multiline string
# .findall() = returns a list containing all matches
# .split() = takes a string, splits at the match points, returns a list
# .sub() = replaces one or many matches within a string

text = "I love teaching Python and javaScript"

# re.I says to ignore the case, so it will return true
# if there is no match it will return None
match = re.match("i love teaching", text, re.I)
print(match)

# returns a tuple which is the start and end position of the match
span = match.span()
print(span)
start, end = span
substring = text[start:end]
print(substring)

text1 = "I recommend Python for a first programming language"
match1 = re.search('first', text1)
print(match1)
span1 = match1.span()
start1, end1 = span1
print(span1)
search_string = text1[start1: end1]
print(search_string)

text2 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# RETURNS A LIST OF ALL INSTANCES OF PYTHON (case insensitive)
# these will all give the same answer of ['Python', 'python']
matches = re.findall('python', text2, re.I)
matches = re.findall('Python|python', text2)
matches = re.findall('[Pp]ython', text2)
print(matches)

# replacing a substring
text = "Python is the best language. I recommend python to everyone."
match_replace = re.sub('[Pp]ython', 'JavaScript',text)
print(match_replace)

text="My%name%is%adam"
matches = re.sub("%", " ", text)
print(matches)

text = "My name is Adam"
print(re.split(" ", text))

