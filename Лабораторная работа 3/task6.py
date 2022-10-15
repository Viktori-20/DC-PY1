list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_element = max(list_numbers)
# максимальный элемент
index = list_numbers.index(max_element)
# индекс максимального элемента
list_numbers[-1], list_numbers[index] = max_element, list_numbers[-1]
# замена последнего и максимального элементов

print(list_numbers)
