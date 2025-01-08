fruits = ["apple", "orange", "mango", "banana", "lemon", "pineapple"]
for fruit in fruits:
    print(fruit)


fruits = [["apple", "orange"], ["mango", "banana"], ["lemon", "pineapple"]]
for fruit in fruits:
    for subfruit in fruit:
        print(subfruit)

#list use integer index
shopping_mall = [
    [
        ["fruits","vegetables"], ["meat", "chimkin"], ["drinks", "snacks"]
    ],
    [
        ["clothes", "shoes"], ["jewellery", "watches"], ["cosmetics", "perfumes"]
    ],
    [
        ["books", "magazines"], ["movies", "games"], ["music", "movies"]
    ]
    ]

#dict can have multiple keys
shopping_mall_cat = [
    {
        "food": ["fruits", "vegetables"],
        "meat": ["meat", "chimkin"],
        "snacks": ["drinks", "snacks"]
    },
    {
        "fashion": ["clothes", "shoes"],
        "accessories": ["jewellery", "watches"],
        "beauty": ["cosmetics", "perfumes"]
    },
    {
        "reading": ["books", "magazines"],
        "entertainment": ["movies", "games"],
        "music": ["music", "movies"]
    }
]
