import unittest
import day1.solution as solution


class TestSolution(unittest.TestCase):
    def test_exercise1(self):
        data = solution.get_data("example_data")
        answer = solution.get_data("example_solution")[0]
        self.assertEqual(answer, solution.exercise1(data))

    def test_exercise2(self):
        data = solution.get_data("example_data")
        answer = solution.get_data("example_solution")[1]
        self.assertEqual(answer, solution.exercise2(data))
