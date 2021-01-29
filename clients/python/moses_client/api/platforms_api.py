# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from moses_client.api_client import ApiClient
from moses_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlatformsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def platform_compatibledevices_get(self, platform_id, **kwargs):  # noqa: E501
        """Get compatible devices  # noqa: E501

        Return a list of devices that are compatible with the platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platform_compatibledevices_get(platform_id, async_req=True)
        >>> result = thread.get()

        :param platform_id: Id of a platform formatted as name_version (required)
        :type platform_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[TargetDevice]
        """
        kwargs['_return_http_data_only'] = True
        return self.platform_compatibledevices_get_with_http_info(platform_id, **kwargs)  # noqa: E501

    def platform_compatibledevices_get_with_http_info(self, platform_id, **kwargs):  # noqa: E501
        """Get compatible devices  # noqa: E501

        Return a list of devices that are compatible with the platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platform_compatibledevices_get_with_http_info(platform_id, async_req=True)
        >>> result = thread.get()

        :param platform_id: Id of a platform formatted as name_version (required)
        :type platform_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[TargetDevice], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'platform_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method platform_compatibledevices_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'platform_id' is set
        if self.api_client.client_side_validation and ('platform_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['platform_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `platform_id` when calling `platform_compatibledevices_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'platform_id' in local_var_params and not re.search(r'^[-0-9a-zA-Z.]*_[-0-9a-zA-Z.]*$', local_var_params['platform_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `platform_id` when calling `platform_compatibledevices_get`, must conform to the pattern `/^[-0-9a-zA-Z.]*_[-0-9a-zA-Z.]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'platform_id' in local_var_params:
            path_params['platform_id'] = local_var_params['platform_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "list[TargetDevice]",
            404: None,
            500: "ErrorInfo",
        }

        return self.api_client.call_api(
            '/platforms/{platform_id}/compatibledevices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def platform_get(self, platform_id, **kwargs):  # noqa: E501
        """Get detailed information about a platform  # noqa: E501

        Return data about a specific platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platform_get(platform_id, async_req=True)
        >>> result = thread.get()

        :param platform_id: Id of a platform formatted as name_version (required)
        :type platform_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Platform
        """
        kwargs['_return_http_data_only'] = True
        return self.platform_get_with_http_info(platform_id, **kwargs)  # noqa: E501

    def platform_get_with_http_info(self, platform_id, **kwargs):  # noqa: E501
        """Get detailed information about a platform  # noqa: E501

        Return data about a specific platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platform_get_with_http_info(platform_id, async_req=True)
        >>> result = thread.get()

        :param platform_id: Id of a platform formatted as name_version (required)
        :type platform_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Platform, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'platform_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method platform_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'platform_id' is set
        if self.api_client.client_side_validation and ('platform_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['platform_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `platform_id` when calling `platform_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'platform_id' in local_var_params and not re.search(r'^[-0-9a-zA-Z.]*_[-0-9a-zA-Z.]*$', local_var_params['platform_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `platform_id` when calling `platform_get`, must conform to the pattern `/^[-0-9a-zA-Z.]*_[-0-9a-zA-Z.]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'platform_id' in local_var_params:
            path_params['platform_id'] = local_var_params['platform_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "Platform",
            404: None,
            500: "ErrorInfo",
        }

        return self.api_client.call_api(
            '/platforms/{platform_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def platforms_get(self, **kwargs):  # noqa: E501
        """Get all platforms  # noqa: E501

        Return all configured platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platforms_get(async_req=True)
        >>> result = thread.get()

        :param runtime:
        :type runtime: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Platform]
        """
        kwargs['_return_http_data_only'] = True
        return self.platforms_get_with_http_info(**kwargs)  # noqa: E501

    def platforms_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all platforms  # noqa: E501

        Return all configured platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.platforms_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param runtime:
        :type runtime: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Platform], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'runtime'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method platforms_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'runtime' in local_var_params and local_var_params['runtime'] is not None:  # noqa: E501
            query_params.append(('runtime', local_var_params['runtime']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "list[Platform]",
            500: "ErrorInfo",
        }

        return self.api_client.call_api(
            '/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
