"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.1.6
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from moses_client.api_client import ApiClient, Endpoint as _Endpoint
from moses_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from moses_client.model.error_info import ErrorInfo
from moses_client.model.eula import Eula


class EulasApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.eula_get_endpoint = _Endpoint(
            settings={
                'response_type': (Eula,),
                'auth': [],
                'endpoint_path': '/eulas/{eula_id}',
                'operation_id': 'eula_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'eula_id',
                ],
                'required': [
                    'eula_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'eula_id',
                ]
            },
            root_map={
                'validations': {
                    ('eula_id',): {

                        'regex': {
                            'pattern': r'^[-0-9a-zA-Z.]*$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'eula_id':
                        (str,),
                },
                'attribute_map': {
                    'eula_id': 'eula_id',
                },
                'location_map': {
                    'eula_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.eula_modify_endpoint = _Endpoint(
            settings={
                'response_type': (Eula,),
                'auth': [],
                'endpoint_path': '/eulas/{eula_id}',
                'operation_id': 'eula_modify',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'eula_id',
                    'e',
                ],
                'required': [
                    'eula_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'eula_id',
                ]
            },
            root_map={
                'validations': {
                    ('eula_id',): {

                        'regex': {
                            'pattern': r'^[-0-9a-zA-Z.]*$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'eula_id':
                        (str,),
                    'e':
                        (Eula,),
                },
                'attribute_map': {
                    'eula_id': 'eula_id',
                },
                'location_map': {
                    'eula_id': 'path',
                    'e': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.eulas_get_endpoint = _Endpoint(
            settings={
                'response_type': ([Eula],),
                'auth': [],
                'endpoint_path': '/eulas',
                'operation_id': 'eulas_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def eula_get(
        self,
        eula_id,
        **kwargs
    ):
        """Get detail about an eula  # noqa: E501

        Return detailed information about a specific eula  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.eula_get(eula_id, async_req=True)
        >>> result = thread.get()

        Args:
            eula_id (str): Id of an Eula

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Eula
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['eula_id'] = \
            eula_id
        return self.eula_get_endpoint.call_with_http_info(**kwargs)

    def eula_modify(
        self,
        eula_id,
        **kwargs
    ):
        """Change eula properties  # noqa: E501

        Set eula as visualized and/or accepted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.eula_modify(eula_id, async_req=True)
        >>> result = thread.get()

        Args:
            eula_id (str): Id of an Eula

        Keyword Args:
            e (Eula): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Eula
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['eula_id'] = \
            eula_id
        return self.eula_modify_endpoint.call_with_http_info(**kwargs)

    def eulas_get(
        self,
        **kwargs
    ):
        """Get all eulas  # noqa: E501

        Returns information about all eulas required to run different platforms on the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.eulas_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [Eula]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.eulas_get_endpoint.call_with_http_info(**kwargs)

