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
    /// Configuration for a network endpoint.
    /// </summary>
    [DataContract]
    public partial class DockerEndpointSettings :  IEquatable<DockerEndpointSettings>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerEndpointSettings" /> class.
        /// </summary>
        /// <param name="iPAMConfig">iPAMConfig.</param>
        /// <param name="links">links.</param>
        /// <param name="aliases">aliases.</param>
        /// <param name="networkID">Unique ID of the network. .</param>
        /// <param name="endpointID">Unique ID for the service endpoint in a Sandbox. .</param>
        /// <param name="gateway">Gateway address for this network. .</param>
        /// <param name="iPAddress">IPv4 address. .</param>
        /// <param name="iPPrefixLen">Mask length of the IPv4 address. .</param>
        /// <param name="iPv6Gateway">IPv6 gateway address. .</param>
        /// <param name="globalIPv6Address">Global IPv6 address. .</param>
        /// <param name="globalIPv6PrefixLen">Mask length of the global IPv6 address. .</param>
        /// <param name="macAddress">MAC address for the endpoint on this network. .</param>
        /// <param name="driverOpts">DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific. .</param>
        public DockerEndpointSettings(DockerEndpointIPAMConfig iPAMConfig = default(DockerEndpointIPAMConfig), List<string> links = default(List<string>), List<string> aliases = default(List<string>), string networkID = default(string), string endpointID = default(string), string gateway = default(string), string iPAddress = default(string), int iPPrefixLen = default(int), string iPv6Gateway = default(string), string globalIPv6Address = default(string), long globalIPv6PrefixLen = default(long), string macAddress = default(string), Dictionary<string, string> driverOpts = default(Dictionary<string, string>))
        {
            this.IPAMConfig = iPAMConfig;
            this.DriverOpts = driverOpts;
            this.IPAMConfig = iPAMConfig;
            this.Links = links;
            this.Aliases = aliases;
            this.NetworkID = networkID;
            this.EndpointID = endpointID;
            this.Gateway = gateway;
            this.IPAddress = iPAddress;
            this.IPPrefixLen = iPPrefixLen;
            this.IPv6Gateway = iPv6Gateway;
            this.GlobalIPv6Address = globalIPv6Address;
            this.GlobalIPv6PrefixLen = globalIPv6PrefixLen;
            this.MacAddress = macAddress;
            this.DriverOpts = driverOpts;
        }
        
        /// <summary>
        /// Gets or Sets IPAMConfig
        /// </summary>
        [DataMember(Name="IPAMConfig", EmitDefaultValue=true)]
        public DockerEndpointIPAMConfig IPAMConfig { get; set; }

        /// <summary>
        /// Gets or Sets Links
        /// </summary>
        [DataMember(Name="Links", EmitDefaultValue=false)]
        public List<string> Links { get; set; }

        /// <summary>
        /// Gets or Sets Aliases
        /// </summary>
        [DataMember(Name="Aliases", EmitDefaultValue=false)]
        public List<string> Aliases { get; set; }

        /// <summary>
        /// Unique ID of the network. 
        /// </summary>
        /// <value>Unique ID of the network. </value>
        [DataMember(Name="NetworkID", EmitDefaultValue=false)]
        public string NetworkID { get; set; }

        /// <summary>
        /// Unique ID for the service endpoint in a Sandbox. 
        /// </summary>
        /// <value>Unique ID for the service endpoint in a Sandbox. </value>
        [DataMember(Name="EndpointID", EmitDefaultValue=false)]
        public string EndpointID { get; set; }

        /// <summary>
        /// Gateway address for this network. 
        /// </summary>
        /// <value>Gateway address for this network. </value>
        [DataMember(Name="Gateway", EmitDefaultValue=false)]
        public string Gateway { get; set; }

        /// <summary>
        /// IPv4 address. 
        /// </summary>
        /// <value>IPv4 address. </value>
        [DataMember(Name="IPAddress", EmitDefaultValue=false)]
        public string IPAddress { get; set; }

        /// <summary>
        /// Mask length of the IPv4 address. 
        /// </summary>
        /// <value>Mask length of the IPv4 address. </value>
        [DataMember(Name="IPPrefixLen", EmitDefaultValue=false)]
        public int IPPrefixLen { get; set; }

        /// <summary>
        /// IPv6 gateway address. 
        /// </summary>
        /// <value>IPv6 gateway address. </value>
        [DataMember(Name="IPv6Gateway", EmitDefaultValue=false)]
        public string IPv6Gateway { get; set; }

        /// <summary>
        /// Global IPv6 address. 
        /// </summary>
        /// <value>Global IPv6 address. </value>
        [DataMember(Name="GlobalIPv6Address", EmitDefaultValue=false)]
        public string GlobalIPv6Address { get; set; }

        /// <summary>
        /// Mask length of the global IPv6 address. 
        /// </summary>
        /// <value>Mask length of the global IPv6 address. </value>
        [DataMember(Name="GlobalIPv6PrefixLen", EmitDefaultValue=false)]
        public long GlobalIPv6PrefixLen { get; set; }

        /// <summary>
        /// MAC address for the endpoint on this network. 
        /// </summary>
        /// <value>MAC address for the endpoint on this network. </value>
        [DataMember(Name="MacAddress", EmitDefaultValue=false)]
        public string MacAddress { get; set; }

        /// <summary>
        /// DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific. 
        /// </summary>
        /// <value>DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific. </value>
        [DataMember(Name="DriverOpts", EmitDefaultValue=true)]
        public Dictionary<string, string> DriverOpts { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerEndpointSettings {\n");
            sb.Append("  IPAMConfig: ").Append(IPAMConfig).Append("\n");
            sb.Append("  Links: ").Append(Links).Append("\n");
            sb.Append("  Aliases: ").Append(Aliases).Append("\n");
            sb.Append("  NetworkID: ").Append(NetworkID).Append("\n");
            sb.Append("  EndpointID: ").Append(EndpointID).Append("\n");
            sb.Append("  Gateway: ").Append(Gateway).Append("\n");
            sb.Append("  IPAddress: ").Append(IPAddress).Append("\n");
            sb.Append("  IPPrefixLen: ").Append(IPPrefixLen).Append("\n");
            sb.Append("  IPv6Gateway: ").Append(IPv6Gateway).Append("\n");
            sb.Append("  GlobalIPv6Address: ").Append(GlobalIPv6Address).Append("\n");
            sb.Append("  GlobalIPv6PrefixLen: ").Append(GlobalIPv6PrefixLen).Append("\n");
            sb.Append("  MacAddress: ").Append(MacAddress).Append("\n");
            sb.Append("  DriverOpts: ").Append(DriverOpts).Append("\n");
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
            return this.Equals(input as DockerEndpointSettings);
        }

        /// <summary>
        /// Returns true if DockerEndpointSettings instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerEndpointSettings to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerEndpointSettings input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.IPAMConfig == input.IPAMConfig ||
                    (this.IPAMConfig != null &&
                    this.IPAMConfig.Equals(input.IPAMConfig))
                ) && 
                (
                    this.Links == input.Links ||
                    this.Links != null &&
                    input.Links != null &&
                    this.Links.SequenceEqual(input.Links)
                ) && 
                (
                    this.Aliases == input.Aliases ||
                    this.Aliases != null &&
                    input.Aliases != null &&
                    this.Aliases.SequenceEqual(input.Aliases)
                ) && 
                (
                    this.NetworkID == input.NetworkID ||
                    (this.NetworkID != null &&
                    this.NetworkID.Equals(input.NetworkID))
                ) && 
                (
                    this.EndpointID == input.EndpointID ||
                    (this.EndpointID != null &&
                    this.EndpointID.Equals(input.EndpointID))
                ) && 
                (
                    this.Gateway == input.Gateway ||
                    (this.Gateway != null &&
                    this.Gateway.Equals(input.Gateway))
                ) && 
                (
                    this.IPAddress == input.IPAddress ||
                    (this.IPAddress != null &&
                    this.IPAddress.Equals(input.IPAddress))
                ) && 
                (
                    this.IPPrefixLen == input.IPPrefixLen ||
                    (this.IPPrefixLen != null &&
                    this.IPPrefixLen.Equals(input.IPPrefixLen))
                ) && 
                (
                    this.IPv6Gateway == input.IPv6Gateway ||
                    (this.IPv6Gateway != null &&
                    this.IPv6Gateway.Equals(input.IPv6Gateway))
                ) && 
                (
                    this.GlobalIPv6Address == input.GlobalIPv6Address ||
                    (this.GlobalIPv6Address != null &&
                    this.GlobalIPv6Address.Equals(input.GlobalIPv6Address))
                ) && 
                (
                    this.GlobalIPv6PrefixLen == input.GlobalIPv6PrefixLen ||
                    (this.GlobalIPv6PrefixLen != null &&
                    this.GlobalIPv6PrefixLen.Equals(input.GlobalIPv6PrefixLen))
                ) && 
                (
                    this.MacAddress == input.MacAddress ||
                    (this.MacAddress != null &&
                    this.MacAddress.Equals(input.MacAddress))
                ) && 
                (
                    this.DriverOpts == input.DriverOpts ||
                    this.DriverOpts != null &&
                    input.DriverOpts != null &&
                    this.DriverOpts.SequenceEqual(input.DriverOpts)
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
                if (this.IPAMConfig != null)
                    hashCode = hashCode * 59 + this.IPAMConfig.GetHashCode();
                if (this.Links != null)
                    hashCode = hashCode * 59 + this.Links.GetHashCode();
                if (this.Aliases != null)
                    hashCode = hashCode * 59 + this.Aliases.GetHashCode();
                if (this.NetworkID != null)
                    hashCode = hashCode * 59 + this.NetworkID.GetHashCode();
                if (this.EndpointID != null)
                    hashCode = hashCode * 59 + this.EndpointID.GetHashCode();
                if (this.Gateway != null)
                    hashCode = hashCode * 59 + this.Gateway.GetHashCode();
                if (this.IPAddress != null)
                    hashCode = hashCode * 59 + this.IPAddress.GetHashCode();
                if (this.IPPrefixLen != null)
                    hashCode = hashCode * 59 + this.IPPrefixLen.GetHashCode();
                if (this.IPv6Gateway != null)
                    hashCode = hashCode * 59 + this.IPv6Gateway.GetHashCode();
                if (this.GlobalIPv6Address != null)
                    hashCode = hashCode * 59 + this.GlobalIPv6Address.GetHashCode();
                if (this.GlobalIPv6PrefixLen != null)
                    hashCode = hashCode * 59 + this.GlobalIPv6PrefixLen.GetHashCode();
                if (this.MacAddress != null)
                    hashCode = hashCode * 59 + this.MacAddress.GetHashCode();
                if (this.DriverOpts != null)
                    hashCode = hashCode * 59 + this.DriverOpts.GetHashCode();
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
