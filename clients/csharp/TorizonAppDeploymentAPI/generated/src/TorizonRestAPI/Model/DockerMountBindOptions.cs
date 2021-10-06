/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.4
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
    /// Optional configuration for the &#x60;bind&#x60; type.
    /// </summary>
    [DataContract]
    public partial class DockerMountBindOptions :  IEquatable<DockerMountBindOptions>, IValidatableObject
    {
        /// <summary>
        /// A propagation mode with the value &#x60;[r]private&#x60;, &#x60;[r]shared&#x60;, or &#x60;[r]slave&#x60;.
        /// </summary>
        /// <value>A propagation mode with the value &#x60;[r]private&#x60;, &#x60;[r]shared&#x60;, or &#x60;[r]slave&#x60;.</value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum PropagationEnum
        {
            /// <summary>
            /// Enum Private for value: private
            /// </summary>
            [EnumMember(Value = "private")]
            Private = 1,

            /// <summary>
            /// Enum Rprivate for value: rprivate
            /// </summary>
            [EnumMember(Value = "rprivate")]
            Rprivate = 2,

            /// <summary>
            /// Enum Shared for value: shared
            /// </summary>
            [EnumMember(Value = "shared")]
            Shared = 3,

            /// <summary>
            /// Enum Rshared for value: rshared
            /// </summary>
            [EnumMember(Value = "rshared")]
            Rshared = 4,

            /// <summary>
            /// Enum Slave for value: slave
            /// </summary>
            [EnumMember(Value = "slave")]
            Slave = 5,

            /// <summary>
            /// Enum Rslave for value: rslave
            /// </summary>
            [EnumMember(Value = "rslave")]
            Rslave = 6

        }

        /// <summary>
        /// A propagation mode with the value &#x60;[r]private&#x60;, &#x60;[r]shared&#x60;, or &#x60;[r]slave&#x60;.
        /// </summary>
        /// <value>A propagation mode with the value &#x60;[r]private&#x60;, &#x60;[r]shared&#x60;, or &#x60;[r]slave&#x60;.</value>
        [DataMember(Name="Propagation", EmitDefaultValue=false)]
        public PropagationEnum? Propagation { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMountBindOptions" /> class.
        /// </summary>
        /// <param name="propagation">A propagation mode with the value &#x60;[r]private&#x60;, &#x60;[r]shared&#x60;, or &#x60;[r]slave&#x60;..</param>
        public DockerMountBindOptions(PropagationEnum? propagation = default(PropagationEnum?))
        {
            this.Propagation = propagation;
        }


        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMountBindOptions {\n");
            sb.Append("  Propagation: ").Append(Propagation).Append("\n");
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
            return this.Equals(input as DockerMountBindOptions);
        }

        /// <summary>
        /// Returns true if DockerMountBindOptions instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMountBindOptions to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMountBindOptions input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Propagation == input.Propagation ||
                    (this.Propagation != null &&
                    this.Propagation.Equals(input.Propagation))
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
                if (this.Propagation != null)
                    hashCode = hashCode * 59 + this.Propagation.GetHashCode();
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
