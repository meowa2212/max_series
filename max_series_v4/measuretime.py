'''
Moduł pomiaru czasu
Wojciech Gorzynski 04.11.2023
v1.0
'''
from time import perf_counter as pc

# funkcja zwracająca czasy
def measuretime(func):
    def wrapper(*args, **kwargs):
        start = pc()
        result = func(*args, **kwargs)
        end = pc()
        se_time = end-start
        return result, se_time
    return wrapper

# funkcja wyświetlająca czas
def measuretime_print(func):
    def wrapper(*args, **kwargs):
        start = pc()
        result = func(*args, **kwargs)
        end = pc()
        se_time = end-start
        print(f"Czas Wykonanie Funkcji {func.__name__} : {end-start} sekund. ")
    return wrapper