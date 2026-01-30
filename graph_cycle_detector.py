"""
Модуль для определения наличия циклов в ориентированном графе.
Использует алгоритм поиска в глубину (DFS) с отслеживанием состояний вершин.
"""

from enum import Enum
from typing import Dict, List


class VertexState(Enum):
    """
    Перечисление состояний вершин при обходе графа.
    
    WHITE - вершина не посещена
    GRAY - вершина находится в процессе обработки
    BLACK - вершина полностью обработана
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2


class GraphCycleDetector:
    """
    Класс для определения наличия циклов в ориентированном графе.
    
    Граф представлен в виде списка смежности (словаря),
    где ключ - вершина, значение - список смежных вершин.
    """
    
    def __init__(self, adjacency_list: Dict[int, List[int]]):
        """
        Инициализация детектора циклов.
        
        Args:
            adjacency_list: Список смежности графа в виде словаря.
                           Ключ - номер вершины, значение - список смежных вершин.
        """
        self.graph = adjacency_list
        self.states: Dict[int, VertexState] = {}
        
    def has_cycle(self) -> bool:
        """
        Определяет наличие циклов в графе.
        
        Returns:
            True, если в графе есть хотя бы один цикл, иначе False.
        """
        # Инициализация всех вершин как непосещенных
        self.states = {vertex: VertexState.WHITE for vertex in self.graph}
        
        # Запуск DFS для каждой непосещенной вершины
        for vertex in self.graph:
            if self.states[vertex] == VertexState.WHITE:
                if self._dfs(vertex):
                    return True
        
        return False
    
    def _dfs(self, vertex: int) -> bool:
        """
        Рекурсивный поиск в глубину для обнаружения циклов.
        
        Args:
            vertex: Номер текущей вершины.
            
        Returns:
            True, если обнаружен цикл, иначе False.
        """
        # Помечаем вершину как находящуюся в обработке
        self.states[vertex] = VertexState.GRAY
        
        # Обходим всех соседей текущей вершины
        for neighbor in self.graph.get(vertex, []):
            # Если сосед еще не посещен, рекурсивно вызываем DFS
            if self.states.get(neighbor, VertexState.WHITE) == VertexState.WHITE:
                if self._dfs(neighbor):
                    return True
            # Если сосед в процессе обработки - найден цикл (обратное ребро)
            elif self.states.get(neighbor) == VertexState.GRAY:
                return True
        
        # Помечаем вершину как полностью обработанную
        self.states[vertex] = VertexState.BLACK
        return False


def read_graph_from_input() -> Dict[int, List[int]]:
    """
    Считывает граф из стандартного ввода.
    
    Формат ввода:
    - Первая строка: количество вершин n и количество рёбер m
    - Следующие m строк: пары вершин (u, v), обозначающие ребро от u к v
    
    Returns:
        Список смежности графа в виде словаря.
    """
    n, m = map(int, input().split())
    
    # Инициализация списка смежности
    graph = {i: [] for i in range(1, n + 1)}
    
    # Чтение рёбер
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    return graph


def main():
    """
    Главная функция программы.
    Считывает граф и определяет наличие циклов.
    """
    print("Введите количество вершин и рёбер:")
    graph = read_graph_from_input()
    
    detector = GraphCycleDetector(graph)
    
    if detector.has_cycle():
        print("YES")  # В графе есть циклы
    else:
        print("NO")   # В графе нет циклов


if __name__ == "__main__":
    main()
