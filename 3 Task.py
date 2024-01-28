import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if cleaned_number.startswith('+'):
        return cleaned_number
    else:
        return '+38' + cleaned_number[1:]

phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11"
]

for number in phone_numbers:
    normalized_number = normalize_phone(number)
    print(f"Original: {number}, Normalized: {normalized_number}")
