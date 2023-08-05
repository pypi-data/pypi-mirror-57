# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="InfoResult.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six

class InfoResult(object):
    """
    Describes document properties result
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_count': 'int',
        'size': 'int',
        'is_encrypted': 'bool',
        'file_format': 'str',
        'extension': 'str'
    }

    attribute_map = {
        'page_count': 'PageCount',
        'size': 'Size',
        'is_encrypted': 'IsEncrypted',
        'file_format': 'FileFormat',
        'extension': 'Extension'
    }

    def __init__(self, page_count=None, size=None, is_encrypted=None, file_format=None, extension=None, **kwargs):  # noqa: E501
        """Initializes new instance of InfoResult"""  # noqa: E501

        self._page_count = None
        self._size = None
        self._is_encrypted = None
        self._file_format = None
        self._extension = None

        if page_count is not None:
            self.page_count = page_count
        if size is not None:
            self.size = size
        if is_encrypted is not None:
            self.is_encrypted = is_encrypted
        if file_format is not None:
            self.file_format = file_format
        if extension is not None:
            self.extension = extension
    
    @property
    def page_count(self):
        """
        Gets the page_count.  # noqa: E501

        Pages count  # noqa: E501

        :return: The page_count.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count.

        Pages count  # noqa: E501

        :param page_count: The page_count.  # noqa: E501
        :type: int
        """
        if page_count is None:
            raise ValueError("Invalid value for `page_count`, must not be `None`")  # noqa: E501
        self._page_count = page_count
    
    @property
    def size(self):
        """
        Gets the size.  # noqa: E501

        Document size in bytes  # noqa: E501

        :return: The size.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size.

        Document size in bytes  # noqa: E501

        :param size: The size.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        self._size = size
    
    @property
    def is_encrypted(self):
        """
        Gets the is_encrypted.  # noqa: E501

        Indicates whether specific file is encrypted and requires password for opening.  # noqa: E501

        :return: The is_encrypted.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """
        Sets the is_encrypted.

        Indicates whether specific file is encrypted and requires password for opening.  # noqa: E501

        :param is_encrypted: The is_encrypted.  # noqa: E501
        :type: bool
        """
        if is_encrypted is None:
            raise ValueError("Invalid value for `is_encrypted`, must not be `None`")  # noqa: E501
        self._is_encrypted = is_encrypted
    
    @property
    def file_format(self):
        """
        Gets the file_format.  # noqa: E501

        File format  # noqa: E501

        :return: The file_format.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """
        Sets the file_format.

        File format  # noqa: E501

        :param file_format: The file_format.  # noqa: E501
        :type: str
        """
        self._file_format = file_format
    
    @property
    def extension(self):
        """
        Gets the extension.  # noqa: E501

        Document extension  # noqa: E501

        :return: The extension.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension.

        Document extension  # noqa: E501

        :param extension: The extension.  # noqa: E501
        :type: str
        """
        self._extension = extension

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
