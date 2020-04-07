import unittest


class GenericValidator(unittest.TestCase):

    def verify_two_values_are_equal(self, actual, expected):
        self.assertEqual(actual, expected, "actual result {0} is not matched with expected result {1}")

    def verify_value_is_not_null(self, actual_result):
        self.assertIsNotNone(actual_result, "temperature value {0} is null".format(actual_result))

