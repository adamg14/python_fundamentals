import json
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

stop_words = ENGLISH_STOP_WORDS



def file_analysis(file_path):
    with open(file_path, 'r') as input_file:
        text = input_file.readlines()
    

    return {
        "number of lines": len(text),
        "numer of words": sum(list(map(lambda x: len(x.split()), text)))
    }


print(file_analysis('code/files/donald_trump_speech.txt'))


def most_spoken_languages(file_path, return_length):
    with open(file_path, 'r') as input_file:
        countries = json.load(input_file)
        print(countries)
        languages = list(map(lambda x: x['languages'], countries))
        print(languages)

        language_counter = {}

        for element in languages:
            if isinstance(element, list):
                for item in element:
                    language_counter[item] = language_counter.get(item, 0) + 1
            else:
                language_counter[element] = language_counter.get(element, 0) + 1

        # .items() returns a dict_items view object
        return sorted(
            list(language_counter.items()),
            key = lambda x: x[1],
            reverse=True
        )[:return_length]


print(most_spoken_languages('data/countries_data.json', 10))


def most_populated_countries(file_path, return_length):
    with open(file_path, 'r') as input_file:
        countries = json.load(input_file)

        population = list(map(lambda x: {'country': x['name'], 'population': x['population']}, countries))
        
        sorted_population = sorted(
            population,
            key=lambda x: x['population'],
            reverse=True
        )
        return sorted_population[:return_length]


print(most_populated_countries('data/countries_data.json', 10))


def find_most_common_words(file_path, list_size):
    with open(file_path) as input_file:
        text = input_file.readlines()
        text_list = [word for setence in text for word in setence.split()]
        print(text)
        print(text_list)

        word_counter = {}
        
        for word in text_list:
            word_counter[word] = word_counter.get(word, 0) + 1

        return sorted(list(word_counter.items()), key= lambda x: x[1], reverse=True)[:list_size]

print(find_most_common_words('code/files/donald_trump_speech.txt', 10))


def clean_text(file_path):
    with open(file_path) as input_file:
        text = input_file.readlines()
        text_list = [word for setence in text for word in setence.split()]
        return text_list


def remove_support_word(file_path, stop_words=stop_words):
    text_list = clean_text(file_path)
    cleaned_text_list = []
    for word in text_list:
        if word in stop_words:
            continue
        else:
            cleaned_text_list.append(word)


def programming_count(file_path):
    counter = {
        'Python': 0,
        'JavaScript': 0,
        'Java': 0
    }

    cleaned_text = clean_text(file_path)

    for word in cleaned_text:
        if 'python' == word.lower():
            counter['Python'] += 1
        elif 'java' == word.lower():
            counter['Java'] += 1
        elif 'javascript' == word.lower():
            counter['JavaScript'] += 1