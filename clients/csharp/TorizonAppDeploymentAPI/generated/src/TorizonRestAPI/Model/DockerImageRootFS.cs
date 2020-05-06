/* 
 * Torizon Deployment API
 *
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.2
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
    /// DockerImageRootFS
    /// </summary>
    [DataContract]
    public partial class DockerImageRootFS :  IEquatable<DockerImageRootFS>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerImageRootFS" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected DockerImageRootFS() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerImageRootFS" /> class.
        /// </summary>
        /// <param name="type">type (required).</param>
        /// <param name="layers">layers.</param>
        /// <param name="baseLayer">baseLayer.</param>
        public DockerImageRootFS(string type = default(string), List<string> layers = default(List<string>), string baseLayer = default(string))
        {
            // to ensure "type" is required (not null)
            if (type == null)
            {
                throw new InvalidDataException("type is a required property for DockerImageRootFS and cannot be null");
            }
            else
            {
                this.Type = type;
            }
            
            this.Layers = layers;
            this.BaseLayer = baseLayer;
        }
        
        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="Type", EmitDefaultValue=false)]
        public string Type { get; set; }

        /// <summary>
        /// Gets or Sets Layers
        /// </summary>
        [DataMember(Name="Layers", EmitDefaultValue=false)]
        public List<string> Layers { get; set; }

        /// <summary>
        /// Gets or Sets BaseLayer
        /// </summary>
        [DataMember(Name="BaseLayer", EmitDefaultValue=false)]
        public string BaseLayer { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerImageRootFS {\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Layers: ").Append(Layers).Append("\n");
            sb.Append("  BaseLayer: ").Append(BaseLayer).Append("\n");
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
            return this.Equals(input as DockerImageRootFS);
        }

        /// <summary>
        /// Returns true if DockerImageRootFS instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerImageRootFS to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerImageRootFS input)
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
                    this.Layers == input.Layers ||
                    this.Layers != null &&
                    input.Layers != null &&
                    this.Layers.SequenceEqual(input.Layers)
                ) && 
                (
                    this.BaseLayer == input.BaseLayer ||
                    (this.BaseLayer != null &&
                    this.BaseLayer.Equals(input.BaseLayer))
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
                if (this.Layers != null)
                    hashCode = hashCode * 59 + this.Layers.GetHashCode();
                if (this.BaseLayer != null)
                    hashCode = hashCode * 59 + this.BaseLayer.GetHashCode();
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
