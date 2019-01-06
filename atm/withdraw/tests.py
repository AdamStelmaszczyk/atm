from django.test import TestCase

from atm.withdraw.withdraw import calculate_change, NoteUnavailableException, unroll_change


class CalculateChangeTest(TestCase):
    def test_calculate_change(self):
        assert calculate_change(0) == [0, 0, 0, 0]
        assert calculate_change(40) == [0, 0, 2, 0]
        assert calculate_change(80) == [0, 1, 1, 1]
        assert calculate_change(280) == [2, 1, 1, 1]
        assert calculate_change(990) == [9, 1, 2, 0]
        self.assertRaises(AssertionError, calculate_change, -1)
        self.assertRaises(AssertionError, calculate_change, 10.0)
        self.assertRaises(AssertionError, calculate_change, '10')
        self.assertRaises(NoteUnavailableException, calculate_change, 5)

    def test_unroll_change(self):
        assert unroll_change([0, 0, 0, 0]) == []
        assert unroll_change([1, 0, 0, 0]) == [100]
        assert unroll_change([2, 0, 0, 0]) == [100, 100]
        assert unroll_change([2, 3, 0, 0]) == [100, 100, 50, 50, 50]
        assert unroll_change([2, 3, 0, 1]) == [100, 100, 50, 50, 50, 10]
        assert unroll_change([0, 0, 2, 1]) == [20, 20, 10]
        self.assertRaises(AssertionError, unroll_change, [0, 0, 0])