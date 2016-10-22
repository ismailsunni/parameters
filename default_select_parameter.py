# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'default_select_parameter'
__date__ = '10/21/16'
__copyright__ = 'ismail@kartoza.com'
__doc__ = ''

from parameter_exceptions import ValueNotAllowedException
from select_parameter import SelectParameter


class DefaultSelectParameter(SelectParameter):
    """Parameter that represent a select parameter with default."""

    def __init__(self, guid=None):
        """Constructor.

        :param guid: Optional unique identifier for this parameter.
            If none is specified one will be generated using python
            hash. This guid will be used when storing parameters in
            the registry.
        :type guid: str
        """

        super(DefaultSelectParameter, self).__init__(guid)
        self.expected_type = object
        self.element_type = object

        # Store option for default labels
        self._default_labels = None
        # Store option for default values
        self._default_values = None
        # Store selected default value
        self._default_value = None

    @property
    def default_labels(self):
        """Property for default_labels"""
        return self._default_labels

    @default_labels.setter
    def default_labels(self, default_labels):
        """Setter for default_labels.

        :param default_labels: The default_labels values.
        :type default_labels: list
        """
        self._default_labels = default_labels

    @property
    def default_values(self):
        """Property for default_values"""
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Setter for default_values.

        :param default_values: The default values.
        :type default_values: list
        """
        self._default_values = default_values

    @property
    def default_value(self):
        """Property for default_value"""
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Setter for default_value.

        :param default_value: The default value.
        :type default_value: object
        """
        # if default_value not in self.defaults:
        #     raise ValueNotAllowedException

        self._default_value = default_value
