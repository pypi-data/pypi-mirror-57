# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="editor_api.py">
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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from groupdocs_editor_cloud.auth import Auth
from groupdocs_editor_cloud.api_client import ApiClient
from groupdocs_editor_cloud.api_exception import ApiException
from groupdocs_editor_cloud.configuration import Configuration

class InfoApi(object):
    """
    GroupDocs.Editor Cloud API

    :param configuration: API configuration
    """

    def __init__(self, configuration):
        api_client = ApiClient(configuration)

        self.auth = Auth(configuration, api_client)
        self.api_client = api_client
        self.configuration = configuration

    def close(self):  # noqa: E501
        """
        Closes thread pool. This method should be called when 
        methods are executed asynchronously (is_async=True is passed as parameter)
        and this instance of InfoApi is not going to be used any more.
        """
        if self.api_client is not None:
            if(self.api_client.pool is not None):
                self.api_client.pool.close()
                self.api_client.pool.join()
                self.api_client.pool = None

    @classmethod
    def from_keys(cls, app_sid, app_key):
        """
        Initializes new instance of InfoApi with API keys

        :param app_sid Application identifier (App SID)
        :param app_key Application private key (App Key)
        """
        configuration = Configuration(app_sid, app_key)
        return InfoApi(configuration)

    @classmethod
    def from_config(cls, configuration):
        """
        Initializes new instance of InfoApi with configuration options

        :param configuration API configuration
        """
        return InfoApi(configuration)

    def get_info(self, request,**kwargs):  # noqa: E501
        """Retrieve information about document pages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param FileInfo file_info: File Info (required)
        :return: InfoResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._get_info_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._get_info_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _get_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieve information about document pages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param GetInfoRequest request object with parameters
        :return: InfoResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_info' is set
        if request.file_info is None:
            raise ValueError("Missing the required parameter `file_info` when calling `get_info`")  # noqa: E501

        collection_formats = {}
        path = '/editor/info'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.file_info is not None:
            body_params = request.file_info
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'InfoResult',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def get_supported_file_formats(self, **kwargs):  # noqa: E501
        """List supported file formats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: FormatsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._get_supported_file_formats_with_http_info(**kwargs)  # noqa: E501
        
        (data) = self._get_supported_file_formats_with_http_info(**kwargs)  # noqa: E501
        return data

    def _get_supported_file_formats_with_http_info(self, **kwargs):  # noqa: E501
        """List supported file formats  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        
        :return: FormatsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_file_formats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/editor/formats'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'FormatsResult',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return str
        else:
            return s[0].lower() + s[1:]

# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="get_info_request.py">
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
# --------------------------------------------------------------------------------

class GetInfoRequest(object):
    """
    Request model for get_info operation.
    :param file_info File Info
    """

    def __init__(self, file_info):
        """Initializes new instance of GetInfoRequest."""  # noqa: E501
        self.file_info = file_info
