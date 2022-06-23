# -*- coding: utf-8 -*-

import os
from pprint import pprint



def search_path():
    FILE_NAME = "recipes.txt"
    BASE_PATH = os.getcwd()
    FULL_PATH = os.path.join(BASE_PATH, FILE_NAME)
    return FULL_PATH


def file_reader():
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


pprint(file_reader())