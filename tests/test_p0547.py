import unittest

from src.p0547_friend_circles import find_friends_circle


class TestCases(unittest.TestCase):
    def test_find_friends_circle(self):
        friends_matrix = [[1]]
        self.assertEqual(find_friends_circle(friends_matrix, 0), {0})

        friends_matrix = [
            [1, 0],
            [0, 1],
        ]
        self.assertEqual(find_friends_circle(friends_matrix, 0), {0})
        self.assertEqual(find_friends_circle(friends_matrix, 1), {1})

        friends_matrix = [
            [1, 1],
            [1, 1],
        ]
        self.assertEqual(find_friends_circle(friends_matrix, 0), {0, 1})
        self.assertEqual(find_friends_circle(friends_matrix, 1), {0, 1})

        friends_matrix = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
        ]
        self.assertEqual(find_friends_circle(friends_matrix, 0), {0, 1})
        self.assertEqual(find_friends_circle(friends_matrix, 1), {0, 1})
        self.assertEqual(find_friends_circle(friends_matrix, 2), {2})

        friends_matrix = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
        ]
        self.assertEqual(find_friends_circle(friends_matrix, 0), {0, 1, 2})
        self.assertEqual(find_friends_circle(friends_matrix, 1), {0, 1, 2})
        self.assertEqual(find_friends_circle(friends_matrix, 2), {0, 1, 2})
