capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Portugal': 'Lisbon'
}

travel_log = {
    'France': ['Paris', 'Lyon', 'Marseille'],
    'Germany': ['Berlin', 'Munich', 'Hamburg'],
    'Italy': ['Rome', 'Milan', 'Venice'],
    'Spain': ['Madrid', 'Barcelona', 'Seville'],
    'Portugal': ['Lisbon', 'Porto', 'Faro'] 
}

print(travel_log["France"][1])

nested_list = [
    ['Apple', 'Banana', 'Cherry'],
    ['Dog', 'Cat', 'Mouse'],
    ['Red', 'Blue', 'Green']
]
print(nested_list[1][1])  # Output: Cat

nested_dict = {
    'Fruits': {
        'Citrus': ['Orange', 'Lemon', 'Lime'],
        'Berries': ['Strawberry', 'Blueberry', 'Raspberry']
    },
    'Animals': {
        'Mammals': ['Dog', 'Cat', 'Elephant'],
        'Birds': ['Eagle', 'Parrot', 'Penguin']
    }
}
print(nested_dict['Animals']['Birds'][0])