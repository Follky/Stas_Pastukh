from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    date_difference = current_date - input_date
    return date_difference.days

date_input = '2020-10-09'
result = get_days_from_today(date_input)
print(f'Кількість днів від {date_input} до поточної дати: {result}')
