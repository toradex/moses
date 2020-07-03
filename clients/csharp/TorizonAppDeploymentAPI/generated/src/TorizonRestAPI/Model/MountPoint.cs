/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.5
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
    /// MountPoint
    /// </summary>
    [DataContract]
    public partial class MountPoint :  IEquatable<MountPoint>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MountPoint" /> class.
        /// </summary>
        /// <param name="mountpoint">mount point.</param>
        /// <param name="filesystem">file system.</param>
        /// <param name="size">total size in 1Kb blocks.</param>
        /// <param name="available">available space in 1kb blocks.</param>
        public MountPoint(string mountpoint = default(string), string filesystem = default(string), int size = default(int), int available = default(int))
        {
            this._Mountpoint = mountpoint;
            this.Filesystem = filesystem;
            this.Size = size;
            this.Available = available;
        }
        
        /// <summary>
        /// mount point
        /// </summary>
        /// <value>mount point</value>
        [DataMember(Name="mountpoint", EmitDefaultValue=false)]
        public string _Mountpoint { get; set; }

        /// <summary>
        /// file system
        /// </summary>
        /// <value>file system</value>
        [DataMember(Name="filesystem", EmitDefaultValue=false)]
        public string Filesystem { get; set; }

        /// <summary>
        /// total size in 1Kb blocks
        /// </summary>
        /// <value>total size in 1Kb blocks</value>
        [DataMember(Name="size", EmitDefaultValue=false)]
        public int Size { get; set; }

        /// <summary>
        /// available space in 1kb blocks
        /// </summary>
        /// <value>available space in 1kb blocks</value>
        [DataMember(Name="available", EmitDefaultValue=false)]
        public int Available { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MountPoint {\n");
            sb.Append("  _Mountpoint: ").Append(_Mountpoint).Append("\n");
            sb.Append("  Filesystem: ").Append(Filesystem).Append("\n");
            sb.Append("  Size: ").Append(Size).Append("\n");
            sb.Append("  Available: ").Append(Available).Append("\n");
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
            return this.Equals(input as MountPoint);
        }

        /// <summary>
        /// Returns true if MountPoint instances are equal
        /// </summary>
        /// <param name="input">Instance of MountPoint to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MountPoint input)
        {
            if (input == null)
                return false;

            return 
                (
                    this._Mountpoint == input._Mountpoint ||
                    (this._Mountpoint != null &&
                    this._Mountpoint.Equals(input._Mountpoint))
                ) && 
                (
                    this.Filesystem == input.Filesystem ||
                    (this.Filesystem != null &&
                    this.Filesystem.Equals(input.Filesystem))
                ) && 
                (
                    this.Size == input.Size ||
                    (this.Size != null &&
                    this.Size.Equals(input.Size))
                ) && 
                (
                    this.Available == input.Available ||
                    (this.Available != null &&
                    this.Available.Equals(input.Available))
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
                if (this._Mountpoint != null)
                    hashCode = hashCode * 59 + this._Mountpoint.GetHashCode();
                if (this.Filesystem != null)
                    hashCode = hashCode * 59 + this.Filesystem.GetHashCode();
                if (this.Size != null)
                    hashCode = hashCode * 59 + this.Size.GetHashCode();
                if (this.Available != null)
                    hashCode = hashCode * 59 + this.Available.GetHashCode();
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
