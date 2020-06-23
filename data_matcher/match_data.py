import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
import json

def preprocess(para):
    stop_words = set(stopwords.words('english')) 
    for word in stop_words:
        if word in para:
            para.pop(word)
    return para

def container(paragraph):
    words = paragraph.split(" ")
    d = {}

    for word in words:
        word = word.lower()
        if word in d:
            d[word] += d[word]
        else:
            d[word] = 1
    return preprocess(d)

def match(keywords, dictionary):
    matched = False
    num = 0
    for keyword in keywords:
        full_points = True
        if keyword in dictionary:
            num += (full_points + 0.5) * dictionary[keyword]
            full_points = False
            matched = True
        synonyms = synonym(keyword)
        for word in synonyms:
            if word in dictionary:
                num += (full_points + 0.5) * dictionary[word]
                full_points = False
                matched = True
    return matched, num

def suggest_club(keywords):
    with open("../data/org_data.json", 'r') as j:
        contents = json.loads(j.read())
    result = []
    for club in contents:
        matched, num = match(keywords, container(contents[club]))
        if matched:
            result.append((club, num))
    return display_top_five(result)


def synonym(keyword):
    synonyms = []
    for syn in wordnet.synsets(keyword):
        for lem in syn.lemmas():
            synonyms.append(lem.name().replace("_", " "))
    return synonyms

def display_top_five(clubs):
    result = {}
    for club in clubs:
        if len(result) < 5:
            result[club] = club[1]
        else:
            first = True
            for c in result:
                if first:
                    min_club = c
                    first = False
                    break
                if result[c] < result[min_club]:
                    min_club = c
            if club[1] > result[min_club]:
                result.pop(min_club)
                result[club] = club[1]
    return [key for key in result]


if __name__ == "__main__":
    # fruits = "joyful blue red green pitiful"
    # boop = "business"
    # x = container(fruits)
    # print(match(boop, x))
    print(suggest_club(["software", "design", "team", "collaboration"]))
