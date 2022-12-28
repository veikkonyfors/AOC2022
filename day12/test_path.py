from unittest import TestCase
from day12.path import *


class TestPath(TestCase):
    hill = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]

    def test_seek(self):
        path = Path(self.hill)
        path.seek()
        for p in path.all_paths: print("Path:\n", p, " Valid: ", p.valid, " Count: ", p.count)

        self.assertEqual(path.hill_path[0][1], ">")

    def test_find_start(self):
        path = Path(self.hill)
        path.find_start()
        self.assertEqual(path.row, 0)
        self.assertEqual(path.col, 0)
