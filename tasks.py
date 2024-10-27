import heapq


# Основне завдання: Мінімізація витрат на об'єднання кабелів
def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Вибираємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх і додаємо витрати
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))


# Опціональне завдання: Злиття k відсортованих списків у один

def merge_k_lists(lists):
    min_heap = []

    # Додаємо всі елементи з усіх списків у мінімальну купу
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(min_heap, (sorted_list[0], i, 0))

    merged_list = []

    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)

        # Якщо є ще елементи в цьому списку, додаємо їх у купу
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
