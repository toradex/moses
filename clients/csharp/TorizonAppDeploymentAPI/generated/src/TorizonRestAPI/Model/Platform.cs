/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.5
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
    /// Platform
    /// </summary>
    [DataContract]
    public partial class Platform :  IEquatable<Platform>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Platform" /> class.
        /// </summary>
        /// <param name="runtimes">runtimes/languages supported by the container.</param>
        /// <param name="sdkcontainerusername">ssh user supported by the SDK container.</param>
        /// <param name="sdkcontainerpassword">password used to ssh inside the SDK container.</param>
        /// <param name="dockercomposefile">path of docker-compose file to be used to start additional containers needed by the app.</param>
        /// <param name="startupscript">path of script to be run when application debugging starts.</param>
        /// <param name="shutdownscript">path of script to be run when application debugging stops.</param>
        /// <param name="ports">ports to be exposed from the container.</param>
        /// <param name="volumes">Local folders to be mounted as mount points inside a container.</param>
        /// <param name="devices">Additional devices to be shared inside container.</param>
        /// <param name="networks">Networks used by container (in debug it will always be also on bridge).</param>
        /// <param name="extraparms">Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML).</param>
        /// <param name="props">Custom properties (may be used in dockerfile or by extensions).</param>
        public Platform(List<string> runtimes = default(List<string>), string sdkcontainerusername = default(string), string sdkcontainerpassword = default(string), Dictionary<string, string> dockercomposefile = default(Dictionary<string, string>), Dictionary<string, string> startupscript = default(Dictionary<string, string>), Dictionary<string, string> shutdownscript = default(Dictionary<string, string>), Dictionary<string, Dictionary<string, string>> ports = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, Dictionary<string, string>> volumes = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, List<string>> devices = default(Dictionary<string, List<string>>), Dictionary<string, List<string>> networks = default(Dictionary<string, List<string>>), Dictionary<string, Dictionary<string, string>> extraparms = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, Dictionary<string, string>> props = default(Dictionary<string, Dictionary<string, string>>))
        {
            this.Runtimes = runtimes;
            this.Sdkcontainerusername = sdkcontainerusername;
            this.Sdkcontainerpassword = sdkcontainerpassword;
            this.Dockercomposefile = dockercomposefile;
            this.Startupscript = startupscript;
            this.Shutdownscript = shutdownscript;
            this.Ports = ports;
            this.Volumes = volumes;
            this.Devices = devices;
            this.Networks = networks;
            this.Extraparms = extraparms;
            this.Props = props;
        }

        /// <summary>
        /// Unique name (should be filesystem-compatible)
        /// </summary>
        /// <value>Unique name (should be filesystem-compatible)</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; private set; }

        /// <summary>
        /// Platform mnemnonic name
        /// </summary>
        /// <value>Platform mnemnonic name</value>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; private set; }

        /// <summary>
        /// true if the platform is provided by Toradex and can&#39;t be modified
        /// </summary>
        /// <value>true if the platform is provided by Toradex and can&#39;t be modified</value>
        [DataMember(Name="standard", EmitDefaultValue=false)]
        public bool Standard { get; private set; }

        /// <summary>
        /// Version of the image (not related to distro version)
        /// </summary>
        /// <value>Version of the image (not related to distro version)</value>
        [DataMember(Name="version", EmitDefaultValue=false)]
        public string _Version { get; private set; }

        /// <summary>
        /// runtimes/languages supported by the container
        /// </summary>
        /// <value>runtimes/languages supported by the container</value>
        [DataMember(Name="runtimes", EmitDefaultValue=false)]
        public List<string> Runtimes { get; set; }

        /// <summary>
        /// ssh user supported by the SDK container
        /// </summary>
        /// <value>ssh user supported by the SDK container</value>
        [DataMember(Name="sdkcontainerusername", EmitDefaultValue=false)]
        public string Sdkcontainerusername { get; set; }

        /// <summary>
        /// password used to ssh inside the SDK container
        /// </summary>
        /// <value>password used to ssh inside the SDK container</value>
        [DataMember(Name="sdkcontainerpassword", EmitDefaultValue=false)]
        public string Sdkcontainerpassword { get; set; }

        /// <summary>
        /// path of docker-compose file to be used to start additional containers needed by the app
        /// </summary>
        /// <value>path of docker-compose file to be used to start additional containers needed by the app</value>
        [DataMember(Name="dockercomposefile", EmitDefaultValue=false)]
        public Dictionary<string, string> Dockercomposefile { get; set; }

        /// <summary>
        /// path of script to be run when application debugging starts
        /// </summary>
        /// <value>path of script to be run when application debugging starts</value>
        [DataMember(Name="startupscript", EmitDefaultValue=false)]
        public Dictionary<string, string> Startupscript { get; set; }

        /// <summary>
        /// path of script to be run when application debugging stops
        /// </summary>
        /// <value>path of script to be run when application debugging stops</value>
        [DataMember(Name="shutdownscript", EmitDefaultValue=false)]
        public Dictionary<string, string> Shutdownscript { get; set; }

        /// <summary>
        /// ports to be exposed from the container
        /// </summary>
        /// <value>ports to be exposed from the container</value>
        [DataMember(Name="ports", EmitDefaultValue=false)]
        public Dictionary<string, Dictionary<string, string>> Ports { get; set; }

        /// <summary>
        /// Local folders to be mounted as mount points inside a container
        /// </summary>
        /// <value>Local folders to be mounted as mount points inside a container</value>
        [DataMember(Name="volumes", EmitDefaultValue=false)]
        public Dictionary<string, Dictionary<string, string>> Volumes { get; set; }

        /// <summary>
        /// Additional devices to be shared inside container
        /// </summary>
        /// <value>Additional devices to be shared inside container</value>
        [DataMember(Name="devices", EmitDefaultValue=false)]
        public Dictionary<string, List<string>> Devices { get; set; }

        /// <summary>
        /// Networks used by container (in debug it will always be also on bridge)
        /// </summary>
        /// <value>Networks used by container (in debug it will always be also on bridge)</value>
        [DataMember(Name="networks", EmitDefaultValue=false)]
        public Dictionary<string, List<string>> Networks { get; set; }

        /// <summary>
        /// Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)
        /// </summary>
        /// <value>Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)</value>
        [DataMember(Name="extraparms", EmitDefaultValue=false)]
        public Dictionary<string, Dictionary<string, string>> Extraparms { get; set; }

        /// <summary>
        /// Custom properties (may be used in dockerfile or by extensions)
        /// </summary>
        /// <value>Custom properties (may be used in dockerfile or by extensions)</value>
        [DataMember(Name="props", EmitDefaultValue=false)]
        public Dictionary<string, Dictionary<string, string>> Props { get; set; }

        /// <summary>
        /// Platform human-readable description
        /// </summary>
        /// <value>Platform human-readable description</value>
        [DataMember(Name="description", EmitDefaultValue=false)]
        public string Description { get; private set; }

        /// <summary>
        /// strings used to identify specific properties of the platform
        /// </summary>
        /// <value>strings used to identify specific properties of the platform</value>
        [DataMember(Name="tags", EmitDefaultValue=false)]
        public List<string> Tags { get; private set; }

        /// <summary>
        /// architecture as defined by docker
        /// </summary>
        /// <value>architecture as defined by docker</value>
        [DataMember(Name="architecture", EmitDefaultValue=false)]
        public string Architecture { get; private set; }

        /// <summary>
        /// true for platforms that are no longer supported
        /// </summary>
        /// <value>true for platforms that are no longer supported</value>
        [DataMember(Name="deprecated", EmitDefaultValue=false)]
        public bool Deprecated { get; private set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Platform {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Standard: ").Append(Standard).Append("\n");
            sb.Append("  _Version: ").Append(_Version).Append("\n");
            sb.Append("  Runtimes: ").Append(Runtimes).Append("\n");
            sb.Append("  Sdkcontainerusername: ").Append(Sdkcontainerusername).Append("\n");
            sb.Append("  Sdkcontainerpassword: ").Append(Sdkcontainerpassword).Append("\n");
            sb.Append("  Dockercomposefile: ").Append(Dockercomposefile).Append("\n");
            sb.Append("  Startupscript: ").Append(Startupscript).Append("\n");
            sb.Append("  Shutdownscript: ").Append(Shutdownscript).Append("\n");
            sb.Append("  Ports: ").Append(Ports).Append("\n");
            sb.Append("  Volumes: ").Append(Volumes).Append("\n");
            sb.Append("  Devices: ").Append(Devices).Append("\n");
            sb.Append("  Networks: ").Append(Networks).Append("\n");
            sb.Append("  Extraparms: ").Append(Extraparms).Append("\n");
            sb.Append("  Props: ").Append(Props).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  Tags: ").Append(Tags).Append("\n");
            sb.Append("  Architecture: ").Append(Architecture).Append("\n");
            sb.Append("  Deprecated: ").Append(Deprecated).Append("\n");
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
            return this.Equals(input as Platform);
        }

        /// <summary>
        /// Returns true if Platform instances are equal
        /// </summary>
        /// <param name="input">Instance of Platform to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Platform input)
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
                    this.Standard == input.Standard ||
                    (this.Standard != null &&
                    this.Standard.Equals(input.Standard))
                ) && 
                (
                    this._Version == input._Version ||
                    (this._Version != null &&
                    this._Version.Equals(input._Version))
                ) && 
                (
                    this.Runtimes == input.Runtimes ||
                    this.Runtimes != null &&
                    input.Runtimes != null &&
                    this.Runtimes.SequenceEqual(input.Runtimes)
                ) && 
                (
                    this.Sdkcontainerusername == input.Sdkcontainerusername ||
                    (this.Sdkcontainerusername != null &&
                    this.Sdkcontainerusername.Equals(input.Sdkcontainerusername))
                ) && 
                (
                    this.Sdkcontainerpassword == input.Sdkcontainerpassword ||
                    (this.Sdkcontainerpassword != null &&
                    this.Sdkcontainerpassword.Equals(input.Sdkcontainerpassword))
                ) && 
                (
                    this.Dockercomposefile == input.Dockercomposefile ||
                    this.Dockercomposefile != null &&
                    input.Dockercomposefile != null &&
                    this.Dockercomposefile.SequenceEqual(input.Dockercomposefile)
                ) && 
                (
                    this.Startupscript == input.Startupscript ||
                    this.Startupscript != null &&
                    input.Startupscript != null &&
                    this.Startupscript.SequenceEqual(input.Startupscript)
                ) && 
                (
                    this.Shutdownscript == input.Shutdownscript ||
                    this.Shutdownscript != null &&
                    input.Shutdownscript != null &&
                    this.Shutdownscript.SequenceEqual(input.Shutdownscript)
                ) && 
                (
                    this.Ports == input.Ports ||
                    this.Ports != null &&
                    input.Ports != null &&
                    this.Ports.SequenceEqual(input.Ports)
                ) && 
                (
                    this.Volumes == input.Volumes ||
                    this.Volumes != null &&
                    input.Volumes != null &&
                    this.Volumes.SequenceEqual(input.Volumes)
                ) && 
                (
                    this.Devices == input.Devices ||
                    this.Devices != null &&
                    input.Devices != null &&
                    this.Devices.SequenceEqual(input.Devices)
                ) && 
                (
                    this.Networks == input.Networks ||
                    this.Networks != null &&
                    input.Networks != null &&
                    this.Networks.SequenceEqual(input.Networks)
                ) && 
                (
                    this.Extraparms == input.Extraparms ||
                    this.Extraparms != null &&
                    input.Extraparms != null &&
                    this.Extraparms.SequenceEqual(input.Extraparms)
                ) && 
                (
                    this.Props == input.Props ||
                    this.Props != null &&
                    input.Props != null &&
                    this.Props.SequenceEqual(input.Props)
                ) && 
                (
                    this.Description == input.Description ||
                    (this.Description != null &&
                    this.Description.Equals(input.Description))
                ) && 
                (
                    this.Tags == input.Tags ||
                    this.Tags != null &&
                    input.Tags != null &&
                    this.Tags.SequenceEqual(input.Tags)
                ) && 
                (
                    this.Architecture == input.Architecture ||
                    (this.Architecture != null &&
                    this.Architecture.Equals(input.Architecture))
                ) && 
                (
                    this.Deprecated == input.Deprecated ||
                    (this.Deprecated != null &&
                    this.Deprecated.Equals(input.Deprecated))
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
                if (this.Standard != null)
                    hashCode = hashCode * 59 + this.Standard.GetHashCode();
                if (this._Version != null)
                    hashCode = hashCode * 59 + this._Version.GetHashCode();
                if (this.Runtimes != null)
                    hashCode = hashCode * 59 + this.Runtimes.GetHashCode();
                if (this.Sdkcontainerusername != null)
                    hashCode = hashCode * 59 + this.Sdkcontainerusername.GetHashCode();
                if (this.Sdkcontainerpassword != null)
                    hashCode = hashCode * 59 + this.Sdkcontainerpassword.GetHashCode();
                if (this.Dockercomposefile != null)
                    hashCode = hashCode * 59 + this.Dockercomposefile.GetHashCode();
                if (this.Startupscript != null)
                    hashCode = hashCode * 59 + this.Startupscript.GetHashCode();
                if (this.Shutdownscript != null)
                    hashCode = hashCode * 59 + this.Shutdownscript.GetHashCode();
                if (this.Ports != null)
                    hashCode = hashCode * 59 + this.Ports.GetHashCode();
                if (this.Volumes != null)
                    hashCode = hashCode * 59 + this.Volumes.GetHashCode();
                if (this.Devices != null)
                    hashCode = hashCode * 59 + this.Devices.GetHashCode();
                if (this.Networks != null)
                    hashCode = hashCode * 59 + this.Networks.GetHashCode();
                if (this.Extraparms != null)
                    hashCode = hashCode * 59 + this.Extraparms.GetHashCode();
                if (this.Props != null)
                    hashCode = hashCode * 59 + this.Props.GetHashCode();
                if (this.Description != null)
                    hashCode = hashCode * 59 + this.Description.GetHashCode();
                if (this.Tags != null)
                    hashCode = hashCode * 59 + this.Tags.GetHashCode();
                if (this.Architecture != null)
                    hashCode = hashCode * 59 + this.Architecture.GetHashCode();
                if (this.Deprecated != null)
                    hashCode = hashCode * 59 + this.Deprecated.GetHashCode();
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
