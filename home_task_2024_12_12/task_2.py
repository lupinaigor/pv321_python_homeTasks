# Завдання 2
# Додайте до першого завдання можливість передавати
# межі діапазону для пошуку усіх простих чисел.

import time

# Декоратор для вимірювання часу виконання

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()  # Початковий час
        result = func(*args, **kwargs)  # Виконуємо декоровану функцію
        t2 = time.time()  # Кінцевий час
        t = t2 - t1  # Розраховуємо час виконання
        # print(f"Час виконання: {int(t)} секунд.")
        print(f"Час виконання: {t:.5f} секунд.")
    return wrapper

# Функція для пошуку простих чисел
@timing_decorator
def prime_numbers(start, end):
    primes = []
    for n in range(start, end + 1):
        if n < 2:
            continue  # Пропускаємо числа менші за 2
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

# Виклик функції з переданими межами
start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

primes = prime_numbers(start_range, end_range)
print(f"Прості числа в діапазоні від {start_range} до {end_range}: {primes}")