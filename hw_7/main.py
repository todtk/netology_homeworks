# -*- coding: utf-8 -*-

import os
from pprint import pprint


def search_path():
    FILE_NAME = "recipes.txt"
    BASE_PATH = os.getcwd()
    FULL_PATH = os.path.join(BASE_PATH, FILE_NAME)
    return FULL_PATH

def file_reader():
    """ЧИТАЕТ РЕЦЕПТЫ ИЗ ФАЙЛА, ГЕНЕРИРУЕТ СЛОВАРЬ ПО 1 ЗАДАЧЕ"""
    cook_book = {}
    FULL_PATH = search_path()
    with open(FULL_PATH, encoding="utf-8") as f:
        for line in f:
            dish_name = line.strip()
            ingredients = []
            for ingredient in range(int(f.readline())):
                ingredient = (f.readline()).strip()
                ingredient = ingredient.split(" | ")
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    """БЕРЕТ ВОЗВРАТ ИЗ FILE_READER И ГЕНЕРИРУЕТ СПИСОК ПОКУПОК ДЛЯ 2 ЗАДАЧИ"""
    cook_book = file_reader()
    shop_list = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingredient in recipe:
            shop_list[ingredient["ingredient_name"]] = {"measure": ingredient["measure"], "quantity": (int(ingredient["quantity"])*person_count)}
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))