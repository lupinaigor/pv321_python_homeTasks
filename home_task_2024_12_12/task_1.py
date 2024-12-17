# Завдання 1

# Створіть функцію, яка повертає список з усіма простими числами від 0 до 1000.

def prime_numbers():
    primes = []
    for n in range(2, 1001):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

print(prime_numbers())

# Використовуючи механізм декораторів, підрахуйте, скільки секунд знадобилося для обчислення усіх простих чисел.
# Виведіть на екран кількість секунд та прості числа.


import time
# Декоратор
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()  # Початковий час
        result = func(*args, **kwargs)  # Виконуємо декоровану функцію
        t2 = time.time()  # Кінцевий час
        t = t2 - t1  # Розраховуємо час виконання
        # print(f"Час виконання: {int(t)} секунд.")
        print(f"Час виконання: {t:.5f} секунд.")
        return result
    return wrapper

# Огортання функції декоратором
@timing_decorator
def prime_numbers():
    primes = []
    for n in range(2, 1001):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

# Викликаємо функцію та виводимо результат
primes = prime_numbers()
print(f"Прості числа: {primes}")