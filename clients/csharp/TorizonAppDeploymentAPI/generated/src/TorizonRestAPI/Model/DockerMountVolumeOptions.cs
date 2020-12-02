/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.14
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
    /// Optional configuration for the &#x60;volume&#x60; type.
    /// </summary>
    [DataContract]
    public partial class DockerMountVolumeOptions :  IEquatable<DockerMountVolumeOptions>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMountVolumeOptions" /> class.
        /// </summary>
        /// <param name="noCopy">Populate volume with data from the target. (default to false).</param>
        /// <param name="labels">User-defined key/value metadata..</param>
        /// <param name="driverConfig">driverConfig.</param>
        public DockerMountVolumeOptions(bool noCopy = false, Dictionary<string, string> labels = default(Dictionary<string, string>), DockerMountVolumeOptionsDriverConfig driverConfig = default(DockerMountVolumeOptionsDriverConfig))
        {
            // use default value if no "noCopy" provided
            if (noCopy == null)
            {
                this.NoCopy = false;
            }
            else
            {
                this.NoCopy = noCopy;
            }
            this.Labels = labels;
            this.DriverConfig = driverConfig;
        }
        
        /// <summary>
        /// Populate volume with data from the target.
        /// </summary>
        /// <value>Populate volume with data from the target.</value>
        [DataMember(Name="NoCopy", EmitDefaultValue=false)]
        public bool NoCopy { get; set; }

        /// <summary>
        /// User-defined key/value metadata.
        /// </summary>
        /// <value>User-defined key/value metadata.</value>
        [DataMember(Name="Labels", EmitDefaultValue=false)]
        public Dictionary<string, string> Labels { get; set; }

        /// <summary>
        /// Gets or Sets DriverConfig
        /// </summary>
        [DataMember(Name="DriverConfig", EmitDefaultValue=false)]
        public DockerMountVolumeOptionsDriverConfig DriverConfig { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMountVolumeOptions {\n");
            sb.Append("  NoCopy: ").Append(NoCopy).Append("\n");
            sb.Append("  Labels: ").Append(Labels).Append("\n");
            sb.Append("  DriverConfig: ").Append(DriverConfig).Append("\n");
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
            return this.Equals(input as DockerMountVolumeOptions);
        }

        /// <summary>
        /// Returns true if DockerMountVolumeOptions instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMountVolumeOptions to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMountVolumeOptions input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.NoCopy == input.NoCopy ||
                    (this.NoCopy != null &&
                    this.NoCopy.Equals(input.NoCopy))
                ) && 
                (
                    this.Labels == input.Labels ||
                    this.Labels != null &&
                    input.Labels != null &&
                    this.Labels.SequenceEqual(input.Labels)
                ) && 
                (
                    this.DriverConfig == input.DriverConfig ||
                    (this.DriverConfig != null &&
                    this.DriverConfig.Equals(input.DriverConfig))
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
                if (this.NoCopy != null)
                    hashCode = hashCode * 59 + this.NoCopy.GetHashCode();
                if (this.Labels != null)
                    hashCode = hashCode * 59 + this.Labels.GetHashCode();
                if (this.DriverConfig != null)
                    hashCode = hashCode * 59 + this.DriverConfig.GetHashCode();
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
