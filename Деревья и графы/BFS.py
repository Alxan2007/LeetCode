from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # Очередь с начальным узлом и путем к нему
    visited = set()  # Множество посещенных узлов

    while queue:
        (node, path) = queue.popleft()  # Извлекаем узел и текущий путь

        if node in visited:
            continue  # Пропускаем уже посещенные узлы

        visited.add(node)  # Добавляем в посещенные

        for neighbor in graph.nodes[node]:  # Перебираем соседей
            if neighbor == end:  # Если нашли целевой узел
                return path + [end]  # Возвращаем полный путь
            else:
                queue.append((neighbor, path + [neighbor]))  # Добавляем в очередь

    return None  # Если путь не найден
