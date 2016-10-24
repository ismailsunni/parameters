# coding=utf-8
"""Select Default Parameter Widget."""

__author__ = 'ismailsunni'
__project_name__ = 'parameters'
__filename__ = 'default_select_parameter_widget'
__date__ = '10/22/2016'
__copyright__ = 'imajimatika@gmail.com'

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QComboBox, QRadioButton, QButtonGroup, QWidget, QLineEdit, QLabel)

# from qt_widgets.generic_parameter_widget import GenericParameterWidget
from qt_widgets.select_parameter_widget import SelectParameterWidget

class DefaultSelectParameterWidget(SelectParameterWidget):
    """Widget class for Default Select Parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        :param parameter: A DefaultSelectParameter object.
        :type parameter: DefaultSelectParameter

        """
        super(DefaultSelectParameterWidget, self).__init__(parameter, parent)

        self.default_layout = QHBoxLayout()
        self.radio_button_layout = QHBoxLayout()
        self.radio_button_widget = QWidget()

        self._default_label = QLabel('Use default')

        # Add label for default
        # self.radio_button_layout.addWidget(self._default_label)

        # Create radio button group
        self._default_input_button_group = QButtonGroup()

        for i in range(len(self._parameter.default_labels)):
            if '%s' in self._parameter.default_labels[i]:
                label = (
                    self._parameter.default_labels[i] %
                    self._parameter.default_values[i])
            else:
                label = self._parameter.default_labels[i]

            radio_button = QRadioButton(label)
            self.radio_button_layout.addWidget(radio_button)
            self._default_input_button_group.addButton(radio_button, i)
            if self._parameter.default_value == \
                    self._parameter.default_values[i]:
                radio_button.setChecked(True)

        line_edit = QLineEdit()
        self.radio_button_layout.addWidget(line_edit)

        # Reset the layout
        self._input_layout.setParent(None)
        self._help_layout.setParent(None)

        self._label.setParent(None)
        self._inner_input_layout.setParent(None)

        self._input_layout = QGridLayout()
        self._input_layout.setSpacing(0)

        self._input_layout.addWidget(self._label, 0, 0)
        self._input_layout.addLayout(self._inner_input_layout, 0, 1)
        self._input_layout.addWidget(self._default_label, 1, 0)
        self._input_layout.addLayout(self.radio_button_layout, 1, 1)

        self._main_layout.addLayout(self._input_layout)
        self._main_layout.addLayout(self._help_layout)

    def raise_invalid_type_exception(self):
        message = 'Expecting element type of %s' % (
            self._parameter.element_type.__name__)
        err = ValueError(message)
        return err

    def get_parameter(self):
        """Obtain list parameter object from the current widget state.

        :returns: A DefaultSelectParameter from the current state of widget

        """
        current_index = self._choice_input.currentIndex()
        selected_choice = self._choice_input.itemData(
            current_index, Qt.UserRole)
        if hasattr(selected_choice, 'toPyObject'):
            selected_choice = selected_choice.toPyObject()

        current_index = self._default_input.currentIndex()
        selected_default = self._default_input.itemData(
            current_index, Qt.UserRole)
        if hasattr(selected_default, 'toPyObject'):
            selected_default = selected_default.toPyObject()

        try:
            self._parameter.value = (selected_choice, selected_default)
        except ValueError:
            err = self.raise_invalid_type_exception()
            raise err

        return self._parameter

    def set_choice(self, choice):
        """Set choice value by item's string.

        :param choice: The choice.
        :type choice: str

        :returns: True if success, else False.
        :rtype: bool
        """
        # Find index of choice
        choice_index = self._parameter.choice_list.index(choice)
        if choice_index < 0:
            return False
        else:
            self._choice_input.setCurrentIndex(choice_index)
            return True

    def set_default(self, default):
        """Set default value by item's string.

        :param default: The default.
        :type default: str, int

        :returns: True if success, else False.
        :rtype: bool
        """
        # Find index of choice
        default_index = self._parameter.default_value_list.index(default)
        if default_index < 0:
            return False
        else:
            self._default_input.setCurrentIndex(default_index)
            return True