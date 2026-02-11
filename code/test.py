from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

stop_words = ENGLISH_STOP_WORDS
print(stop_words)
print(type(stop_words))

print("adam" in stop_words)
print("another" in stop_words)