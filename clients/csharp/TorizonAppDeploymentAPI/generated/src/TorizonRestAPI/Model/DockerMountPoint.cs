/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.7
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
    /// A mount point inside a container
    /// </summary>
    [DataContract]
    public partial class DockerMountPoint :  IEquatable<DockerMountPoint>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMountPoint" /> class.
        /// </summary>
        /// <param name="type">type.</param>
        /// <param name="name">name.</param>
        /// <param name="source">source.</param>
        /// <param name="destination">destination.</param>
        /// <param name="driver">driver.</param>
        /// <param name="mode">mode.</param>
        /// <param name="rW">rW.</param>
        /// <param name="propagation">propagation.</param>
        public DockerMountPoint(string type = default(string), string name = default(string), string source = default(string), string destination = default(string), string driver = default(string), string mode = default(string), bool rW = default(bool), string propagation = default(string))
        {
            this.Type = type;
            this.Name = name;
            this.Source = source;
            this.Destination = destination;
            this.Driver = driver;
            this.Mode = mode;
            this.RW = rW;
            this.Propagation = propagation;
        }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="Type", EmitDefaultValue=false)]
        public string Type { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Source
        /// </summary>
        [DataMember(Name="Source", EmitDefaultValue=false)]
        public string Source { get; set; }

        /// <summary>
        /// Gets or Sets Destination
        /// </summary>
        [DataMember(Name="Destination", EmitDefaultValue=false)]
        public string Destination { get; set; }

        /// <summary>
        /// Gets or Sets Driver
        /// </summary>
        [DataMember(Name="Driver", EmitDefaultValue=false)]
        public string Driver { get; set; }

        /// <summary>
        /// Gets or Sets Mode
        /// </summary>
        [DataMember(Name="Mode", EmitDefaultValue=false)]
        public string Mode { get; set; }

        /// <summary>
        /// Gets or Sets RW
        /// </summary>
        [DataMember(Name="RW", EmitDefaultValue=false)]
        public bool RW { get; set; }

        /// <summary>
        /// Gets or Sets Propagation
        /// </summary>
        [DataMember(Name="Propagation", EmitDefaultValue=false)]
        public string Propagation { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMountPoint {\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Source: ").Append(Source).Append("\n");
            sb.Append("  Destination: ").Append(Destination).Append("\n");
            sb.Append("  Driver: ").Append(Driver).Append("\n");
            sb.Append("  Mode: ").Append(Mode).Append("\n");
            sb.Append("  RW: ").Append(RW).Append("\n");
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
            return this.Equals(input as DockerMountPoint);
        }

        /// <summary>
        /// Returns true if DockerMountPoint instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMountPoint to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMountPoint input)
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
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Source == input.Source ||
                    (this.Source != null &&
                    this.Source.Equals(input.Source))
                ) && 
                (
                    this.Destination == input.Destination ||
                    (this.Destination != null &&
                    this.Destination.Equals(input.Destination))
                ) && 
                (
                    this.Driver == input.Driver ||
                    (this.Driver != null &&
                    this.Driver.Equals(input.Driver))
                ) && 
                (
                    this.Mode == input.Mode ||
                    (this.Mode != null &&
                    this.Mode.Equals(input.Mode))
                ) && 
                (
                    this.RW == input.RW ||
                    (this.RW != null &&
                    this.RW.Equals(input.RW))
                ) && 
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
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Source != null)
                    hashCode = hashCode * 59 + this.Source.GetHashCode();
                if (this.Destination != null)
                    hashCode = hashCode * 59 + this.Destination.GetHashCode();
                if (this.Driver != null)
                    hashCode = hashCode * 59 + this.Driver.GetHashCode();
                if (this.Mode != null)
                    hashCode = hashCode * 59 + this.Mode.GetHashCode();
                if (this.RW != null)
                    hashCode = hashCode * 59 + this.RW.GetHashCode();
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
