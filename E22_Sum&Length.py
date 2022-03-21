"""
grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)
"""

lottery_numbers = {13, 21, 22, 5, 8}

players = [

    {
        'name': 'Joseph',
        'numbers': {5, 12, 24, 15, 22}
    },

    {
        'name': 'Rachel',
        'numbers': {8, 13, 4, 10, 5}
    }

]

name1 = players[0]['name']
name2 = players[1]['name']

numbers1 = lottery_numbers.intersection(players[0]['numbers'])
numbers2 = lottery_numbers.intersection(players[1]['numbers'])

print(f"Player {name1} got {len(numbers1)} numbers right!")
print(f"Player {name2} got {len(numbers2)} numbers right!")