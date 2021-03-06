# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.14
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


class ProgressApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def progress_create(self, **kwargs):  # noqa: E501
        """create a progress ID  # noqa: E501

        creates a progress object that could be used to monitor and abort operations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_create(async_req=True)
        >>> result = thread.get()

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
        :rtype: Progress
        """
        kwargs['_return_http_data_only'] = True
        return self.progress_create_with_http_info(**kwargs)  # noqa: E501

    def progress_create_with_http_info(self, **kwargs):  # noqa: E501
        """create a progress ID  # noqa: E501

        creates a progress object that could be used to monitor and abort operations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_create_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(Progress, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
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
                    " to method progress_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            200: "Progress",
            500: "ErrorInfo",
        }

        return self.api_client.call_api(
            '/progress/create', 'GET',
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

    def progress_delete(self, **kwargs):  # noqa: E501
        """releases progress ID  # noqa: E501

        if delete is called when the operation is still pending, it will try to abort it  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_delete(async_req=True)
        >>> result = thread.get()

        :param progress_id: Id of a progress cookie (uuid)
        :type progress_id: str
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.progress_delete_with_http_info(**kwargs)  # noqa: E501

    def progress_delete_with_http_info(self, **kwargs):  # noqa: E501
        """releases progress ID  # noqa: E501

        if delete is called when the operation is still pending, it will try to abort it  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param progress_id: Id of a progress cookie (uuid)
        :type progress_id: str
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'progress_id'
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
                    " to method progress_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'progress_id' in local_var_params and not re.search(r'^$|[0-9,a-f,A-F]{8}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{12}$', local_var_params['progress_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `progress_id` when calling `progress_delete`, must conform to the pattern `/^$|[0-9,a-f,A-F]{8}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'progress_id' in local_var_params and local_var_params['progress_id'] is not None:  # noqa: E501
            query_params.append(('progress_id', local_var_params['progress_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/progress/delete', 'GET',
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

    def progress_status(self, **kwargs):  # noqa: E501
        """retrieves status of an operation  # noqa: E501

        return status and messages, it's blocking until status changes or the operation is completed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_status(async_req=True)
        >>> result = thread.get()

        :param progress_id: Id of a progress cookie (uuid)
        :type progress_id: str
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
        :rtype: Progress
        """
        kwargs['_return_http_data_only'] = True
        return self.progress_status_with_http_info(**kwargs)  # noqa: E501

    def progress_status_with_http_info(self, **kwargs):  # noqa: E501
        """retrieves status of an operation  # noqa: E501

        return status and messages, it's blocking until status changes or the operation is completed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.progress_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param progress_id: Id of a progress cookie (uuid)
        :type progress_id: str
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
        :rtype: tuple(Progress, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'progress_id'
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
                    " to method progress_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'progress_id' in local_var_params and not re.search(r'^$|[0-9,a-f,A-F]{8}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{12}$', local_var_params['progress_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `progress_id` when calling `progress_status`, must conform to the pattern `/^$|[0-9,a-f,A-F]{8}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{4}-[0-9,a-f,A-F]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'progress_id' in local_var_params and local_var_params['progress_id'] is not None:  # noqa: E501
            query_params.append(('progress_id', local_var_params['progress_id']))  # noqa: E501

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
            200: "Progress",
            404: None,
            500: "ErrorInfo",
        }

        return self.api_client.call_api(
            '/progress/status', 'GET',
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
