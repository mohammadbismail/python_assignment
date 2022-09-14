# 4)Iterate Through a Dictionary with List Values

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def printInfo(dojo):
    for key in dojo.keys():
        print(len(dojo[key]), key)
        for i in range(len(dojo[key])):
            print(dojo[key][i])


printInfo(dojo)
