# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'default_select_parameter'
__date__ = '10/21/16'
__copyright__ = 'ismail@kartoza.com'
__doc__ = ''


from parameter_exceptions import ValueNotAllowedException
from generic_parameter import GenericParameter


class DefaultSelectParameter(GenericParameter):
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
        self.expected_type = tuple


        self._choice_list = None
        self._choice_value = None

        self._default_value_list = None
        self._default_value = None

    @property
    def choice_value(self):
        """Property for choice_value"""
        return self._choice_value

    @choice_value.setter
    def choice_value(self, choice_value_input):
        """Setter for choice_value.

        :param choice_value_input: The choice value.
        :type choice_value_input: object
        """
        if choice_value_input in self.choice_list:
            self._choice_value = choice_value_input
        else:
            raise ValueNotAllowedException

    @property
    def choice_list(self):
        """Stores the list of options the value can take"""
        return self._choice_list

    @choice_list.setter
    def choice_list(self, value):
        # the options type must be the same as the value type
        self._choice_list = value

    @property
    def default_value(self):
        """Property for default_value"""
        return self._default_value

    @default_value.setter
    def default_value(self, default_value_input):
        """Setter for default_value.

        :param default_value_input: The default value.
        :type default_value_input: object
        """
        if default_value_input in self.default_value_list:
            self._default_value = default_value_input
        else:
            raise ValueNotAllowedException

    @property
    def default_value_list(self):
        """Stores the list of default value can take"""
        return self._default_value_list

    @default_value_list.setter
    def default_value_list(self, value):
        # the options type must be the same as the value type
        self._default_value_list = value


    @property
    def value(self):
        """Return the value of the parameter"""
        return self.choice_value, self.default_value

    @value.setter
    def value(self, value):
        """Setter fot the value

        :param value: The value as tuple of two.
        :type value: tuple
        """
        if isinstance(value, tuple) and len(value) == 2:
            self.choice_value = value[0]
            self.default_value = value[1]
        else:
            raise ValueNotAllowedException
