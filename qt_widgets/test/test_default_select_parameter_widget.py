# coding=utf-8
"""Test class for default_select_parameter_widget."""


import unittest

from PyQt4.QtGui import QApplication

from default_select_parameter import DefaultSelectParameter


from qt_widgets.default_select_parameter_widget import (
    DefaultSelectParameterWidget)


class TestSelectParameterWidget(unittest.TestCase):
    """Test for SelectParameterWidget"""
    application = QApplication([])

    def test_init(self):
        default_select_parameter = DefaultSelectParameter()
        default_select_parameter.name = 'Select Affected Field'
        default_select_parameter.is_required = True
        default_select_parameter.help_text = 'Column used for affected field'
        default_select_parameter.description = (
            'Column used for affected field in the vector')
        default_select_parameter.element_type = str
        default_select_parameter.options_list = [
            'FLOODPRONE', 'affected', 'floodprone', 'yes/no',
            '\xddounicode test']

        widget = DefaultSelectParameterWidget(default_select_parameter)

        expected_value = default_select_parameter.value
        real_value = widget.get_parameter().value
        self.assertEqual(expected_value, real_value)

    def test_set_choice(self):
        """Test for set_choice method."""
        default_select_parameter = DefaultSelectParameter()
        default_select_parameter.name = 'Select Affected Field'
        default_select_parameter.is_required = True
        default_select_parameter.help_text = 'Column used for affected field'
        default_select_parameter.description = (
            'Column used for affected field in the vector')
        default_select_parameter.element_type = str
        default_select_parameter.choice_list = [
            'FLOODPRONE', 'affected', 'floodprone', 'yes/no',
            '\xddounicode test']
        default_select_parameter.default_value_list = [1, 2, 3, 4]

        default_select_parameter.value = ('affected', 1)

        widget = DefaultSelectParameterWidget(default_select_parameter)

        expected = ('floodprone', 2)
        widget.set_choice(expected[0])
        widget.set_default(expected[1])
        real_value = widget.get_parameter().value
        self.assertEqual(expected, real_value)
