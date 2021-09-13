from pprint import pprint

from collections import Counter

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            number_dishes = int(file.readline())
            dish_list = []
            for ingredient in range(number_dishes):
                ingredient_name, quantity, measure = file.readline().split('|')
                dish_list.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()}
                )
            result[dish_name] = dish_list
            file.readline()
    return result

result_dict = prepare_dict("recipes2.txt")

def get_shop_list_by_dishes(dishes, person_count):

  result = {}
  may_list = []
  for dishe in dishes:
    if dishe in result_dict:
        for ingredient in result_dict[dishe]:    
            ingredients = ingredient['ingredient_name']
            may_list.append(ingredients)
            count_dict = Counter(may_list)
            dish_list = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count * count_dict[ingredients]}
            result[ingredients] = dish_list
  return result

pprint(get_shop_list_by_dishes(['Омлет','Омлет'], 1))