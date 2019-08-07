import random
import json

from main import Porker

def generate ():
    card_list = []
    for _ in range(5):
        card_list.append({"num":random.choice(num_list), "mark": random.choice(mark_list)})
    return card_list

def has_not_duplicates(card_list):
    return len(card_list) == len(set(map(json.dumps, card_list)))

num_list = [ i for i in range(1,14) ]
mark_list = [i for i in range(4)]
card_list = []

while True:
    card_list = generate()
    if has_not_duplicates(card_list) == True:
        break
print(card_list)

Porker().judgment_role(card_list)

