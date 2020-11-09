/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.11
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
    /// EndpointIPAMConfig represents an endpoint&#39;s IPAM configuration. 
    /// </summary>
    [DataContract]
    public partial class DockerEndpointIPAMConfig :  IEquatable<DockerEndpointIPAMConfig>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerEndpointIPAMConfig" /> class.
        /// </summary>
        /// <param name="iPv4Address">iPv4Address.</param>
        /// <param name="iPv6Address">iPv6Address.</param>
        /// <param name="linkLocalIPs">linkLocalIPs.</param>
        public DockerEndpointIPAMConfig(string iPv4Address = default(string), string iPv6Address = default(string), List<string> linkLocalIPs = default(List<string>))
        {
            this.IPv4Address = iPv4Address;
            this.IPv6Address = iPv6Address;
            this.LinkLocalIPs = linkLocalIPs;
        }
        
        /// <summary>
        /// Gets or Sets IPv4Address
        /// </summary>
        [DataMember(Name="IPv4Address", EmitDefaultValue=false)]
        public string IPv4Address { get; set; }

        /// <summary>
        /// Gets or Sets IPv6Address
        /// </summary>
        [DataMember(Name="IPv6Address", EmitDefaultValue=false)]
        public string IPv6Address { get; set; }

        /// <summary>
        /// Gets or Sets LinkLocalIPs
        /// </summary>
        [DataMember(Name="LinkLocalIPs", EmitDefaultValue=false)]
        public List<string> LinkLocalIPs { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerEndpointIPAMConfig {\n");
            sb.Append("  IPv4Address: ").Append(IPv4Address).Append("\n");
            sb.Append("  IPv6Address: ").Append(IPv6Address).Append("\n");
            sb.Append("  LinkLocalIPs: ").Append(LinkLocalIPs).Append("\n");
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
            return this.Equals(input as DockerEndpointIPAMConfig);
        }

        /// <summary>
        /// Returns true if DockerEndpointIPAMConfig instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerEndpointIPAMConfig to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerEndpointIPAMConfig input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.IPv4Address == input.IPv4Address ||
                    (this.IPv4Address != null &&
                    this.IPv4Address.Equals(input.IPv4Address))
                ) && 
                (
                    this.IPv6Address == input.IPv6Address ||
                    (this.IPv6Address != null &&
                    this.IPv6Address.Equals(input.IPv6Address))
                ) && 
                (
                    this.LinkLocalIPs == input.LinkLocalIPs ||
                    this.LinkLocalIPs != null &&
                    input.LinkLocalIPs != null &&
                    this.LinkLocalIPs.SequenceEqual(input.LinkLocalIPs)
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
                if (this.IPv4Address != null)
                    hashCode = hashCode * 59 + this.IPv4Address.GetHashCode();
                if (this.IPv6Address != null)
                    hashCode = hashCode * 59 + this.IPv6Address.GetHashCode();
                if (this.LinkLocalIPs != null)
                    hashCode = hashCode * 59 + this.LinkLocalIPs.GetHashCode();
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
