import webbrowser
import requests
import json
from maths_package.maths import add_numbers
from statistics import mean, stdev
import math

url_lists = [
    'http://www.python.org',
    'http://www.google.com'
]


# for url in url_lists:
#     webbrowser.open_new_tab(url)

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
w3_text = response.text
print(response.headers)
print(response.status_code)

countries_url = 'https://restcountries.com/v3.1/name/germany'

response = requests.get(countries_url)
country_data = response.json()
print(country_data)

print(add_numbers(1, 2, 3))

def calculate_mean(*args):
    mean = sum(args) / len(args)
    return mean

cat_url = 'https://api.thecatapi.com/v1/breeds'
cat_response = requests.get(cat_url)
cat_json = cat_response.json()
cat_weight = [calculate_mean(int(cat["weight"]["metric"][0]), int(cat["weight"]["metric"][-1])) for cat in cat_json] 
print(cat_weight)

min_weight = sorted(cat_weight)[0]
max_weight = sorted(cat_weight)[-1]
mean_weight = sum(cat_weight) / len(cat_weight)
print(min_weight)
print(max_weight)
print(mean_weight)
median_weight = sorted(cat_weight)[math.floor(len(cat_weight) / 2)]
print(median_weight)
standard_deviation = stdev(cat_weight)
print(standard_deviation)
# database packages = sqlalchemy
# web development = django, flask
# html parser = beautiful soup, pyquery
# xml processing = elementtree
# network = requests

