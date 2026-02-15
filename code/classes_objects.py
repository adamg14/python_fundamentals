# Python is an object oriented programming.
# everything in python is an object with properties and methods
# e.g. a number or a string is a program with an object of corresponding built-in class
# create a class to create an object, a class is like an object constructor or blueprint for creating objects
# instantiate a class to create an object
# the class defines the behaviour and attributes of the object, the object represents the class

# defining the class
class Person:
    # defining the constructor for the class
    def __init__(self, first_name, last_name, age, city, country):
        # adding additional parameters to the constructor function
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.skills = []
    
    # Methods are functions that belong to the Object
    def getFullName(self):
        return f"Hello, my name is {self.first_name} {self.last_name}."
    
    def getLocation(self):
        return f"I am from {self.city}, {self.country}"

    # method to modify class values
    def addSkill(self, skill):
        self.skills.append(skill)

# inheritance - reusing parent class code. 
# inheritance allows us to define a class that inherits all the methods and properties from parent class
# the parent class is the base/super class which gives all the methods and properites 
# child class is the class that inherits from the parent class

class Student(Person):
    # overriding parent methods
    def getLocation(self):
        return f"I am studying in {self.city}, {self.country}"


# creating an object
p = Person(
    'Alice',
    'Bob',
    42,
    'London',
    'United Kingdom'
    )

print(p)
print(p.first_name)
print(p.getFullName())
print(p.getLocation())
print(p.skills)
p.addSkill('Piano')
print(p.skills)

s1 = Student('Bob', 'Alice', 12, 'Munich', 'Germany')
print(s1.city)
print(s1.skills)
s1.addSkill('Marketing')
s1.addSkill('Spanish')
print(s1.skills)
print(s1.getLocation())


# the statistics inherist from the list class and then extends the features
class Statistics(list):

    def count_items(self):
        return len(self)
    
    def sum(self):
        return sum(self)

    def min(self):
        return min(self)
    
    def max(self):
        return max(self)
    
    def range(self):
        return max(self) - min(self)
    
    def mean(self):
        return sum(self) / len(self)
    
    def median(self):
        if len(self) % 2 == 0:
            return (sorted(self)[len(self) // 2 - 1] + sorted(self)[len(self)//2]) / 2
        else:
            return sorted(self)[len(self) // 2]
    
    def mode(self):
        max_count = 0
        mode = None
        for value in self:
            count = self.count(value)
            if count > max_count:
                max_count = count
                mode = value
        
        return {'mode': mode, 'count': max_count}
    
    # standard deviation
    def std(self):
        return round(self.var() ** 0.5, 2)
    
    # variance
    def var(self):
        return round(sum((value - self.mean()) ** 2 for value in self)/ len(self), 2)
    
    def freq_dist(self):
        set_self = set(self)
        frequency = [((self.count(item) / len(self)) * 100, item) for item in set_self]
        return sorted(frequency, key=lambda x: x[0], reverse=True)
    
    def describe(self):
        return f"""
        Count: {self.count_items()}
        Sum: {self.sum()}
        Min: {self.min()}
        Max: {self.max()},
        Range: {self.range()},
        Mean: {self.mean()},
        Median: {self.median()},
        Mode: {self.mode()},
        Standard Deviation: {self.std()},
        Variance: {self.var()},
        Frequency Distribution: {self.freq_dist()}
        """
    
ages = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print(ages.count_items())
print(ages.sum())
print(ages.min())
print(f"this should be the median : {ages.median()}")
print(ages.mode())
print(ages.freq_dist())
print(ages.var())
print(ages.std())


class PersonAccount():
    def __init__(
            self,
            first_name,
            last_name,
            incomes,
            expenses,
    ):
        self.first_name = first_name
        self.last_name = last_name
        # optionally could be defined as lists below
        self.incomes = incomes
        self.expenses = expenses
    
    def account_balance(self):
        return self.incomes - self.expenses
    
    def total_income(self):
        return self.incomes
    
    def total_expenses(self):
        return self.expenses
    
    def add_income(self, amount):
        self.incomes += amount
    
    def reduce_income(self, amount):
        self.incomes -= amount
    
    def add_expense(self, amount):
        self.expenses += amount
    
    def reduce_expenses(self, amount):
        self.expenses -= amount
        
    def account_info(self):
        return f"""
        first_name: {self.first_name},
        last_name: {self.last_name},
        total_income: {self.total_income()},
        total_expenses: {self.total_expenses()}
        account_balance: {self.account_balance()}"""
    

person_one = PersonAccount(
    'Alice',
    'Bob',
    100000,
    85000
)

print(person_one.total_income())