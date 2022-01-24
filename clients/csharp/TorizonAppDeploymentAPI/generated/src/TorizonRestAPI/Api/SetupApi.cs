/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.5
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
    public interface ISetupApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Enable ARM emulation using binfmt/qemu
        /// </summary>
        /// <remarks>
        /// Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns></returns>
        void SetupEnableemulation (string progressId = default(string));

        /// <summary>
        /// Enable ARM emulation using binfmt/qemu
        /// </summary>
        /// <remarks>
        /// Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        ApiResponse<Object> SetupEnableemulationWithHttpInfo (string progressId = default(string));
        /// <summary>
        /// Pulls container from docker repo
        /// </summary>
        /// <remarks>
        /// Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns></returns>
        void SetupPullcontainers (string progressId = default(string));

        /// <summary>
        /// Pulls container from docker repo
        /// </summary>
        /// <remarks>
        /// Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        ApiResponse<Object> SetupPullcontainersWithHttpInfo (string progressId = default(string));
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// Enable ARM emulation using binfmt/qemu
        /// </summary>
        /// <remarks>
        /// Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of void</returns>
        System.Threading.Tasks.Task SetupEnableemulationAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Enable ARM emulation using binfmt/qemu
        /// </summary>
        /// <remarks>
        /// Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse</returns>
        System.Threading.Tasks.Task<ApiResponse<Object>> SetupEnableemulationWithHttpInfoAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken));
        /// <summary>
        /// Pulls container from docker repo
        /// </summary>
        /// <remarks>
        /// Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of void</returns>
        System.Threading.Tasks.Task SetupPullcontainersAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Pulls container from docker repo
        /// </summary>
        /// <remarks>
        /// Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse</returns>
        System.Threading.Tasks.Task<ApiResponse<Object>> SetupPullcontainersWithHttpInfoAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class SetupApi : ISetupApi
    {
        private TorizonRestAPI.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="SetupApi"/> class.
        /// </summary>
        /// <returns></returns>
        public SetupApi(String basePath)
        {
            this.Configuration = new TorizonRestAPI.Client.Configuration { BasePath = basePath };

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="SetupApi"/> class
        /// </summary>
        /// <returns></returns>
        public SetupApi()
        {
            this.Configuration = TorizonRestAPI.Client.Configuration.Default;

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="SetupApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public SetupApi(TorizonRestAPI.Client.Configuration configuration = null)
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
        /// Enable ARM emulation using binfmt/qemu Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns></returns>
        public void SetupEnableemulation (string progressId = default(string))
        {
             SetupEnableemulationWithHttpInfo(progressId);
        }

        /// <summary>
        /// Enable ARM emulation using binfmt/qemu Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        public ApiResponse<Object> SetupEnableemulationWithHttpInfo (string progressId = default(string))
        {

            var localVarPath = "/setup/enableemulation";
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

            if (progressId != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "progress_id", progressId)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("SetupEnableemulation", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

        /// <summary>
        /// Enable ARM emulation using binfmt/qemu Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of void</returns>
        public async System.Threading.Tasks.Task SetupEnableemulationAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {
             await SetupEnableemulationWithHttpInfoAsync(progressId, cancellationToken);

        }

        /// <summary>
        /// Enable ARM emulation using binfmt/qemu Uses an externa container that leverages binfmt and qemu to enable ARM32 and ARM64 emulation on non-ARM devices
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Object>> SetupEnableemulationWithHttpInfoAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {

            var localVarPath = "/setup/enableemulation";
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

            if (progressId != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "progress_id", progressId)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("SetupEnableemulation", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

        /// <summary>
        /// Pulls container from docker repo Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns></returns>
        public void SetupPullcontainers (string progressId = default(string))
        {
             SetupPullcontainersWithHttpInfo(progressId);
        }

        /// <summary>
        /// Pulls container from docker repo Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        public ApiResponse<Object> SetupPullcontainersWithHttpInfo (string progressId = default(string))
        {

            var localVarPath = "/setup/pullcontainers";
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

            if (progressId != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "progress_id", progressId)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("SetupPullcontainers", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

        /// <summary>
        /// Pulls container from docker repo Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of void</returns>
        public async System.Threading.Tasks.Task SetupPullcontainersAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {
             await SetupPullcontainersWithHttpInfoAsync(progressId, cancellationToken);

        }

        /// <summary>
        /// Pulls container from docker repo Pulls all base and SDK base container for the configured platforms. This can also be used to update them.
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="progressId">Id of a progress cookie (uuid) (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Object>> SetupPullcontainersWithHttpInfoAsync (string progressId = default(string), CancellationToken cancellationToken = default(CancellationToken))
        {

            var localVarPath = "/setup/pullcontainers";
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

            if (progressId != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "progress_id", progressId)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("SetupPullcontainers", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

    }
}
