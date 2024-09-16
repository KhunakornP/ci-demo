"""Test cases for the statistic.py file"""
from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):
    """Test cases for functions in statistics.py ."""

    def test_variance_typical_values(self):
        """Test the variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """The variance should work with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_of_nothing(self):
        """Variance should raise an exception on empty list"""
        with self.assertRaises(ValueError):
            variance([])

    def test_stdev(self):
        """Test the standard variance."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average_int(self):
        """Test the average of a set of ints"""
        self.assertEqual(2, average([2, 2, 2, 2, 2, 2, 2, 2]))
        self.assertEqual(5, average([1, 3, 5, 7, 9]))
        self.assertEqual(0, average([0]))

    def test_average_float(self):
        """Test the average with floats"""
        self.assertEqual(2, average([2.0, 2.0, 2.0, 2.0,
                                     2.0, 2.0, 2.0, 2.0]))
        self.assertEqual(2, average([2.0, 2.0, 2.0, 2.0,
                                     2, 2, 2, 2]))
        self.assertAlmostEqual(2.2, average([1.1, 3.3]))
        self.assertAlmostEqual(2.1, average([0.1, 4.1]))

    def test_average_of_no_values(self):
        """Test if the average function throws an exception on empty list"""
        with self.assertRaises(ValueError):
            average([])
