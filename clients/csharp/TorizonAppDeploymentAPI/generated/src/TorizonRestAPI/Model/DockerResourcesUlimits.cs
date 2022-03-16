/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.6
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
    /// DockerResourcesUlimits
    /// </summary>
    [DataContract]
    public partial class DockerResourcesUlimits :  IEquatable<DockerResourcesUlimits>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerResourcesUlimits" /> class.
        /// </summary>
        /// <param name="name">Name of ulimit.</param>
        /// <param name="soft">Soft limit.</param>
        /// <param name="hard">Hard limit.</param>
        public DockerResourcesUlimits(string name = default(string), int soft = default(int), int hard = default(int))
        {
            this.Name = name;
            this.Soft = soft;
            this.Hard = hard;
        }

        /// <summary>
        /// Name of ulimit
        /// </summary>
        /// <value>Name of ulimit</value>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Soft limit
        /// </summary>
        /// <value>Soft limit</value>
        [DataMember(Name="Soft", EmitDefaultValue=false)]
        public int Soft { get; set; }

        /// <summary>
        /// Hard limit
        /// </summary>
        /// <value>Hard limit</value>
        [DataMember(Name="Hard", EmitDefaultValue=false)]
        public int Hard { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerResourcesUlimits {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Soft: ").Append(Soft).Append("\n");
            sb.Append("  Hard: ").Append(Hard).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as DockerResourcesUlimits);
        }

        /// <summary>
        /// Returns true if DockerResourcesUlimits instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerResourcesUlimits to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerResourcesUlimits input)
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
                    this.Soft == input.Soft ||
                    (this.Soft != null &&
                    this.Soft.Equals(input.Soft))
                ) && 
                (
                    this.Hard == input.Hard ||
                    (this.Hard != null &&
                    this.Hard.Equals(input.Hard))
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
                if (this.Soft != null)
                    hashCode = hashCode * 59 + this.Soft.GetHashCode();
                if (this.Hard != null)
                    hashCode = hashCode * 59 + this.Hard.GetHashCode();
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
