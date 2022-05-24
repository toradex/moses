/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.6
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
    /// TargetDevice
    /// </summary>
    [DataContract]
    public partial class TargetDevice :  IEquatable<TargetDevice>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TargetDevice" /> class.
        /// </summary>
        /// <param name="name">Device mnemnonic name.</param>
        /// <param name="hostname">Device host name.</param>
        /// <param name="username">User account used to connect to device via ssh.</param>
        /// <param name="homefolder">Home folder of ssh user (used to deploy files and apps, can be different from actual home).</param>
        /// <param name="runningtorizon">True for a target device that is a community device, false for default Toradex devices.</param>
        /// <param name="cpuArchitecture">CPU architecture.</param>
        /// <param name="modelDescription">detailed model description.</param>
        public TargetDevice(string name = default(string), string hostname = default(string), string username = default(string), string homefolder = default(string), bool runningtorizon = default(bool), string cpuArchitecture = default(string), string modelDescription = default(string))
        {
            this.Name = name;
            this.Hostname = hostname;
            this.Username = username;
            this.Homefolder = homefolder;
            this.Runningtorizon = runningtorizon;
            this.CpuArchitecture = cpuArchitecture;
            this.ModelDescription = modelDescription;
        }

        /// <summary>
        /// Unique serial number
        /// </summary>
        /// <value>Unique serial number</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; private set; }

        /// <summary>
        /// Device mnemnonic name
        /// </summary>
        /// <value>Device mnemnonic name</value>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Device hardware ID
        /// </summary>
        /// <value>Device hardware ID</value>
        [DataMember(Name="model", EmitDefaultValue=false)]
        public string Model { get; private set; }

        /// <summary>
        /// Device hardware revision
        /// </summary>
        /// <value>Device hardware revision</value>
        [DataMember(Name="hwrev", EmitDefaultValue=false)]
        public string Hwrev { get; private set; }

        /// <summary>
        /// Kernel name
        /// </summary>
        /// <value>Kernel name</value>
        [DataMember(Name="kernelversion", EmitDefaultValue=false)]
        public string Kernelversion { get; private set; }

        /// <summary>
        /// Kernel release
        /// </summary>
        /// <value>Kernel release</value>
        [DataMember(Name="kernelrelease", EmitDefaultValue=false)]
        public string Kernelrelease { get; private set; }

        /// <summary>
        /// Torizon version (date)
        /// </summary>
        /// <value>Torizon version (date)</value>
        [DataMember(Name="distroversion", EmitDefaultValue=false)]
        public string Distroversion { get; private set; }

        /// <summary>
        /// Device host name
        /// </summary>
        /// <value>Device host name</value>
        [DataMember(Name="hostname", EmitDefaultValue=false)]
        public string Hostname { get; set; }

        /// <summary>
        /// User account used to connect to device via ssh
        /// </summary>
        /// <value>User account used to connect to device via ssh</value>
        [DataMember(Name="username", EmitDefaultValue=false)]
        public string Username { get; set; }

        /// <summary>
        /// Home folder of ssh user (used to deploy files and apps, can be different from actual home)
        /// </summary>
        /// <value>Home folder of ssh user (used to deploy files and apps, can be different from actual home)</value>
        [DataMember(Name="homefolder", EmitDefaultValue=false)]
        public string Homefolder { get; set; }

        /// <summary>
        /// True for a target device that is a community device, false for default Toradex devices
        /// </summary>
        /// <value>True for a target device that is a community device, false for default Toradex devices</value>
        [DataMember(Name="runningtorizon", EmitDefaultValue=false)]
        public bool Runningtorizon { get; set; }

        /// <summary>
        /// CPU architecture
        /// </summary>
        /// <value>CPU architecture</value>
        [DataMember(Name="cpu_architecture", EmitDefaultValue=false)]
        public string CpuArchitecture { get; set; }

        /// <summary>
        /// detailed model description
        /// </summary>
        /// <value>detailed model description</value>
        [DataMember(Name="model_description", EmitDefaultValue=false)]
        public string ModelDescription { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TargetDevice {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Model: ").Append(Model).Append("\n");
            sb.Append("  Hwrev: ").Append(Hwrev).Append("\n");
            sb.Append("  Kernelversion: ").Append(Kernelversion).Append("\n");
            sb.Append("  Kernelrelease: ").Append(Kernelrelease).Append("\n");
            sb.Append("  Distroversion: ").Append(Distroversion).Append("\n");
            sb.Append("  Hostname: ").Append(Hostname).Append("\n");
            sb.Append("  Username: ").Append(Username).Append("\n");
            sb.Append("  Homefolder: ").Append(Homefolder).Append("\n");
            sb.Append("  Runningtorizon: ").Append(Runningtorizon).Append("\n");
            sb.Append("  CpuArchitecture: ").Append(CpuArchitecture).Append("\n");
            sb.Append("  ModelDescription: ").Append(ModelDescription).Append("\n");
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
            return this.Equals(input as TargetDevice);
        }

        /// <summary>
        /// Returns true if TargetDevice instances are equal
        /// </summary>
        /// <param name="input">Instance of TargetDevice to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TargetDevice input)
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
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Model == input.Model ||
                    (this.Model != null &&
                    this.Model.Equals(input.Model))
                ) && 
                (
                    this.Hwrev == input.Hwrev ||
                    (this.Hwrev != null &&
                    this.Hwrev.Equals(input.Hwrev))
                ) && 
                (
                    this.Kernelversion == input.Kernelversion ||
                    (this.Kernelversion != null &&
                    this.Kernelversion.Equals(input.Kernelversion))
                ) && 
                (
                    this.Kernelrelease == input.Kernelrelease ||
                    (this.Kernelrelease != null &&
                    this.Kernelrelease.Equals(input.Kernelrelease))
                ) && 
                (
                    this.Distroversion == input.Distroversion ||
                    (this.Distroversion != null &&
                    this.Distroversion.Equals(input.Distroversion))
                ) && 
                (
                    this.Hostname == input.Hostname ||
                    (this.Hostname != null &&
                    this.Hostname.Equals(input.Hostname))
                ) && 
                (
                    this.Username == input.Username ||
                    (this.Username != null &&
                    this.Username.Equals(input.Username))
                ) && 
                (
                    this.Homefolder == input.Homefolder ||
                    (this.Homefolder != null &&
                    this.Homefolder.Equals(input.Homefolder))
                ) && 
                (
                    this.Runningtorizon == input.Runningtorizon ||
                    (this.Runningtorizon != null &&
                    this.Runningtorizon.Equals(input.Runningtorizon))
                ) && 
                (
                    this.CpuArchitecture == input.CpuArchitecture ||
                    (this.CpuArchitecture != null &&
                    this.CpuArchitecture.Equals(input.CpuArchitecture))
                ) && 
                (
                    this.ModelDescription == input.ModelDescription ||
                    (this.ModelDescription != null &&
                    this.ModelDescription.Equals(input.ModelDescription))
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
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Model != null)
                    hashCode = hashCode * 59 + this.Model.GetHashCode();
                if (this.Hwrev != null)
                    hashCode = hashCode * 59 + this.Hwrev.GetHashCode();
                if (this.Kernelversion != null)
                    hashCode = hashCode * 59 + this.Kernelversion.GetHashCode();
                if (this.Kernelrelease != null)
                    hashCode = hashCode * 59 + this.Kernelrelease.GetHashCode();
                if (this.Distroversion != null)
                    hashCode = hashCode * 59 + this.Distroversion.GetHashCode();
                if (this.Hostname != null)
                    hashCode = hashCode * 59 + this.Hostname.GetHashCode();
                if (this.Username != null)
                    hashCode = hashCode * 59 + this.Username.GetHashCode();
                if (this.Homefolder != null)
                    hashCode = hashCode * 59 + this.Homefolder.GetHashCode();
                if (this.Runningtorizon != null)
                    hashCode = hashCode * 59 + this.Runningtorizon.GetHashCode();
                if (this.CpuArchitecture != null)
                    hashCode = hashCode * 59 + this.CpuArchitecture.GetHashCode();
                if (this.ModelDescription != null)
                    hashCode = hashCode * 59 + this.ModelDescription.GetHashCode();
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
