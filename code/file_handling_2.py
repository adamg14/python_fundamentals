import json


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