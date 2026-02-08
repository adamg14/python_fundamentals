import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# \b = word boundary, the start and end of the word
# \w+ = one or more word characters
# \b

words = re.findall(r'\b\w+\b', paragraph.lower())
freq = Counter(words)
freq_list = list(freq.items())
print(freq_list)

paragraph2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
numerical_matches = r'-?\d+'
string_matches = re.findall(numerical_matches, paragraph2)
points = list(map(lambda x: int(x), string_matches))
print(points)
sorted_points = sorted(points)
distance = abs(sorted_points[0] - sorted_points[-1])
print(distance)


def is_valid_variable(variable_name):
    regex_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    matches = re.findall(regex_pattern, variable_name)
    if matches:
        return True
    else:
        return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    clean_setence = re.sub(r'[%@$&#;]', "", sentence)
    return clean_setence 

print(clean_text(sentence=sentence))

def most_frequent_words(cleaned_text):
    words = re.findall(r'\b\w+\b', cleaned_text.lower())
    freq = Counter(words)
    freq_list = list(freq.items())
    return freq_list

print(most_frequent_words(clean_text(sentence=sentence)))