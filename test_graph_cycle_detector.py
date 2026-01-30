"""
Модульные тесты для класса GraphCycleDetector.
"""

import unittest
from graph_cycle_detector import GraphCycleDetector


class TestGraphCycleDetector(unittest.TestCase):
    """
    Тестовый класс для проверки определения циклов в графе.
    """
    
    def test_simple_cycle(self):
        """Тест: простой цикл из трёх вершин (1 -> 2 -> 3 -> 1)"""
        graph = {
            1: [2],
            2: [3],
            3: [1]
        }
        detector = GraphCycleDetector(graph)
        self.assertTrue(detector.has_cycle())
    
    def test_no_cycle_linear(self):
        """Тест: линейный граф без циклов (1 -> 2 -> 3)"""
        graph = {
            1: [2],
            2: [3],
            3: []
        }
        detector = GraphCycleDetector(graph)
        self.assertFalse(detector.has_cycle())
    
    def test_self_loop(self):
        """Тест: граф с петлей (1 -> 1)"""
        graph = {
            1: [1],
            2: []
        }
        detector = GraphCycleDetector(graph)
        self.assertTrue(detector.has_cycle())
    
    def test_disconnected_with_cycle(self):
        """Тест: несвязный граф с циклом в одной компоненте"""
        graph = {
            1: [2],
            2: [1],  # Цикл между 1 и 2
            3: [4],  # Отдельная компонента без цикла
            4: []
        }
        detector = GraphCycleDetector(graph)
        self.assertTrue(detector.has_cycle())
    
    def test_complex_graph_with_cycle(self):
        """Тест: сложный граф с несколькими путями и циклом"""
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: [5],
            5: [2]  # Цикл: 2 -> 4 -> 5 -> 2
        }
        detector = GraphCycleDetector(graph)
        self.assertTrue(detector.has_cycle())
    
    def test_dag(self):
        """Тест: направленный ациклический граф (DAG)"""
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: [5],
            5: []
        }
        detector = GraphCycleDetector(graph)
        self.assertFalse(detector.has_cycle())
    
    def test_empty_graph(self):
        """Тест: пустой граф"""
        graph = {}
        detector = GraphCycleDetector(graph)
        self.assertFalse(detector.has_cycle())
    
    def test_single_vertex_no_edges(self):
        """Тест: одна вершина без рёбер"""
        graph = {1: []}
        detector = GraphCycleDetector(graph)
        self.assertFalse(detector.has_cycle())


if __name__ == '__main__':
    unittest.main()
