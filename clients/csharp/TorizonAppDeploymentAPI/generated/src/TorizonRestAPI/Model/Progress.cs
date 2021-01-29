/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.0
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
    /// Progress
    /// </summary>
    [DataContract]
    public partial class Progress :  IEquatable<Progress>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Progress" /> class.
        /// </summary>
        /// <param name="pending">true as long as operation is pending.</param>
        /// <param name="result">result.</param>
        public Progress(bool pending = default(bool), ErrorInfo result = default(ErrorInfo))
        {
            this.Pending = pending;
            this.Result = result;
        }
        
        /// <summary>
        /// cookie
        /// </summary>
        /// <value>cookie</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; private set; }

        /// <summary>
        /// 0%-100%
        /// </summary>
        /// <value>0%-100%</value>
        [DataMember(Name="progress", EmitDefaultValue=false)]
        public int _Progress { get; private set; }

        /// <summary>
        /// Gets or Sets Messages
        /// </summary>
        [DataMember(Name="messages", EmitDefaultValue=false)]
        public List<string> Messages { get; private set; }

        /// <summary>
        /// true as long as operation is pending
        /// </summary>
        /// <value>true as long as operation is pending</value>
        [DataMember(Name="pending", EmitDefaultValue=false)]
        public bool Pending { get; set; }

        /// <summary>
        /// Gets or Sets Result
        /// </summary>
        [DataMember(Name="result", EmitDefaultValue=false)]
        public ErrorInfo Result { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Progress {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  _Progress: ").Append(_Progress).Append("\n");
            sb.Append("  Messages: ").Append(Messages).Append("\n");
            sb.Append("  Pending: ").Append(Pending).Append("\n");
            sb.Append("  Result: ").Append(Result).Append("\n");
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
            return this.Equals(input as Progress);
        }

        /// <summary>
        /// Returns true if Progress instances are equal
        /// </summary>
        /// <param name="input">Instance of Progress to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Progress input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this._Progress == input._Progress ||
                    (this._Progress != null &&
                    this._Progress.Equals(input._Progress))
                ) && 
                (
                    this.Messages == input.Messages ||
                    this.Messages != null &&
                    input.Messages != null &&
                    this.Messages.SequenceEqual(input.Messages)
                ) && 
                (
                    this.Pending == input.Pending ||
                    (this.Pending != null &&
                    this.Pending.Equals(input.Pending))
                ) && 
                (
                    this.Result == input.Result ||
                    (this.Result != null &&
                    this.Result.Equals(input.Result))
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
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this._Progress != null)
                    hashCode = hashCode * 59 + this._Progress.GetHashCode();
                if (this.Messages != null)
                    hashCode = hashCode * 59 + this.Messages.GetHashCode();
                if (this.Pending != null)
                    hashCode = hashCode * 59 + this.Pending.GetHashCode();
                if (this.Result != null)
                    hashCode = hashCode * 59 + this.Result.GetHashCode();
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
