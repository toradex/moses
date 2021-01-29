/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = TorizonRestAPI.Client.OpenAPIDateConverter;

namespace TorizonRestAPI.Model
{
    /// <summary>
    /// The behavior to apply when the container exits. The default is not to restart.  An ever increasing delay (double the previous delay, starting at 100ms) is added before each restart to prevent flooding the server. 
    /// </summary>
    [DataContract]
    public partial class DockerRestartPolicy :  IEquatable<DockerRestartPolicy>, IValidatableObject
    {
        /// <summary>
        /// - Empty string or &#x60;no&#x60;means not to restart - &#x60;always&#x60; Always restart - &#x60;unless-stopped&#x60; Restart always except when the user has manually stopped the container - &#x60;on-failure&#x60; Restart only when the container exit code is non-zero 
        /// </summary>
        /// <value>- Empty string or &#x60;no&#x60;means not to restart - &#x60;always&#x60; Always restart - &#x60;unless-stopped&#x60; Restart always except when the user has manually stopped the container - &#x60;on-failure&#x60; Restart only when the container exit code is non-zero </value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum NameEnum
        {
            /// <summary>
            /// Enum Empty for value: 
            /// </summary>
            [EnumMember(Value = "")]
            Empty = 1,

            /// <summary>
            /// Enum Always for value: always
            /// </summary>
            [EnumMember(Value = "always")]
            Always = 2,

            /// <summary>
            /// Enum UnlessStopped for value: unless-stopped
            /// </summary>
            [EnumMember(Value = "unless-stopped")]
            UnlessStopped = 3,

            /// <summary>
            /// Enum OnFailure for value: on-failure
            /// </summary>
            [EnumMember(Value = "on-failure")]
            OnFailure = 4,

            /// <summary>
            /// Enum No for value: no
            /// </summary>
            [EnumMember(Value = "no")]
            No = 5

        }

        /// <summary>
        /// - Empty string or &#x60;no&#x60;means not to restart - &#x60;always&#x60; Always restart - &#x60;unless-stopped&#x60; Restart always except when the user has manually stopped the container - &#x60;on-failure&#x60; Restart only when the container exit code is non-zero 
        /// </summary>
        /// <value>- Empty string or &#x60;no&#x60;means not to restart - &#x60;always&#x60; Always restart - &#x60;unless-stopped&#x60; Restart always except when the user has manually stopped the container - &#x60;on-failure&#x60; Restart only when the container exit code is non-zero </value>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public NameEnum? Name { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerRestartPolicy" /> class.
        /// </summary>
        /// <param name="name">- Empty string or &#x60;no&#x60;means not to restart - &#x60;always&#x60; Always restart - &#x60;unless-stopped&#x60; Restart always except when the user has manually stopped the container - &#x60;on-failure&#x60; Restart only when the container exit code is non-zero .</param>
        /// <param name="maximumRetryCount">If &#x60;on-failure&#x60; is used, the number of times to retry before giving up.</param>
        public DockerRestartPolicy(NameEnum? name = default(NameEnum?), int maximumRetryCount = default(int))
        {
            this.Name = name;
            this.MaximumRetryCount = maximumRetryCount;
        }
        

        /// <summary>
        /// If &#x60;on-failure&#x60; is used, the number of times to retry before giving up
        /// </summary>
        /// <value>If &#x60;on-failure&#x60; is used, the number of times to retry before giving up</value>
        [DataMember(Name="MaximumRetryCount", EmitDefaultValue=false)]
        public int MaximumRetryCount { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerRestartPolicy {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  MaximumRetryCount: ").Append(MaximumRetryCount).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as DockerRestartPolicy);
        }

        /// <summary>
        /// Returns true if DockerRestartPolicy instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerRestartPolicy to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerRestartPolicy input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.MaximumRetryCount == input.MaximumRetryCount ||
                    (this.MaximumRetryCount != null &&
                    this.MaximumRetryCount.Equals(input.MaximumRetryCount))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.MaximumRetryCount != null)
                    hashCode = hashCode * 59 + this.MaximumRetryCount.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
