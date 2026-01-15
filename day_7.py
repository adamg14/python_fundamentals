# Sets = a collection of unordered, unindexed collection of items

# string = A collection of ordered characters 
# list = An indexed, ordered collection of the items of the same data types
# tuple = An unindexed, immutable collection of items of different data types
# set = unqiue collection of unindexed, unordered items
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Alibaba", "Samsung"])
it_companies.remove("Facebook")

# remove and discard both remove an element but remove will throw an error when an item is not in the set

print(A.union(B))
print(A.intersection(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))

A.clear()
B.clear()

print(len(age))
age_set= set(age)
print(len(age_set))

string_1 = "I am a teacher and I love to inspire and teach people"
list_1 = string_1.split(" ")
print(list_1)
print(len(list_1))
set_1 = set(list_1)
print(len(set_1))
