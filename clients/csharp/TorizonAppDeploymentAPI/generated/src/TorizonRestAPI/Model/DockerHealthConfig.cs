/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.13
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
    /// A test to perform to check that the container is healthy.
    /// </summary>
    [DataContract]
    public partial class DockerHealthConfig :  IEquatable<DockerHealthConfig>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerHealthConfig" /> class.
        /// </summary>
        /// <param name="test">The test to perform. Possible values are:  - &#x60;[]&#x60; inherit healthcheck from image or parent image - &#x60;[\&quot;NONE\&quot;]&#x60; disable healthcheck - &#x60;[\&quot;CMD\&quot;, args...]&#x60; exec arguments directly - &#x60;[\&quot;CMD-SHELL\&quot;, command]&#x60; run command with system&#39;s default shell .</param>
        /// <param name="interval">The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit..</param>
        /// <param name="timeout">The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit..</param>
        /// <param name="retries">The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit..</param>
        /// <param name="startPeriod">Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit..</param>
        public DockerHealthConfig(List<string> test = default(List<string>), int interval = default(int), int timeout = default(int), int retries = default(int), int startPeriod = default(int))
        {
            this.Test = test;
            this.Interval = interval;
            this.Timeout = timeout;
            this.Retries = retries;
            this.StartPeriod = startPeriod;
        }
        
        /// <summary>
        /// The test to perform. Possible values are:  - &#x60;[]&#x60; inherit healthcheck from image or parent image - &#x60;[\&quot;NONE\&quot;]&#x60; disable healthcheck - &#x60;[\&quot;CMD\&quot;, args...]&#x60; exec arguments directly - &#x60;[\&quot;CMD-SHELL\&quot;, command]&#x60; run command with system&#39;s default shell 
        /// </summary>
        /// <value>The test to perform. Possible values are:  - &#x60;[]&#x60; inherit healthcheck from image or parent image - &#x60;[\&quot;NONE\&quot;]&#x60; disable healthcheck - &#x60;[\&quot;CMD\&quot;, args...]&#x60; exec arguments directly - &#x60;[\&quot;CMD-SHELL\&quot;, command]&#x60; run command with system&#39;s default shell </value>
        [DataMember(Name="Test", EmitDefaultValue=false)]
        public List<string> Test { get; set; }

        /// <summary>
        /// The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
        /// </summary>
        /// <value>The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.</value>
        [DataMember(Name="Interval", EmitDefaultValue=false)]
        public int Interval { get; set; }

        /// <summary>
        /// The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
        /// </summary>
        /// <value>The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit.</value>
        [DataMember(Name="Timeout", EmitDefaultValue=false)]
        public int Timeout { get; set; }

        /// <summary>
        /// The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit.
        /// </summary>
        /// <value>The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit.</value>
        [DataMember(Name="Retries", EmitDefaultValue=false)]
        public int Retries { get; set; }

        /// <summary>
        /// Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
        /// </summary>
        /// <value>Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.</value>
        [DataMember(Name="StartPeriod", EmitDefaultValue=false)]
        public int StartPeriod { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerHealthConfig {\n");
            sb.Append("  Test: ").Append(Test).Append("\n");
            sb.Append("  Interval: ").Append(Interval).Append("\n");
            sb.Append("  Timeout: ").Append(Timeout).Append("\n");
            sb.Append("  Retries: ").Append(Retries).Append("\n");
            sb.Append("  StartPeriod: ").Append(StartPeriod).Append("\n");
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
            return this.Equals(input as DockerHealthConfig);
        }

        /// <summary>
        /// Returns true if DockerHealthConfig instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerHealthConfig to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerHealthConfig input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Test == input.Test ||
                    this.Test != null &&
                    input.Test != null &&
                    this.Test.SequenceEqual(input.Test)
                ) && 
                (
                    this.Interval == input.Interval ||
                    (this.Interval != null &&
                    this.Interval.Equals(input.Interval))
                ) && 
                (
                    this.Timeout == input.Timeout ||
                    (this.Timeout != null &&
                    this.Timeout.Equals(input.Timeout))
                ) && 
                (
                    this.Retries == input.Retries ||
                    (this.Retries != null &&
                    this.Retries.Equals(input.Retries))
                ) && 
                (
                    this.StartPeriod == input.StartPeriod ||
                    (this.StartPeriod != null &&
                    this.StartPeriod.Equals(input.StartPeriod))
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
                if (this.Test != null)
                    hashCode = hashCode * 59 + this.Test.GetHashCode();
                if (this.Interval != null)
                    hashCode = hashCode * 59 + this.Interval.GetHashCode();
                if (this.Timeout != null)
                    hashCode = hashCode * 59 + this.Timeout.GetHashCode();
                if (this.Retries != null)
                    hashCode = hashCode * 59 + this.Retries.GetHashCode();
                if (this.StartPeriod != null)
                    hashCode = hashCode * 59 + this.StartPeriod.GetHashCode();
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
