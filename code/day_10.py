count = 0

while count < 11:
    print(count)
    count += 1

count = 10

while count > 0:
    print(count)
    count -= 1

str = '#'
while len(str) < 8:
    print(str)
    str += '#'

for i in range(7):
    for i in range(8):
        print('*', end="")
    print()

for i in range(0, 11):
    print(f"{i} x {i} = {i * i}")

my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in range(0, len(my_list)):
    print(my_list[i])

for i in range(0, 101):
    if i % 2 == 0:
        print(i)

for i in range(0, 101):
    if i % 2 == 1:
        print(i)

sum = 0
for i in range(0, 101):
    sum += i
else:
    print('The sum of all numbers is' + str(sum))