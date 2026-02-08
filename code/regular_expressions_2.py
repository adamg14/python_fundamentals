import re

# to declare a regex variable use r before the string, the following only identifies apple in lowercase
regex_pattern = r"apple"
text = "Apple and bananas are fruits. An apple a day keeps the doctor away"
matches = re.findall(regex_pattern, text)
print(matches)

# to look for apple where it is not case sensitive
regex_pattern = r"[Aa]pple"
all_matches = re.findall(regex_pattern, text)
print(all_matches)
# or just add the case insensitive flag
all_matches = re.findall(regex_pattern, text, re.I)
print(all_matches)

# [] = a set of characters
# [a-c] = a, b, c
# [a-z] = a to z
# [A-Z] = A to Z
# [0-3] = 0, 1, 2, 3
# [0-9] = any number 0 to 9
# [A-Za-z0-9] = a single character, a to z, A to Z, 0 to 9

# \ uses to escape special characters
# \d = match where the string contains a digit (0-9)
# \D means match where the string does not contain a digit
# . = any character except a new line
# ^ = starts with
# r'^substring' = a sentence that starts with the substring
# r'[^abc]' means not a, not b, not c
# $ = ends with
# r'love$' = sentence that ends with the word love
# * = zero or more times e.g. e'[a]*'
# + = one or more times
# ? = zero or one time
# {3} = exactly 3 characters
# {3,} at least 3 characters
# {3, 8} = 3 to 8 characters

# | either or e.g. r'apple|banana' means either apple or banana
# () capture and group

regex_pattern = r'[Aa]pple|[Bb]anana'
all_matches = re.findall(regex_pattern, text)
print(all_matches)

# d means digits
regex_pattern = r'\d' 
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
single_matches = re.findall(regex_pattern, txt)
print(single_matches)
# one or more digits 
regex_pattern = r'\d+'
all_matches = re.findall(regex_pattern, txt)
print(all_matches)

# starts with an a and has any number of characters preceding
regex_pattern = '[Aa].'
txt = '''Apple and banana are fruits'''
all_starting_a = re.findall(regex_pattern, txt)
print(all_starting_a)

# finds the first a and gets everything after i
# . = any character
# + = one or more time
# .+ = any character one or more times
regex_pattern = '[a].+'
matches = re.findall(regex_pattern, txt)
print(matches)

# ? = zero or one time, which means that it is it is optional
# in this case the dash is optional
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r"[Ee]-?mail"
email_matches = re.findall(regex_pattern, txt)
print(email_matches)

# decimal exactly 4 times
regex_pattern = r'\d{4}'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
year_matches = re.findall(regex_pattern, txt)
print(year_matches)

# ^ starts with this
reg = r'^This'
# ^ negation, doesnt start with a letter therefore a number ^[a-zA-Z]+'