from nltk.corpus import wordnet

fruits = "joyful blue red green pitiful"
boop = "business"


def container(paragraph):
    words = paragraph.split(" ")
    d = {}

    for word in words:
        if word in d:
            d[word] += d[word]
        else:
            d[word] = 1
    return d


def match(keyword, dictionary):
    if keyword in dictionary:
        return dictionary
    else:
        synonyms = synonym(keyword)
        for word in synonyms:
            if word in dictionary:
                return dictionary


def synonym(keyword):
    synonyms = []
    for syn in wordnet.synsets(keyword):
        for lem in syn.lemmas():
            synonyms.append(lem.name().replace("_", " "))
    print(set(synonyms))
    return synonyms


if __name__ == "__main__":
    x = container(fruits)
    print(match(boop, x))
