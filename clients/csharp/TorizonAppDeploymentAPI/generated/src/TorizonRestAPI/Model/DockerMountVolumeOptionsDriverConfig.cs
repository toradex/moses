/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.7
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
    /// Map of driver specific options
    /// </summary>
    [DataContract]
    public partial class DockerMountVolumeOptionsDriverConfig :  IEquatable<DockerMountVolumeOptionsDriverConfig>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMountVolumeOptionsDriverConfig" /> class.
        /// </summary>
        /// <param name="name">Name of the driver to use to create the volume..</param>
        /// <param name="options">key/value map of driver specific options..</param>
        public DockerMountVolumeOptionsDriverConfig(string name = default(string), Dictionary<string, string> options = default(Dictionary<string, string>))
        {
            this.Name = name;
            this.Options = options;
        }
        
        /// <summary>
        /// Name of the driver to use to create the volume.
        /// </summary>
        /// <value>Name of the driver to use to create the volume.</value>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// key/value map of driver specific options.
        /// </summary>
        /// <value>key/value map of driver specific options.</value>
        [DataMember(Name="Options", EmitDefaultValue=false)]
        public Dictionary<string, string> Options { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMountVolumeOptionsDriverConfig {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Options: ").Append(Options).Append("\n");
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
            return this.Equals(input as DockerMountVolumeOptionsDriverConfig);
        }

        /// <summary>
        /// Returns true if DockerMountVolumeOptionsDriverConfig instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMountVolumeOptionsDriverConfig to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMountVolumeOptionsDriverConfig input)
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
                    this.Options == input.Options ||
                    this.Options != null &&
                    input.Options != null &&
                    this.Options.SequenceEqual(input.Options)
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
                if (this.Options != null)
                    hashCode = hashCode * 59 + this.Options.GetHashCode();
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
