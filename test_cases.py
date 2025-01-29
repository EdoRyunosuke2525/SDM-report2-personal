#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertEqual(calc(1, 1), 1)  # 最小境界値
        self.assertEqual(calc(999, 999), 998001)  # 最大境界値
        self.assertEqual(calc(500, 500), 250000)  # 中央値

    def test_invalid_inputs(self):
        self.assertEqual(calc(0, 500), -1)  # 境界値以下
        self.assertEqual(calc(1000, 500), -1)  # 境界値以上
        self.assertEqual(calc(500, 0), -1)  # 境界値以下
        self.assertEqual(calc(500, 1000), -1)  # 境界値以上
        self.assertEqual(calc(-1, 500), -1)  # 負の数
        self.assertEqual(calc(500, -1), -1)  # 負の数
        self.assertEqual(calc("a", 500), -1)  # 文字列
        self.assertEqual(calc(500, "b"), -1)  # 文字列
        self.assertEqual(calc(0.5, 500), -1)  # 小数
        self.assertEqual(calc(500, 0.9), -1)  # 小数
