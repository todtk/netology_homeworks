# -*- coding: utf-8 -*-

import requests
import json


URL = "https://akabab.github.io/superhero-api/api/all.json"

def find_intelligence(target_hero):
    response = requests.get(URL)
    response = json.loads(response.text)
    hero_dict = exract(response)
    result = None
    for hero in target_hero:
        intelligence = hero_dict[hero]
        if result is None:
            result = [hero, intelligence]
        else:
            if intelligence > result[1]:
                result = [hero, intelligence]
    return f"Cамый умный {result[0]}"

def exract(response):
    hero_dict = {}
    for item in response:
        name = item["name"]
        intelligence = item["powerstats"]["intelligence"]
        hero_dict[name] = intelligence
    return hero_dict


print(find_intelligence(["Hulk", "Captain America", "Thanos"]))