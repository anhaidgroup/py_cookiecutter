import unittest

from nose.tools import assert_equal


class Module1Command1(unittest.TestCase):
	def test_command1(self):
		assert_equal(1, 1)
