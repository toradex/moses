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
    /// DockerMount
    /// </summary>
    [DataContract]
    public partial class DockerMount :  IEquatable<DockerMount>, IValidatableObject
    {
        /// <summary>
        /// The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs. 
        /// </summary>
        /// <value>The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs. </value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum TypeEnum
        {
            /// <summary>
            /// Enum Bind for value: bind
            /// </summary>
            [EnumMember(Value = "bind")]
            Bind = 1,

            /// <summary>
            /// Enum Volume for value: volume
            /// </summary>
            [EnumMember(Value = "volume")]
            Volume = 2,

            /// <summary>
            /// Enum Tmpfs for value: tmpfs
            /// </summary>
            [EnumMember(Value = "tmpfs")]
            Tmpfs = 3

        }

        /// <summary>
        /// The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs. 
        /// </summary>
        /// <value>The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs. </value>
        [DataMember(Name="Type", EmitDefaultValue=false)]
        public TypeEnum? Type { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerMount" /> class.
        /// </summary>
        /// <param name="target">Container path..</param>
        /// <param name="source">Mount source (e.g. a volume name, a host path)..</param>
        /// <param name="type">The mount type. Available types:  - &#x60;bind&#x60; Mounts a file or directory from the host into the container. Must exist prior to creating the container. - &#x60;volume&#x60; Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - &#x60;tmpfs&#x60; Create a tmpfs with the given options. The mount source cannot be specified for tmpfs. .</param>
        /// <param name="readOnly">Whether the mount should be read-only..</param>
        /// <param name="consistency">The consistency requirement for the mount: &#x60;default&#x60;, &#x60;consistent&#x60;, &#x60;cached&#x60;, or &#x60;delegated&#x60;..</param>
        /// <param name="bindOptions">bindOptions.</param>
        /// <param name="volumeOptions">volumeOptions.</param>
        /// <param name="tmpfsOptions">tmpfsOptions.</param>
        public DockerMount(string target = default(string), string source = default(string), TypeEnum? type = default(TypeEnum?), bool readOnly = default(bool), string consistency = default(string), DockerMountBindOptions bindOptions = default(DockerMountBindOptions), DockerMountVolumeOptions volumeOptions = default(DockerMountVolumeOptions), DockerMountTmpfsOptions tmpfsOptions = default(DockerMountTmpfsOptions))
        {
            this.Target = target;
            this.Source = source;
            this.Type = type;
            this.ReadOnly = readOnly;
            this.Consistency = consistency;
            this.BindOptions = bindOptions;
            this.VolumeOptions = volumeOptions;
            this.TmpfsOptions = tmpfsOptions;
        }
        
        /// <summary>
        /// Container path.
        /// </summary>
        /// <value>Container path.</value>
        [DataMember(Name="Target", EmitDefaultValue=false)]
        public string Target { get; set; }

        /// <summary>
        /// Mount source (e.g. a volume name, a host path).
        /// </summary>
        /// <value>Mount source (e.g. a volume name, a host path).</value>
        [DataMember(Name="Source", EmitDefaultValue=false)]
        public string Source { get; set; }


        /// <summary>
        /// Whether the mount should be read-only.
        /// </summary>
        /// <value>Whether the mount should be read-only.</value>
        [DataMember(Name="ReadOnly", EmitDefaultValue=false)]
        public bool ReadOnly { get; set; }

        /// <summary>
        /// The consistency requirement for the mount: &#x60;default&#x60;, &#x60;consistent&#x60;, &#x60;cached&#x60;, or &#x60;delegated&#x60;.
        /// </summary>
        /// <value>The consistency requirement for the mount: &#x60;default&#x60;, &#x60;consistent&#x60;, &#x60;cached&#x60;, or &#x60;delegated&#x60;.</value>
        [DataMember(Name="Consistency", EmitDefaultValue=false)]
        public string Consistency { get; set; }

        /// <summary>
        /// Gets or Sets BindOptions
        /// </summary>
        [DataMember(Name="BindOptions", EmitDefaultValue=false)]
        public DockerMountBindOptions BindOptions { get; set; }

        /// <summary>
        /// Gets or Sets VolumeOptions
        /// </summary>
        [DataMember(Name="VolumeOptions", EmitDefaultValue=false)]
        public DockerMountVolumeOptions VolumeOptions { get; set; }

        /// <summary>
        /// Gets or Sets TmpfsOptions
        /// </summary>
        [DataMember(Name="TmpfsOptions", EmitDefaultValue=false)]
        public DockerMountTmpfsOptions TmpfsOptions { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerMount {\n");
            sb.Append("  Target: ").Append(Target).Append("\n");
            sb.Append("  Source: ").Append(Source).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  ReadOnly: ").Append(ReadOnly).Append("\n");
            sb.Append("  Consistency: ").Append(Consistency).Append("\n");
            sb.Append("  BindOptions: ").Append(BindOptions).Append("\n");
            sb.Append("  VolumeOptions: ").Append(VolumeOptions).Append("\n");
            sb.Append("  TmpfsOptions: ").Append(TmpfsOptions).Append("\n");
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
            return this.Equals(input as DockerMount);
        }

        /// <summary>
        /// Returns true if DockerMount instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerMount to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerMount input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Target == input.Target ||
                    (this.Target != null &&
                    this.Target.Equals(input.Target))
                ) && 
                (
                    this.Source == input.Source ||
                    (this.Source != null &&
                    this.Source.Equals(input.Source))
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.ReadOnly == input.ReadOnly ||
                    (this.ReadOnly != null &&
                    this.ReadOnly.Equals(input.ReadOnly))
                ) && 
                (
                    this.Consistency == input.Consistency ||
                    (this.Consistency != null &&
                    this.Consistency.Equals(input.Consistency))
                ) && 
                (
                    this.BindOptions == input.BindOptions ||
                    (this.BindOptions != null &&
                    this.BindOptions.Equals(input.BindOptions))
                ) && 
                (
                    this.VolumeOptions == input.VolumeOptions ||
                    (this.VolumeOptions != null &&
                    this.VolumeOptions.Equals(input.VolumeOptions))
                ) && 
                (
                    this.TmpfsOptions == input.TmpfsOptions ||
                    (this.TmpfsOptions != null &&
                    this.TmpfsOptions.Equals(input.TmpfsOptions))
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
                if (this.Target != null)
                    hashCode = hashCode * 59 + this.Target.GetHashCode();
                if (this.Source != null)
                    hashCode = hashCode * 59 + this.Source.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.ReadOnly != null)
                    hashCode = hashCode * 59 + this.ReadOnly.GetHashCode();
                if (this.Consistency != null)
                    hashCode = hashCode * 59 + this.Consistency.GetHashCode();
                if (this.BindOptions != null)
                    hashCode = hashCode * 59 + this.BindOptions.GetHashCode();
                if (this.VolumeOptions != null)
                    hashCode = hashCode * 59 + this.VolumeOptions.GetHashCode();
                if (this.TmpfsOptions != null)
                    hashCode = hashCode * 59 + this.TmpfsOptions.GetHashCode();
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
