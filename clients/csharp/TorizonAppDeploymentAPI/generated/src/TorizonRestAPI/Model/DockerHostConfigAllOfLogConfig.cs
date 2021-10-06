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
    /// The logging configuration for this container
    /// </summary>
    [DataContract]
    public partial class DockerHostConfigAllOfLogConfig :  IEquatable<DockerHostConfigAllOfLogConfig>, IValidatableObject
    {
        /// <summary>
        /// Defines Type
        /// </summary>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum TypeEnum
        {
            /// <summary>
            /// Enum JsonFile for value: json-file
            /// </summary>
            [EnumMember(Value = "json-file")]
            JsonFile = 1,

            /// <summary>
            /// Enum Syslog for value: syslog
            /// </summary>
            [EnumMember(Value = "syslog")]
            Syslog = 2,

            /// <summary>
            /// Enum Journald for value: journald
            /// </summary>
            [EnumMember(Value = "journald")]
            Journald = 3,

            /// <summary>
            /// Enum Gelf for value: gelf
            /// </summary>
            [EnumMember(Value = "gelf")]
            Gelf = 4,

            /// <summary>
            /// Enum Fluentd for value: fluentd
            /// </summary>
            [EnumMember(Value = "fluentd")]
            Fluentd = 5,

            /// <summary>
            /// Enum Awslogs for value: awslogs
            /// </summary>
            [EnumMember(Value = "awslogs")]
            Awslogs = 6,

            /// <summary>
            /// Enum Splunk for value: splunk
            /// </summary>
            [EnumMember(Value = "splunk")]
            Splunk = 7,

            /// <summary>
            /// Enum Etwlogs for value: etwlogs
            /// </summary>
            [EnumMember(Value = "etwlogs")]
            Etwlogs = 8,

            /// <summary>
            /// Enum None for value: none
            /// </summary>
            [EnumMember(Value = "none")]
            None = 9

        }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="Type", EmitDefaultValue=false)]
        public TypeEnum? Type { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerHostConfigAllOfLogConfig" /> class.
        /// </summary>
        /// <param name="type">type.</param>
        /// <param name="config">config.</param>
        public DockerHostConfigAllOfLogConfig(TypeEnum? type = default(TypeEnum?), Dictionary<string, string> config = default(Dictionary<string, string>))
        {
            this.Type = type;
            this.Config = config;
        }


        /// <summary>
        /// Gets or Sets Config
        /// </summary>
        [DataMember(Name="Config", EmitDefaultValue=false)]
        public Dictionary<string, string> Config { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerHostConfigAllOfLogConfig {\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Config: ").Append(Config).Append("\n");
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
            return this.Equals(input as DockerHostConfigAllOfLogConfig);
        }

        /// <summary>
        /// Returns true if DockerHostConfigAllOfLogConfig instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerHostConfigAllOfLogConfig to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerHostConfigAllOfLogConfig input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.Config == input.Config ||
                    this.Config != null &&
                    input.Config != null &&
                    this.Config.SequenceEqual(input.Config)
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
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.Config != null)
                    hashCode = hashCode * 59 + this.Config.GetHashCode();
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
