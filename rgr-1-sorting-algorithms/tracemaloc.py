import random
import tracemalloc
from sorts import Selection_Sort, Bubble_Sort, Quick_Sort, Merge_Sort

def measure_memory_tracemalloc(function, arr):
    """ Функция. которая изменярет пространственную сложность 
    функции bubble_sort"""
    # Создание копии исходного массива. чтобы его изначальная версия осталась в неизменном виде.
    arr_copy = arr.copy()
    # Выполнение самой сортировки.
    tracemalloc.start() # Старт анализа
    sourted_arr = function(arr_copy) #Сама сортировка
    current, pic = tracemalloc.get_traced_memory() # Получение текущего и пикового значения памяти.
    tracemalloc.stop() # Завершения анализа
    #Форматирование даннных
    peak_kb = pic / 1024
    return peak_kb


# Реализация
if __name__ == '__main__':
    test_massive = [random.randint(1,1000) for _ in range(10000)]
    test_bubble = measure_memory_tracemalloc(Bubble_Sort, test_massive)
    test_selection = measure_memory_tracemalloc(Selection_Sort, test_massive)
    test_quick = measure_memory_tracemalloc(Quick_Sort, test_massive)
    test_merge = measure_memory_tracemalloc(Merge_Sort, test_massive)
    print(f'Пузырьковая сортировка {test_bubble:.2f} Кб\nСортировка выбором: {test_selection:.2f} Кб\nБыстрая сортировка: {test_quick:.2f} Кб\nMerge сортировка: {test_merge:.2f} Кб')