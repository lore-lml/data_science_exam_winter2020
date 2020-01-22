from nltk.stem.snowball import ItalianStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
stem = SnowballStemmer(language='italian')
lem = WordNetLemmatizer()
print(lem.lemmatize("abbandonata"))
print(stem.stem("abbandonata"))
print(stem.stem("abbandonerà"))