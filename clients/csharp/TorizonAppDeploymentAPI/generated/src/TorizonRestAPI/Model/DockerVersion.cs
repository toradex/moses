/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.9
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
    /// Information about docker version
    /// </summary>
    [DataContract]
    public partial class DockerVersion :  IEquatable<DockerVersion>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerVersion" /> class.
        /// </summary>
        /// <param name="platform">platform.</param>
        /// <param name="components">components.</param>
        /// <param name="version">version.</param>
        /// <param name="apiVersion">apiVersion.</param>
        /// <param name="minAPIVersion">minAPIVersion.</param>
        /// <param name="gitCommit">gitCommit.</param>
        /// <param name="goVersion">goVersion.</param>
        /// <param name="os">os.</param>
        /// <param name="arch">arch.</param>
        /// <param name="kernelVersion">kernelVersion.</param>
        /// <param name="experimental">experimental.</param>
        /// <param name="buildTime">buildTime.</param>
        public DockerVersion(DockerVersionPlatform platform = default(DockerVersionPlatform), List<DockerVersionComponents> components = default(List<DockerVersionComponents>), string version = default(string), string apiVersion = default(string), string minAPIVersion = default(string), string gitCommit = default(string), string goVersion = default(string), string os = default(string), string arch = default(string), string kernelVersion = default(string), bool experimental = default(bool), string buildTime = default(string))
        {
            this.Platform = platform;
            this.Components = components;
            this.Version = version;
            this.ApiVersion = apiVersion;
            this.MinAPIVersion = minAPIVersion;
            this.GitCommit = gitCommit;
            this.GoVersion = goVersion;
            this.Os = os;
            this.Arch = arch;
            this.KernelVersion = kernelVersion;
            this.Experimental = experimental;
            this.BuildTime = buildTime;
        }
        
        /// <summary>
        /// Gets or Sets Platform
        /// </summary>
        [DataMember(Name="Platform", EmitDefaultValue=false)]
        public DockerVersionPlatform Platform { get; set; }

        /// <summary>
        /// Gets or Sets Components
        /// </summary>
        [DataMember(Name="Components", EmitDefaultValue=false)]
        public List<DockerVersionComponents> Components { get; set; }

        /// <summary>
        /// Gets or Sets Version
        /// </summary>
        [DataMember(Name="Version", EmitDefaultValue=false)]
        public string Version { get; set; }

        /// <summary>
        /// Gets or Sets ApiVersion
        /// </summary>
        [DataMember(Name="ApiVersion", EmitDefaultValue=false)]
        public string ApiVersion { get; set; }

        /// <summary>
        /// Gets or Sets MinAPIVersion
        /// </summary>
        [DataMember(Name="MinAPIVersion", EmitDefaultValue=false)]
        public string MinAPIVersion { get; set; }

        /// <summary>
        /// Gets or Sets GitCommit
        /// </summary>
        [DataMember(Name="GitCommit", EmitDefaultValue=false)]
        public string GitCommit { get; set; }

        /// <summary>
        /// Gets or Sets GoVersion
        /// </summary>
        [DataMember(Name="GoVersion", EmitDefaultValue=false)]
        public string GoVersion { get; set; }

        /// <summary>
        /// Gets or Sets Os
        /// </summary>
        [DataMember(Name="Os", EmitDefaultValue=false)]
        public string Os { get; set; }

        /// <summary>
        /// Gets or Sets Arch
        /// </summary>
        [DataMember(Name="Arch", EmitDefaultValue=false)]
        public string Arch { get; set; }

        /// <summary>
        /// Gets or Sets KernelVersion
        /// </summary>
        [DataMember(Name="KernelVersion", EmitDefaultValue=false)]
        public string KernelVersion { get; set; }

        /// <summary>
        /// Gets or Sets Experimental
        /// </summary>
        [DataMember(Name="Experimental", EmitDefaultValue=false)]
        public bool Experimental { get; set; }

        /// <summary>
        /// Gets or Sets BuildTime
        /// </summary>
        [DataMember(Name="BuildTime", EmitDefaultValue=false)]
        public string BuildTime { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerVersion {\n");
            sb.Append("  Platform: ").Append(Platform).Append("\n");
            sb.Append("  Components: ").Append(Components).Append("\n");
            sb.Append("  Version: ").Append(Version).Append("\n");
            sb.Append("  ApiVersion: ").Append(ApiVersion).Append("\n");
            sb.Append("  MinAPIVersion: ").Append(MinAPIVersion).Append("\n");
            sb.Append("  GitCommit: ").Append(GitCommit).Append("\n");
            sb.Append("  GoVersion: ").Append(GoVersion).Append("\n");
            sb.Append("  Os: ").Append(Os).Append("\n");
            sb.Append("  Arch: ").Append(Arch).Append("\n");
            sb.Append("  KernelVersion: ").Append(KernelVersion).Append("\n");
            sb.Append("  Experimental: ").Append(Experimental).Append("\n");
            sb.Append("  BuildTime: ").Append(BuildTime).Append("\n");
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
            return this.Equals(input as DockerVersion);
        }

        /// <summary>
        /// Returns true if DockerVersion instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerVersion to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerVersion input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Platform == input.Platform ||
                    (this.Platform != null &&
                    this.Platform.Equals(input.Platform))
                ) && 
                (
                    this.Components == input.Components ||
                    this.Components != null &&
                    input.Components != null &&
                    this.Components.SequenceEqual(input.Components)
                ) && 
                (
                    this.Version == input.Version ||
                    (this.Version != null &&
                    this.Version.Equals(input.Version))
                ) && 
                (
                    this.ApiVersion == input.ApiVersion ||
                    (this.ApiVersion != null &&
                    this.ApiVersion.Equals(input.ApiVersion))
                ) && 
                (
                    this.MinAPIVersion == input.MinAPIVersion ||
                    (this.MinAPIVersion != null &&
                    this.MinAPIVersion.Equals(input.MinAPIVersion))
                ) && 
                (
                    this.GitCommit == input.GitCommit ||
                    (this.GitCommit != null &&
                    this.GitCommit.Equals(input.GitCommit))
                ) && 
                (
                    this.GoVersion == input.GoVersion ||
                    (this.GoVersion != null &&
                    this.GoVersion.Equals(input.GoVersion))
                ) && 
                (
                    this.Os == input.Os ||
                    (this.Os != null &&
                    this.Os.Equals(input.Os))
                ) && 
                (
                    this.Arch == input.Arch ||
                    (this.Arch != null &&
                    this.Arch.Equals(input.Arch))
                ) && 
                (
                    this.KernelVersion == input.KernelVersion ||
                    (this.KernelVersion != null &&
                    this.KernelVersion.Equals(input.KernelVersion))
                ) && 
                (
                    this.Experimental == input.Experimental ||
                    (this.Experimental != null &&
                    this.Experimental.Equals(input.Experimental))
                ) && 
                (
                    this.BuildTime == input.BuildTime ||
                    (this.BuildTime != null &&
                    this.BuildTime.Equals(input.BuildTime))
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
                if (this.Platform != null)
                    hashCode = hashCode * 59 + this.Platform.GetHashCode();
                if (this.Components != null)
                    hashCode = hashCode * 59 + this.Components.GetHashCode();
                if (this.Version != null)
                    hashCode = hashCode * 59 + this.Version.GetHashCode();
                if (this.ApiVersion != null)
                    hashCode = hashCode * 59 + this.ApiVersion.GetHashCode();
                if (this.MinAPIVersion != null)
                    hashCode = hashCode * 59 + this.MinAPIVersion.GetHashCode();
                if (this.GitCommit != null)
                    hashCode = hashCode * 59 + this.GitCommit.GetHashCode();
                if (this.GoVersion != null)
                    hashCode = hashCode * 59 + this.GoVersion.GetHashCode();
                if (this.Os != null)
                    hashCode = hashCode * 59 + this.Os.GetHashCode();
                if (this.Arch != null)
                    hashCode = hashCode * 59 + this.Arch.GetHashCode();
                if (this.KernelVersion != null)
                    hashCode = hashCode * 59 + this.KernelVersion.GetHashCode();
                if (this.Experimental != null)
                    hashCode = hashCode * 59 + this.Experimental.GetHashCode();
                if (this.BuildTime != null)
                    hashCode = hashCode * 59 + this.BuildTime.GetHashCode();
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
