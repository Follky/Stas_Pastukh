from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        days_until_birthday = (birthday - today).days

        if days_until_birthday < 0:
            birthday = birthday.replace(year=today.year + 1)
            days_until_birthday = (birthday - today).days

        if birthday.weekday() >= 5:  # 5 та 6 - субота і неділя
            days_until_birthday += (7 - birthday.weekday())

        if 0 <= days_until_birthday <= 7:
            congratulation_date = today + timedelta(days=days_until_birthday)
            congratulation_info = {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")}
            upcoming_birthdays.append(congratulation_info)

    return upcoming_birthdays

users = [
    {"name": "John", "birthday": "2000.01.15"},
    {"name": "Alice", "birthday": "1995.12.31"},
    {"name": "Bob", "birthday": "2005.02.20"},
]

result = get_upcoming_birthdays(users)
for info in result:
    print(f"{info['name']} - {info['congratulation_date']}")
