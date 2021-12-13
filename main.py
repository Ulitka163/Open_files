def cook_book_create(file):
    with open(file, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            ingredients = []
            cook_book[line.strip()] = ingredients
            for i in range(int(file.readline())):
                ingredient = file.readline().strip()
                ingredients.append({'ingredient_name': ingredient.split('|')[0],
                                    'quantity': ingredient.split('|')[1],
                                    'measure': ingredient.split('|')[2]
                                    }
                                   )
            file.readline()
    return print(cook_book)


cook_book_create('files.txt')