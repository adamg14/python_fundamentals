import os

# many types of files: text, json, xml, csv, tsv, excel
# can create, read, update and delete files

# file modes:
# r = read
# a = append
# w = write
# x = creates, returns an error if already exists
# t = text = default value
# b = binary mode e.g. images

file = open('code/files/reading_file_example.txt')
# pass the number of characters within the file you want to read e.g. 10
text = file.read()
print(f"This is the text: {text}")


# use file.readline() to read only the first line
# file.readlines() read all the text line by line and returns a list of lines
file = open('code/files/reading_file_example.txt')
text_file = file.read().splitlines()
print(text_file)


# .splitlines() is the same as .readlines()
file = open('code/files/reading_file_example.txt')
text_file = file.readlines()
print(text_file)
# file.close()

# should always close a file, to avoid forgetting to close it you can read the file like this
with open('code/files/reading_file_example.txt', 'r') as input_file:
    text = input_file.readlines()
    print(text)
 

# 'a' = append = add text to the end of the line
# 'w' = write = will overwrite the contents of the file
with open('code/files/reading_file_example.txt', 'a') as input_file:
    input_file.write("\n")
    input_file.write('This should be inserted at the end of the file')

with open('code/files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

# deleting a file
if os.path.exists('code/files/writing_file_example.txt'):
    os.remove('code/files/writing_file_example.txt')
else:
    print("this file does not exist")