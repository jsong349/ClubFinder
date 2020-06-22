fruits = "apple banana apple peach pear"
boop = "doodle"


def container(paragraph):
    words = paragraph.split(" ")
    d = {}

    for word in words:
        if word in d:
            d[word] += d[word]
        else:
            d[word] = 1

    for key in d:
        print(key, ":", d[key])

    return d


def match(keyword, dictionary):
    if keyword in dictionary:
        return dictionary


if __name__ == "__main__":
    x = container(fruits)
    print(match(boop, x))
