import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/'
response = requests.get(url)
status = response.status_code
print(status)

content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

url_2 = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url_2)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup)

presidents_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "explaintext": True,
    "titles": "Artificial intelligence"
}

# headers = {
#     "User-Agent": "MyResearchBot/1.0 (adamg2609@gmail.com)"
# }

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(presidents_url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table")

presidents = tables[1].find("ol").find_all("li")

presidents_object = {}
count = 1
for president in presidents:
    presidents_object[count] = {
          'name': ' '.join(president.text.split(" ")[:-1]),
          'years': president.text.split(" ")[-1]
    }
    count += 1

print(presidents_object)