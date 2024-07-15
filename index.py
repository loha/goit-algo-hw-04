import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Використовуємо вбудоване сортування Python (Timsort)
def timsort(arr):
    arr.sort()

# Функція для заміру часу виконання
def measure_time(sort_func, data):
    def wrapper():
        return sort_func(data.copy())
    return wrapper

# Генерація випадкового масиву
data_size = 10000
random_data = [random.randint(0, 100000) for _ in range(data_size)]

# Заміри часу виконання алгоритмів
time_merge_sort = timeit.timeit(measure_time(merge_sort, random_data), number=10)
time_insertion_sort = timeit.timeit(measure_time(insertion_sort, random_data), number=10)
time_timsort = timeit.timeit(measure_time(timsort, random_data), number=10)

print(f"Merge Sort: {time_merge_sort:.6f} seconds")
print(f"Insertion Sort: {time_insertion_sort:.6f} seconds")
print(f"Timsort: {time_timsort:.6f} seconds")
