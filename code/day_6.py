# tuples = immutable, unchangeable collection of different data types
tuple_1 = tuple()
sisters = ("Alice", "Brittney")
brothers = ("Alex", "Bob")
siblings = sisters + brothers
print(siblings)
print(len(siblings))
family_members = ("Adam", "Brianna") + sisters + brothers
print(family_members)

dad, mum, sister_1, sister_2, brother_1, brother_2 = family_members
print(dad)

fruits = ("Apple", "Banana", "Cherry")
vegetables = ("Carrots", "Cucumber")
animal_products = ("Beef", "Chicken")
food_tuple = fruits + vegetables + animal_products
print(food_tuple)
print(food_tuple[len(food_tuple) // 2])
print(food_tuple[:3] + food_tuple[-3:])

del food_tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
