/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.1
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Threading;
using RestSharp;
using TorizonRestAPI.Client;
using TorizonRestAPI.Model;

namespace TorizonRestAPI.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IPlatformsApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Get compatible devices
        /// </summary>
        /// <remarks>
        /// Return a list of devices that are compatible with the platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>List&lt;TargetDevice&gt;</returns>
        List<TargetDevice> PlatformCompatibledevicesGet (string platformId);

        /// <summary>
        /// Get compatible devices
        /// </summary>
        /// <remarks>
        /// Return a list of devices that are compatible with the platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>ApiResponse of List&lt;TargetDevice&gt;</returns>
        ApiResponse<List<TargetDevice>> PlatformCompatibledevicesGetWithHttpInfo (string platformId);
        /// <summary>
        /// Get detailed information about a platform
        /// </summary>
        /// <remarks>
        /// Return data about a specific platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>Platform</returns>
        Platform PlatformGet (string platformId);

        /// <summary>
        /// Get detailed information about a platform
        /// </summary>
        /// <remarks>
        /// Return data about a specific platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>ApiResponse of Platform</returns>
        ApiResponse<Platform> PlatformGetWithHttpInfo (string platformId);
        /// <summary>
        /// Get all platforms
        /// </summary>
        /// <remarks>
        /// Return all configured platforms
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <returns>List&lt;Platform&gt;</returns>
        List<Platform> PlatformsGet (string runtime = default(string));

        /// <summary>
        /// Get all platforms
        /// </summary>
        /// <remarks>
        /// Return all configured platforms
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <returns>ApiResponse of List&lt;Platform&gt;</returns>
        ApiResponse<List<Platform>> PlatformsGetWithHttpInfo (string runtime = default(string));
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// Get compatible devices
        /// </summary>
        /// <remarks>
        /// Return a list of devices that are compatible with the platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;TargetDevice&gt;</returns>
        System.Threading.Tasks.Task<List<TargetDevice>> PlatformCompatibledevicesGetAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Get compatible devices
        /// </summary>
        /// <remarks>
        /// Return a list of devices that are compatible with the platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;TargetDevice&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<TargetDevice>>> PlatformCompatibledevicesGetWithHttpInfoAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken));
        /// <summary>
        /// Get detailed information about a platform
        /// </summary>
        /// <remarks>
        /// Return data about a specific platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Platform</returns>
        System.Threading.Tasks.Task<Platform> PlatformGetAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Get detailed information about a platform
        /// </summary>
        /// <remarks>
        /// Return data about a specific platform
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Platform)</returns>
        System.Threading.Tasks.Task<ApiResponse<Platform>> PlatformGetWithHttpInfoAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken));
        /// <summary>
        /// Get all platforms
        /// </summary>
        /// <remarks>
        /// Return all configured platforms
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;Platform&gt;</returns>
        System.Threading.Tasks.Task<List<Platform>> PlatformsGetAsync (string runtime = default(string), CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Get all platforms
        /// </summary>
        /// <remarks>
        /// Return all configured platforms
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;Platform&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<Platform>>> PlatformsGetWithHttpInfoAsync (string runtime = default(string), CancellationToken cancellationToken = default(CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class PlatformsApi : IPlatformsApi
    {
        private TorizonRestAPI.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="PlatformsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public PlatformsApi(String basePath)
        {
            this.Configuration = new TorizonRestAPI.Client.Configuration { BasePath = basePath };

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PlatformsApi"/> class
        /// </summary>
        /// <returns></returns>
        public PlatformsApi()
        {
            this.Configuration = TorizonRestAPI.Client.Configuration.Default;

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PlatformsApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public PlatformsApi(TorizonRestAPI.Client.Configuration configuration = null)
        {
            if (configuration == null) // use the default one in Configuration
                this.Configuration = TorizonRestAPI.Client.Configuration.Default;
            else
                this.Configuration = configuration;

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.ApiClient.RestClient.BaseUrl.ToString();
        }

        /// <summary>
        /// Sets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        [Obsolete("SetBasePath is deprecated, please do 'Configuration.ApiClient = new ApiClient(\"http://new-path\")' instead.")]
        public void SetBasePath(String basePath)
        {
            // do nothing
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public TorizonRestAPI.Client.Configuration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public TorizonRestAPI.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Gets the default header.
        /// </summary>
        /// <returns>Dictionary of HTTP header</returns>
        [Obsolete("DefaultHeader is deprecated, please use Configuration.DefaultHeader instead.")]
        public IDictionary<String, String> DefaultHeader()
        {
            return new ReadOnlyDictionary<string, string>(this.Configuration.DefaultHeader);
        }

        /// <summary>
        /// Add default header.
        /// </summary>
        /// <param name="key">Header field name.</param>
        /// <param name="value">Header field value.</param>
        /// <returns></returns>
        [Obsolete("AddDefaultHeader is deprecated, please use Configuration.AddDefaultHeader instead.")]
        public void AddDefaultHeader(string key, string value)
        {
            this.Configuration.AddDefaultHeader(key, value);
        }

        /// <summary>
        /// Get compatible devices Return a list of devices that are compatible with the platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>List&lt;TargetDevice&gt;</returns>
        public List<TargetDevice> PlatformCompatibledevicesGet (string platformId)
        {
             ApiResponse<List<TargetDevice>> localVarResponse = PlatformCompatibledevicesGetWithHttpInfo(platformId);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get compatible devices Return a list of devices that are compatible with the platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>ApiResponse of List&lt;TargetDevice&gt;</returns>
        public ApiResponse<List<TargetDevice>> PlatformCompatibledevicesGetWithHttpInfo (string platformId)
        {
            // verify the required parameter 'platformId' is set
            if (platformId == null)
                throw new ApiException(400, "Missing required parameter 'platformId' when calling PlatformsApi->PlatformCompatibledevicesGet");

            var localVarPath = "/platforms/{platform_id}/compatibledevices";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (platformId != null) localVarPathParams.Add("platform_id", this.Configuration.ApiClient.ParameterToString(platformId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformCompatibledevicesGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<TargetDevice>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<TargetDevice>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<TargetDevice>)));
        }

        /// <summary>
        /// Get compatible devices Return a list of devices that are compatible with the platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;TargetDevice&gt;</returns>
        public async System.Threading.Tasks.Task<List<TargetDevice>> PlatformCompatibledevicesGetAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<List<TargetDevice>> localVarResponse = await PlatformCompatibledevicesGetWithHttpInfoAsync(platformId, cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get compatible devices Return a list of devices that are compatible with the platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;TargetDevice&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<TargetDevice>>> PlatformCompatibledevicesGetWithHttpInfoAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken))
        {
            // verify the required parameter 'platformId' is set
            if (platformId == null)
                throw new ApiException(400, "Missing required parameter 'platformId' when calling PlatformsApi->PlatformCompatibledevicesGet");

            var localVarPath = "/platforms/{platform_id}/compatibledevices";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (platformId != null) localVarPathParams.Add("platform_id", this.Configuration.ApiClient.ParameterToString(platformId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformCompatibledevicesGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<TargetDevice>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<TargetDevice>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<TargetDevice>)));
        }

        /// <summary>
        /// Get detailed information about a platform Return data about a specific platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>Platform</returns>
        public Platform PlatformGet (string platformId)
        {
             ApiResponse<Platform> localVarResponse = PlatformGetWithHttpInfo(platformId);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get detailed information about a platform Return data about a specific platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <returns>ApiResponse of Platform</returns>
        public ApiResponse<Platform> PlatformGetWithHttpInfo (string platformId)
        {
            // verify the required parameter 'platformId' is set
            if (platformId == null)
                throw new ApiException(400, "Missing required parameter 'platformId' when calling PlatformsApi->PlatformGet");

            var localVarPath = "/platforms/{platform_id}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (platformId != null) localVarPathParams.Add("platform_id", this.Configuration.ApiClient.ParameterToString(platformId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Platform>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Platform) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Platform)));
        }

        /// <summary>
        /// Get detailed information about a platform Return data about a specific platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Platform</returns>
        public async System.Threading.Tasks.Task<Platform> PlatformGetAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<Platform> localVarResponse = await PlatformGetWithHttpInfoAsync(platformId, cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get detailed information about a platform Return data about a specific platform
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="platformId">Id of a platform formatted as name_version</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Platform)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Platform>> PlatformGetWithHttpInfoAsync (string platformId, CancellationToken cancellationToken = default(CancellationToken))
        {
            // verify the required parameter 'platformId' is set
            if (platformId == null)
                throw new ApiException(400, "Missing required parameter 'platformId' when calling PlatformsApi->PlatformGet");

            var localVarPath = "/platforms/{platform_id}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (platformId != null) localVarPathParams.Add("platform_id", this.Configuration.ApiClient.ParameterToString(platformId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Platform>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Platform) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Platform)));
        }

        /// <summary>
        /// Get all platforms Return all configured platforms
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <returns>List&lt;Platform&gt;</returns>
        public List<Platform> PlatformsGet (string runtime = default(string))
        {
             ApiResponse<List<Platform>> localVarResponse = PlatformsGetWithHttpInfo(runtime);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get all platforms Return all configured platforms
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <returns>ApiResponse of List&lt;Platform&gt;</returns>
        public ApiResponse<List<Platform>> PlatformsGetWithHttpInfo (string runtime = default(string))
        {

            var localVarPath = "/platforms";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (runtime != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "runtime", runtime)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformsGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Platform>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Platform>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Platform>)));
        }

        /// <summary>
        /// Get all platforms Return all configured platforms
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;Platform&gt;</returns>
        public async System.Threading.Tasks.Task<List<Platform>> PlatformsGetAsync (string runtime = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<List<Platform>> localVarResponse = await PlatformsGetWithHttpInfoAsync(runtime, cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get all platforms Return all configured platforms
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="runtime"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;Platform&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<Platform>>> PlatformsGetWithHttpInfoAsync (string runtime = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {

            var localVarPath = "/platforms";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (runtime != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "runtime", runtime)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("PlatformsGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Platform>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Platform>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Platform>)));
        }

    }
}
