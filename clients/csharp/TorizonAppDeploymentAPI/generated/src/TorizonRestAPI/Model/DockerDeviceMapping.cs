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
    /// A device mapping between the host and container
    /// </summary>
    [DataContract]
    public partial class DockerDeviceMapping :  IEquatable<DockerDeviceMapping>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerDeviceMapping" /> class.
        /// </summary>
        /// <param name="pathOnHost">pathOnHost.</param>
        /// <param name="pathInContainer">pathInContainer.</param>
        /// <param name="cgroupPermissions">cgroupPermissions.</param>
        public DockerDeviceMapping(string pathOnHost = default(string), string pathInContainer = default(string), string cgroupPermissions = default(string))
        {
            this.PathOnHost = pathOnHost;
            this.PathInContainer = pathInContainer;
            this.CgroupPermissions = cgroupPermissions;
        }
        
        /// <summary>
        /// Gets or Sets PathOnHost
        /// </summary>
        [DataMember(Name="PathOnHost", EmitDefaultValue=false)]
        public string PathOnHost { get; set; }

        /// <summary>
        /// Gets or Sets PathInContainer
        /// </summary>
        [DataMember(Name="PathInContainer", EmitDefaultValue=false)]
        public string PathInContainer { get; set; }

        /// <summary>
        /// Gets or Sets CgroupPermissions
        /// </summary>
        [DataMember(Name="CgroupPermissions", EmitDefaultValue=false)]
        public string CgroupPermissions { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerDeviceMapping {\n");
            sb.Append("  PathOnHost: ").Append(PathOnHost).Append("\n");
            sb.Append("  PathInContainer: ").Append(PathInContainer).Append("\n");
            sb.Append("  CgroupPermissions: ").Append(CgroupPermissions).Append("\n");
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
            return this.Equals(input as DockerDeviceMapping);
        }

        /// <summary>
        /// Returns true if DockerDeviceMapping instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerDeviceMapping to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerDeviceMapping input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.PathOnHost == input.PathOnHost ||
                    (this.PathOnHost != null &&
                    this.PathOnHost.Equals(input.PathOnHost))
                ) && 
                (
                    this.PathInContainer == input.PathInContainer ||
                    (this.PathInContainer != null &&
                    this.PathInContainer.Equals(input.PathInContainer))
                ) && 
                (
                    this.CgroupPermissions == input.CgroupPermissions ||
                    (this.CgroupPermissions != null &&
                    this.CgroupPermissions.Equals(input.CgroupPermissions))
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
                if (this.PathOnHost != null)
                    hashCode = hashCode * 59 + this.PathOnHost.GetHashCode();
                if (this.PathInContainer != null)
                    hashCode = hashCode * 59 + this.PathInContainer.GetHashCode();
                if (this.CgroupPermissions != null)
                    hashCode = hashCode * 59 + this.CgroupPermissions.GetHashCode();
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
