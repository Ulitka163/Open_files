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
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_create('files.txt')
    number_ingredient = {}
    for cook in dishes:
        if cook in cook_book.keys():
            for values in cook_book.get(cook):
                if values.get('ingredient_name') in number_ingredient.keys():
                    number_ingredient[values.get('ingredient_name')]['quantity'] = number_ingredient[values.get('ingredient_name')]['quantity'] + int(values.get('quantity')) * person_count
                else:
                    number_ingredient[values.get('ingredient_name')] = {'measure': values.get('measure'),
                                                                    'quantity': int(values.get('quantity')) * person_count
                                                                    }
    return print(number_ingredient)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


