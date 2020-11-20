/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.12
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
    /// DockerResourcesBlkioWeightDevice
    /// </summary>
    [DataContract]
    public partial class DockerResourcesBlkioWeightDevice :  IEquatable<DockerResourcesBlkioWeightDevice>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerResourcesBlkioWeightDevice" /> class.
        /// </summary>
        /// <param name="path">path.</param>
        /// <param name="weight">weight.</param>
        public DockerResourcesBlkioWeightDevice(string path = default(string), int weight = default(int))
        {
            this.Path = path;
            this.Weight = weight;
        }
        
        /// <summary>
        /// Gets or Sets Path
        /// </summary>
        [DataMember(Name="Path", EmitDefaultValue=false)]
        public string Path { get; set; }

        /// <summary>
        /// Gets or Sets Weight
        /// </summary>
        [DataMember(Name="Weight", EmitDefaultValue=false)]
        public int Weight { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerResourcesBlkioWeightDevice {\n");
            sb.Append("  Path: ").Append(Path).Append("\n");
            sb.Append("  Weight: ").Append(Weight).Append("\n");
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
            return this.Equals(input as DockerResourcesBlkioWeightDevice);
        }

        /// <summary>
        /// Returns true if DockerResourcesBlkioWeightDevice instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerResourcesBlkioWeightDevice to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerResourcesBlkioWeightDevice input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Path == input.Path ||
                    (this.Path != null &&
                    this.Path.Equals(input.Path))
                ) && 
                (
                    this.Weight == input.Weight ||
                    (this.Weight != null &&
                    this.Weight.Equals(input.Weight))
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
                if (this.Path != null)
                    hashCode = hashCode * 59 + this.Path.GetHashCode();
                if (this.Weight != null)
                    hashCode = hashCode * 59 + this.Weight.GetHashCode();
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

            
            // Weight (int) minimum
            if(this.Weight < (int)0)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for Weight, must be a value greater than or equal to 0.", new [] { "Weight" });
            }

            yield break;
        }
    }

}
