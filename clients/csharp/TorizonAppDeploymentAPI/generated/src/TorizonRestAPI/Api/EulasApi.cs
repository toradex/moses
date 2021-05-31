/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.2
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
    public interface IEulasApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Get detail about an eula
        /// </summary>
        /// <remarks>
        /// Return detailed information about a specific eula
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <returns>Eula</returns>
        Eula EulaGet (string eulaId);

        /// <summary>
        /// Get detail about an eula
        /// </summary>
        /// <remarks>
        /// Return detailed information about a specific eula
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <returns>ApiResponse of Eula</returns>
        ApiResponse<Eula> EulaGetWithHttpInfo (string eulaId);
        /// <summary>
        /// Change eula properties
        /// </summary>
        /// <remarks>
        /// Set eula as visualized and/or accepted
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <returns>Eula</returns>
        Eula EulaModify (string eulaId, Eula e = default(Eula));

        /// <summary>
        /// Change eula properties
        /// </summary>
        /// <remarks>
        /// Set eula as visualized and/or accepted
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <returns>ApiResponse of Eula</returns>
        ApiResponse<Eula> EulaModifyWithHttpInfo (string eulaId, Eula e = default(Eula));
        /// <summary>
        /// Get all eulas
        /// </summary>
        /// <remarks>
        /// Returns information about all eulas required to run different platforms on the system
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>List&lt;Eula&gt;</returns>
        List<Eula> EulasGet ();

        /// <summary>
        /// Get all eulas
        /// </summary>
        /// <remarks>
        /// Returns information about all eulas required to run different platforms on the system
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>ApiResponse of List&lt;Eula&gt;</returns>
        ApiResponse<List<Eula>> EulasGetWithHttpInfo ();
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// Get detail about an eula
        /// </summary>
        /// <remarks>
        /// Return detailed information about a specific eula
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Eula</returns>
        System.Threading.Tasks.Task<Eula> EulaGetAsync (string eulaId, CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Get detail about an eula
        /// </summary>
        /// <remarks>
        /// Return detailed information about a specific eula
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Eula)</returns>
        System.Threading.Tasks.Task<ApiResponse<Eula>> EulaGetWithHttpInfoAsync (string eulaId, CancellationToken cancellationToken = default(CancellationToken));
        /// <summary>
        /// Change eula properties
        /// </summary>
        /// <remarks>
        /// Set eula as visualized and/or accepted
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Eula</returns>
        System.Threading.Tasks.Task<Eula> EulaModifyAsync (string eulaId, Eula e = default(Eula), CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Change eula properties
        /// </summary>
        /// <remarks>
        /// Set eula as visualized and/or accepted
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Eula)</returns>
        System.Threading.Tasks.Task<ApiResponse<Eula>> EulaModifyWithHttpInfoAsync (string eulaId, Eula e = default(Eula), CancellationToken cancellationToken = default(CancellationToken));
        /// <summary>
        /// Get all eulas
        /// </summary>
        /// <remarks>
        /// Returns information about all eulas required to run different platforms on the system
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;Eula&gt;</returns>
        System.Threading.Tasks.Task<List<Eula>> EulasGetAsync (CancellationToken cancellationToken = default(CancellationToken));

        /// <summary>
        /// Get all eulas
        /// </summary>
        /// <remarks>
        /// Returns information about all eulas required to run different platforms on the system
        /// </remarks>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;Eula&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<Eula>>> EulasGetWithHttpInfoAsync (CancellationToken cancellationToken = default(CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class EulasApi : IEulasApi
    {
        private TorizonRestAPI.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="EulasApi"/> class.
        /// </summary>
        /// <returns></returns>
        public EulasApi(String basePath)
        {
            this.Configuration = new TorizonRestAPI.Client.Configuration { BasePath = basePath };

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="EulasApi"/> class
        /// </summary>
        /// <returns></returns>
        public EulasApi()
        {
            this.Configuration = TorizonRestAPI.Client.Configuration.Default;

            ExceptionFactory = TorizonRestAPI.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="EulasApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public EulasApi(TorizonRestAPI.Client.Configuration configuration = null)
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
        /// Get detail about an eula Return detailed information about a specific eula
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <returns>Eula</returns>
        public Eula EulaGet (string eulaId)
        {
             ApiResponse<Eula> localVarResponse = EulaGetWithHttpInfo(eulaId);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get detail about an eula Return detailed information about a specific eula
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <returns>ApiResponse of Eula</returns>
        public ApiResponse<Eula> EulaGetWithHttpInfo (string eulaId)
        {
            // verify the required parameter 'eulaId' is set
            if (eulaId == null)
                throw new ApiException(400, "Missing required parameter 'eulaId' when calling EulasApi->EulaGet");

            var localVarPath = "/eulas/{eula_id}";
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

            if (eulaId != null) localVarPathParams.Add("eula_id", this.Configuration.ApiClient.ParameterToString(eulaId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulaGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Eula>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Eula) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Eula)));
        }

        /// <summary>
        /// Get detail about an eula Return detailed information about a specific eula
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Eula</returns>
        public async System.Threading.Tasks.Task<Eula> EulaGetAsync (string eulaId, CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<Eula> localVarResponse = await EulaGetWithHttpInfoAsync(eulaId, cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get detail about an eula Return detailed information about a specific eula
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Eula)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Eula>> EulaGetWithHttpInfoAsync (string eulaId, CancellationToken cancellationToken = default(CancellationToken))
        {
            // verify the required parameter 'eulaId' is set
            if (eulaId == null)
                throw new ApiException(400, "Missing required parameter 'eulaId' when calling EulasApi->EulaGet");

            var localVarPath = "/eulas/{eula_id}";
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

            if (eulaId != null) localVarPathParams.Add("eula_id", this.Configuration.ApiClient.ParameterToString(eulaId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulaGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Eula>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Eula) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Eula)));
        }

        /// <summary>
        /// Change eula properties Set eula as visualized and/or accepted
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <returns>Eula</returns>
        public Eula EulaModify (string eulaId, Eula e = default(Eula))
        {
             ApiResponse<Eula> localVarResponse = EulaModifyWithHttpInfo(eulaId, e);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Change eula properties Set eula as visualized and/or accepted
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <returns>ApiResponse of Eula</returns>
        public ApiResponse<Eula> EulaModifyWithHttpInfo (string eulaId, Eula e = default(Eula))
        {
            // verify the required parameter 'eulaId' is set
            if (eulaId == null)
                throw new ApiException(400, "Missing required parameter 'eulaId' when calling EulasApi->EulaModify");

            var localVarPath = "/eulas/{eula_id}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (eulaId != null) localVarPathParams.Add("eula_id", this.Configuration.ApiClient.ParameterToString(eulaId)); // path parameter
            if (e != null && e.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(e); // http body (model) parameter
            }
            else
            {
                localVarPostBody = e; // byte array
            }


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.PUT, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulaModify", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Eula>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Eula) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Eula)));
        }

        /// <summary>
        /// Change eula properties Set eula as visualized and/or accepted
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of Eula</returns>
        public async System.Threading.Tasks.Task<Eula> EulaModifyAsync (string eulaId, Eula e = default(Eula), CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<Eula> localVarResponse = await EulaModifyWithHttpInfoAsync(eulaId, e, cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Change eula properties Set eula as visualized and/or accepted
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="eulaId">Id of an Eula</param>
        /// <param name="e"> (optional)</param>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (Eula)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Eula>> EulaModifyWithHttpInfoAsync (string eulaId, Eula e = default(Eula), CancellationToken cancellationToken = default(CancellationToken))
        {
            // verify the required parameter 'eulaId' is set
            if (eulaId == null)
                throw new ApiException(400, "Missing required parameter 'eulaId' when calling EulasApi->EulaModify");

            var localVarPath = "/eulas/{eula_id}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (eulaId != null) localVarPathParams.Add("eula_id", this.Configuration.ApiClient.ParameterToString(eulaId)); // path parameter
            if (e != null && e.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(e); // http body (model) parameter
            }
            else
            {
                localVarPostBody = e; // byte array
            }


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.PUT, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulaModify", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Eula>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Eula) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Eula)));
        }

        /// <summary>
        /// Get all eulas Returns information about all eulas required to run different platforms on the system
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>List&lt;Eula&gt;</returns>
        public List<Eula> EulasGet ()
        {
             ApiResponse<List<Eula>> localVarResponse = EulasGetWithHttpInfo();
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get all eulas Returns information about all eulas required to run different platforms on the system
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>ApiResponse of List&lt;Eula&gt;</returns>
        public ApiResponse<List<Eula>> EulasGetWithHttpInfo ()
        {

            var localVarPath = "/eulas";
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



            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulasGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Eula>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Eula>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Eula>)));
        }

        /// <summary>
        /// Get all eulas Returns information about all eulas required to run different platforms on the system
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of List&lt;Eula&gt;</returns>
        public async System.Threading.Tasks.Task<List<Eula>> EulasGetAsync (CancellationToken cancellationToken = default(CancellationToken))
        {
             ApiResponse<List<Eula>> localVarResponse = await EulasGetWithHttpInfoAsync(cancellationToken);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get all eulas Returns information about all eulas required to run different platforms on the system
        /// </summary>
        /// <exception cref="TorizonRestAPI.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="cancellationToken">Cancellation Token to cancel request (optional) </param>
        /// <returns>Task of ApiResponse (List&lt;Eula&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<Eula>>> EulasGetWithHttpInfoAsync (CancellationToken cancellationToken = default(CancellationToken))
        {

            var localVarPath = "/eulas";
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



            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType, cancellationToken);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("EulasGet", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Eula>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Eula>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Eula>)));
        }

    }
}
