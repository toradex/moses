/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.6
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
    /// MemInfo
    /// </summary>
    [DataContract]
    public partial class MemInfo :  IEquatable<MemInfo>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MemInfo" /> class.
        /// </summary>
        /// <param name="total">total memory in kb.</param>
        /// <param name="available">available memory in kb.</param>
        /// <param name="free">free memory in kb.</param>
        public MemInfo(decimal total = default(decimal), decimal available = default(decimal), decimal free = default(decimal))
        {
            this.Total = total;
            this.Available = available;
            this.Free = free;
        }
        
        /// <summary>
        /// total memory in kb
        /// </summary>
        /// <value>total memory in kb</value>
        [DataMember(Name="total", EmitDefaultValue=false)]
        public decimal Total { get; set; }

        /// <summary>
        /// available memory in kb
        /// </summary>
        /// <value>available memory in kb</value>
        [DataMember(Name="available", EmitDefaultValue=false)]
        public decimal Available { get; set; }

        /// <summary>
        /// free memory in kb
        /// </summary>
        /// <value>free memory in kb</value>
        [DataMember(Name="free", EmitDefaultValue=false)]
        public decimal Free { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MemInfo {\n");
            sb.Append("  Total: ").Append(Total).Append("\n");
            sb.Append("  Available: ").Append(Available).Append("\n");
            sb.Append("  Free: ").Append(Free).Append("\n");
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
            return this.Equals(input as MemInfo);
        }

        /// <summary>
        /// Returns true if MemInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of MemInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MemInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Total == input.Total ||
                    (this.Total != null &&
                    this.Total.Equals(input.Total))
                ) && 
                (
                    this.Available == input.Available ||
                    (this.Available != null &&
                    this.Available.Equals(input.Available))
                ) && 
                (
                    this.Free == input.Free ||
                    (this.Free != null &&
                    this.Free.Equals(input.Free))
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
                if (this.Total != null)
                    hashCode = hashCode * 59 + this.Total.GetHashCode();
                if (this.Available != null)
                    hashCode = hashCode * 59 + this.Available.GetHashCode();
                if (this.Free != null)
                    hashCode = hashCode * 59 + this.Free.GetHashCode();
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
