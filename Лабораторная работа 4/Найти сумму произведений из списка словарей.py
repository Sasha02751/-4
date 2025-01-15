import json


def task() -> float:
    with open('input.json', 'r') as file:
        items = json.load(file)

    total_sum = 0.0

    for item in items:
        if 'score' in item and 'weight' in item:
            product = item['score'] * item['weight']
            total_sum += product

    return round(total_sum, 3)


print(task())
