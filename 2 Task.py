import random

def get_numbers_ticket(min_value, max_value, quantity):
    if not(1 <= min_value <= max_value <= 1000) or not(1 <= quantity <= max_value - min_value + 1):
        return []
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        random_number = random.randint(min_value, max_value)
        unique_numbers.add(random_number)
    return sorted(list(unique_numbers))

min_value = 1
max_value = 49
quantity = 6
result = get_numbers_ticket(min_value, max_value, quantity)
print(f'Ваші унікальні випадкові числа: {result}')
