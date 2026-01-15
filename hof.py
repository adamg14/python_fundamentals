from functools import reduce

# Behavior Parameterization
def apply_to_all(iterable, func):
    new_iterable = []
    for element in iterable:
        new_iterable.append(func(element))
    return new_iterable


print(apply_to_all([1, 2, 3], lambda x: x ** x))

# lazy evaluation - equivalent to using the map function
def apply_to_all_lazy(iterable, func):
    for element in iterable:
        yield func(element)

print([1, 2, 3], lambda x: x ** x)


# Predicate Injection
def count_if(iterable, predicate):
    return sum(1 for _ in filter(predicate, iterable))


print(
    count_if(
        [1, 5, 3],
        lambda x: True if x > 2 else False
    )
)


# 3. Reusable Filtering Pipeline

def filter_and_map(iterable, predicate, mapper):
    return map(
        mapper,
        filter(predicate, iterable)
    )
    # alteranative answer
    # return (mapper(x) for x in iterable if predicate(x))
print(
    list(
        filter_and_map(
            ["Adam", "AdamWorede"],
            lambda x: True if len(x) > 4 else False,
            lambda x: x.upper()
        )
    )
)


# 4. Accumulator Design
def reduce_to_dict(iterable, key_func, value_func):
    def step_function(acc, x):
        key = key_func(x)
        acc[key] = acc.get(key, 0) + value_func(x)
        return acc
    
    return reduce(
        step_function,
        iterable,
        {}
    )


# 5. Ranking Abstraction

def rank(iterable, score_func, *, reverse=True, limit=None):
    ranked = sorted(iterable,key=score_func,reverse=reverse)
    return ranked if limit is None else ranked[:limit]


# 6. Predicate Factory
def starts_with(letter):
    return lambda x: x[0] == letter


# 7. Comparator Factory
def sort_by(field, *, reverse=False):
    def sorter(iterable):
        return sorted(iterable, key=lambda x: x["name"], reverse=reverse)
    return sorter

countries = [
    {"name": "Finland", "population": 5_500_000},
    {"name": "Iceland", "population": 366_000},
    {"name": "Poland", "population": 38_000_000},
]

sort_by_name = sort_by("name")
sort_by_population = sort_by("population", reverse=True)
print(sort_by_name(countries))
print(sort_by_population(countries))

# 8. Rule Engine
def make_rule(min_val=None, max_val=None):
    def rule_validator(value):
        if min_val is not None and value <= min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        
        return True
    
    return rule_validator
    

valid_age = make_rule(min_val=0, max_val=99)
print(f"{24} is a valid age {valid_age(24)}")
print(f"{131} is not a valid age {valid_age(131)}")


