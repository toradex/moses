/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.8
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
    /// PortBinding represents a binding between a host IP address and a host port. 
    /// </summary>
    [DataContract]
    public partial class DockerPortBinding :  IEquatable<DockerPortBinding>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerPortBinding" /> class.
        /// </summary>
        /// <param name="hostIp">Host IP address that the container&#39;s port is mapped to..</param>
        /// <param name="hostPort">Host port number that the container&#39;s port is mapped to..</param>
        public DockerPortBinding(string hostIp = default(string), string hostPort = default(string))
        {
            this.HostIp = hostIp;
            this.HostPort = hostPort;
        }
        
        /// <summary>
        /// Host IP address that the container&#39;s port is mapped to.
        /// </summary>
        /// <value>Host IP address that the container&#39;s port is mapped to.</value>
        [DataMember(Name="HostIp", EmitDefaultValue=false)]
        public string HostIp { get; set; }

        /// <summary>
        /// Host port number that the container&#39;s port is mapped to.
        /// </summary>
        /// <value>Host port number that the container&#39;s port is mapped to.</value>
        [DataMember(Name="HostPort", EmitDefaultValue=false)]
        public string HostPort { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerPortBinding {\n");
            sb.Append("  HostIp: ").Append(HostIp).Append("\n");
            sb.Append("  HostPort: ").Append(HostPort).Append("\n");
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
            return this.Equals(input as DockerPortBinding);
        }

        /// <summary>
        /// Returns true if DockerPortBinding instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerPortBinding to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerPortBinding input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.HostIp == input.HostIp ||
                    (this.HostIp != null &&
                    this.HostIp.Equals(input.HostIp))
                ) && 
                (
                    this.HostPort == input.HostPort ||
                    (this.HostPort != null &&
                    this.HostPort.Equals(input.HostPort))
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
                if (this.HostIp != null)
                    hashCode = hashCode * 59 + this.HostIp.GetHashCode();
                if (this.HostPort != null)
                    hashCode = hashCode * 59 + this.HostPort.GetHashCode();
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
