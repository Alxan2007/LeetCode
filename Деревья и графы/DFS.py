def find_path(root, target):
    path = []  # Создаем пустой список для хранения пути
    if dfs_find_path(root, target, path):  # Если путь найден
        return path  # Возвращаем найденный путь
    return None  # Если путь не найден, возвращаем None


def dfs_find_path(node, target, path):
    if node is None:  # Базовый случай: если узел пустой
        return False  # Возвращаем False

    path.append(node.value)  # Добавляем значение текущего узла в путь

    if node.value == target:  # Если нашли целевое значение
        return True  # Возвращаем True

    # Рекурсивно проверяем всех детей
    for child in node.children:
        if dfs_find_path(child, target, path):
            return True

    # Если путь не найден, удаляем последний элемент
    path.pop()
    return False
