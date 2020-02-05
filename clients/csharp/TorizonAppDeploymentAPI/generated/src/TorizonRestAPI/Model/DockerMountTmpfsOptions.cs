/* 
 * Torizon Deployment API
 *
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.0
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
    /// Optional configuration for the &#x60;tmpfs&#x60; type.
    /// </summary>
    [DataContract]
    public partial class DockerMountTmpfsOptions :  IEquatable<DockerMountTmpfsOptions>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMountTmpfsOptions" /> class.
        /// </summary>
        /// <param name="sizeBytes">The size for the tmpfs mount in bytes..</param>
        /// <param name="mode">The permission mode for the tmpfs mount in an integer..</param>
        public DockerMountTmpfsOptions(long sizeBytes = default(long), int mode = default(int))
        {
            this.SizeBytes = sizeBytes;
            this.Mode = mode;
        }
        
        /// <summary>
        /// The size for the tmpfs mount in bytes.
        /// </summary>
        /// <value>The size for the tmpfs mount in bytes.</value>
        [DataMember(Name="SizeBytes", EmitDefaultValue=false)]
        public long SizeBytes { get; set; }

        /// <summary>
        /// The permission mode for the tmpfs mount in an integer.
        /// </summary>
        /// <value>The permission mode for the tmpfs mount in an integer.</value>
        [DataMember(Name="Mode", EmitDefaultValue=false)]
        public int Mode { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMountTmpfsOptions {\n");
            sb.Append("  SizeBytes: ").Append(SizeBytes).Append("\n");
            sb.Append("  Mode: ").Append(Mode).Append("\n");
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
            return this.Equals(input as DockerMountTmpfsOptions);
        }

        /// <summary>
        /// Returns true if DockerMountTmpfsOptions instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMountTmpfsOptions to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMountTmpfsOptions input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.SizeBytes == input.SizeBytes ||
                    (this.SizeBytes != null &&
                    this.SizeBytes.Equals(input.SizeBytes))
                ) && 
                (
                    this.Mode == input.Mode ||
                    (this.Mode != null &&
                    this.Mode.Equals(input.Mode))
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
                if (this.SizeBytes != null)
                    hashCode = hashCode * 59 + this.SizeBytes.GetHashCode();
                if (this.Mode != null)
                    hashCode = hashCode * 59 + this.Mode.GetHashCode();
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
