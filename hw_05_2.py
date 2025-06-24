import re
from typing import Callable

def generator_numbers(text: str):
    # Пошук усіх дійсних чисел, що відокремлені пробілами
    pattern = r'\ \d+\.\d+\ '
    for match in re.findall(pattern, text):
        yield float(match)  # перетворюємо на float

def sum_profit(text: str, func: Callable):
    return sum(func(text))  # підсумовуємо всі числа з генератора

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
