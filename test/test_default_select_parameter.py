# coding=utf-8
"""Tests for default select parameter."""

from unittest import TestCase

from default_select_parameter import DefaultSelectParameter
from parameter_exceptions import ValueNotAllowedException

__author__ = 'ismailsunni'
__project_name__ = 'parameters'
__filename__ = 'test_default_select_parameter'
__date__ = '10/22/2016'
__copyright__ = 'imajimatika@gmail.com'

selected = 'one'

choices = ['one', 'two', 'three', 'four', 'five']
defaults = [1, 2, 3]


class TestDefaultSelectParameter(TestCase):
    """Test For Default Select Parameter."""

    def setUp(self):
        self.parameter = DefaultSelectParameter()

        self.parameter._choice_list = choices
        self.parameter.default_value_list = defaults

    def test_set_value(self):
        selected = ('one', 1)
        self.parameter.value = selected
        self.assertEqual(selected, self.parameter.value)

    def test_not_allowed_value(self):
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = ('six', 1)
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = ('one', 4)
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = ('one', 4, 5)
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = ('one')
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = ['one', 4]
