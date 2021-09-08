/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.3
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
    /// The state of the container.
    /// </summary>
    [DataContract]
    public partial class DockerContainerState :  IEquatable<DockerContainerState>, IValidatableObject
    {
        /// <summary>
        /// The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;. 
        /// </summary>
        /// <value>The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;. </value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum StatusEnum
        {
            /// <summary>
            /// Enum Created for value: created
            /// </summary>
            [EnumMember(Value = "created")]
            Created = 1,

            /// <summary>
            /// Enum Running for value: running
            /// </summary>
            [EnumMember(Value = "running")]
            Running = 2,

            /// <summary>
            /// Enum Paused for value: paused
            /// </summary>
            [EnumMember(Value = "paused")]
            Paused = 3,

            /// <summary>
            /// Enum Restarting for value: restarting
            /// </summary>
            [EnumMember(Value = "restarting")]
            Restarting = 4,

            /// <summary>
            /// Enum Removing for value: removing
            /// </summary>
            [EnumMember(Value = "removing")]
            Removing = 5,

            /// <summary>
            /// Enum Exited for value: exited
            /// </summary>
            [EnumMember(Value = "exited")]
            Exited = 6,

            /// <summary>
            /// Enum Dead for value: dead
            /// </summary>
            [EnumMember(Value = "dead")]
            Dead = 7

        }

        /// <summary>
        /// The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;. 
        /// </summary>
        /// <value>The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;. </value>
        [DataMember(Name="Status", EmitDefaultValue=false)]
        public StatusEnum? Status { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerContainerState" /> class.
        /// </summary>
        /// <param name="status">The status of the container. For example, &#x60;\&quot;running\&quot;&#x60; or &#x60;\&quot;exited\&quot;&#x60;. .</param>
        /// <param name="running">Whether this container is running.  Note that a running container can be _paused_. The &#x60;Running&#x60; and &#x60;Paused&#x60; booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both &#x60;Running&#x60; _and_ &#x60;Paused&#x60;.  Use the &#x60;Status&#x60; field instead to determine if a container&#39;s state is \&quot;running\&quot;. .</param>
        /// <param name="paused">Whether this container is paused..</param>
        /// <param name="restarting">Whether this container is restarting..</param>
        /// <param name="oOMKilled">Whether this container has been killed because it ran out of memory..</param>
        /// <param name="dead">dead.</param>
        /// <param name="pid">The process ID of this container.</param>
        /// <param name="exitCode">The last exit code of this container.</param>
        /// <param name="error">error.</param>
        /// <param name="startedAt">The time when this container was last started..</param>
        /// <param name="finishedAt">The time when this container last exited..</param>
        public DockerContainerState(StatusEnum? status = default(StatusEnum?), bool running = default(bool), bool paused = default(bool), bool restarting = default(bool), bool oOMKilled = default(bool), bool dead = default(bool), int pid = default(int), int exitCode = default(int), string error = default(string), string startedAt = default(string), string finishedAt = default(string))
        {
            this.Status = status;
            this.Running = running;
            this.Paused = paused;
            this.Restarting = restarting;
            this.OOMKilled = oOMKilled;
            this.Dead = dead;
            this.Pid = pid;
            this.ExitCode = exitCode;
            this.Error = error;
            this.StartedAt = startedAt;
            this.FinishedAt = finishedAt;
        }


        /// <summary>
        /// Whether this container is running.  Note that a running container can be _paused_. The &#x60;Running&#x60; and &#x60;Paused&#x60; booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both &#x60;Running&#x60; _and_ &#x60;Paused&#x60;.  Use the &#x60;Status&#x60; field instead to determine if a container&#39;s state is \&quot;running\&quot;. 
        /// </summary>
        /// <value>Whether this container is running.  Note that a running container can be _paused_. The &#x60;Running&#x60; and &#x60;Paused&#x60; booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both &#x60;Running&#x60; _and_ &#x60;Paused&#x60;.  Use the &#x60;Status&#x60; field instead to determine if a container&#39;s state is \&quot;running\&quot;. </value>
        [DataMember(Name="Running", EmitDefaultValue=false)]
        public bool Running { get; set; }

        /// <summary>
        /// Whether this container is paused.
        /// </summary>
        /// <value>Whether this container is paused.</value>
        [DataMember(Name="Paused", EmitDefaultValue=false)]
        public bool Paused { get; set; }

        /// <summary>
        /// Whether this container is restarting.
        /// </summary>
        /// <value>Whether this container is restarting.</value>
        [DataMember(Name="Restarting", EmitDefaultValue=false)]
        public bool Restarting { get; set; }

        /// <summary>
        /// Whether this container has been killed because it ran out of memory.
        /// </summary>
        /// <value>Whether this container has been killed because it ran out of memory.</value>
        [DataMember(Name="OOMKilled", EmitDefaultValue=false)]
        public bool OOMKilled { get; set; }

        /// <summary>
        /// Gets or Sets Dead
        /// </summary>
        [DataMember(Name="Dead", EmitDefaultValue=false)]
        public bool Dead { get; set; }

        /// <summary>
        /// The process ID of this container
        /// </summary>
        /// <value>The process ID of this container</value>
        [DataMember(Name="Pid", EmitDefaultValue=false)]
        public int Pid { get; set; }

        /// <summary>
        /// The last exit code of this container
        /// </summary>
        /// <value>The last exit code of this container</value>
        [DataMember(Name="ExitCode", EmitDefaultValue=false)]
        public int ExitCode { get; set; }

        /// <summary>
        /// Gets or Sets Error
        /// </summary>
        [DataMember(Name="Error", EmitDefaultValue=false)]
        public string Error { get; set; }

        /// <summary>
        /// The time when this container was last started.
        /// </summary>
        /// <value>The time when this container was last started.</value>
        [DataMember(Name="StartedAt", EmitDefaultValue=false)]
        public string StartedAt { get; set; }

        /// <summary>
        /// The time when this container last exited.
        /// </summary>
        /// <value>The time when this container last exited.</value>
        [DataMember(Name="FinishedAt", EmitDefaultValue=false)]
        public string FinishedAt { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerContainerState {\n");
            sb.Append("  Status: ").Append(Status).Append("\n");
            sb.Append("  Running: ").Append(Running).Append("\n");
            sb.Append("  Paused: ").Append(Paused).Append("\n");
            sb.Append("  Restarting: ").Append(Restarting).Append("\n");
            sb.Append("  OOMKilled: ").Append(OOMKilled).Append("\n");
            sb.Append("  Dead: ").Append(Dead).Append("\n");
            sb.Append("  Pid: ").Append(Pid).Append("\n");
            sb.Append("  ExitCode: ").Append(ExitCode).Append("\n");
            sb.Append("  Error: ").Append(Error).Append("\n");
            sb.Append("  StartedAt: ").Append(StartedAt).Append("\n");
            sb.Append("  FinishedAt: ").Append(FinishedAt).Append("\n");
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
            return this.Equals(input as DockerContainerState);
        }

        /// <summary>
        /// Returns true if DockerContainerState instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerContainerState to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerContainerState input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Status == input.Status ||
                    (this.Status != null &&
                    this.Status.Equals(input.Status))
                ) && 
                (
                    this.Running == input.Running ||
                    (this.Running != null &&
                    this.Running.Equals(input.Running))
                ) && 
                (
                    this.Paused == input.Paused ||
                    (this.Paused != null &&
                    this.Paused.Equals(input.Paused))
                ) && 
                (
                    this.Restarting == input.Restarting ||
                    (this.Restarting != null &&
                    this.Restarting.Equals(input.Restarting))
                ) && 
                (
                    this.OOMKilled == input.OOMKilled ||
                    (this.OOMKilled != null &&
                    this.OOMKilled.Equals(input.OOMKilled))
                ) && 
                (
                    this.Dead == input.Dead ||
                    (this.Dead != null &&
                    this.Dead.Equals(input.Dead))
                ) && 
                (
                    this.Pid == input.Pid ||
                    (this.Pid != null &&
                    this.Pid.Equals(input.Pid))
                ) && 
                (
                    this.ExitCode == input.ExitCode ||
                    (this.ExitCode != null &&
                    this.ExitCode.Equals(input.ExitCode))
                ) && 
                (
                    this.Error == input.Error ||
                    (this.Error != null &&
                    this.Error.Equals(input.Error))
                ) && 
                (
                    this.StartedAt == input.StartedAt ||
                    (this.StartedAt != null &&
                    this.StartedAt.Equals(input.StartedAt))
                ) && 
                (
                    this.FinishedAt == input.FinishedAt ||
                    (this.FinishedAt != null &&
                    this.FinishedAt.Equals(input.FinishedAt))
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
                if (this.Status != null)
                    hashCode = hashCode * 59 + this.Status.GetHashCode();
                if (this.Running != null)
                    hashCode = hashCode * 59 + this.Running.GetHashCode();
                if (this.Paused != null)
                    hashCode = hashCode * 59 + this.Paused.GetHashCode();
                if (this.Restarting != null)
                    hashCode = hashCode * 59 + this.Restarting.GetHashCode();
                if (this.OOMKilled != null)
                    hashCode = hashCode * 59 + this.OOMKilled.GetHashCode();
                if (this.Dead != null)
                    hashCode = hashCode * 59 + this.Dead.GetHashCode();
                if (this.Pid != null)
                    hashCode = hashCode * 59 + this.Pid.GetHashCode();
                if (this.ExitCode != null)
                    hashCode = hashCode * 59 + this.ExitCode.GetHashCode();
                if (this.Error != null)
                    hashCode = hashCode * 59 + this.Error.GetHashCode();
                if (this.StartedAt != null)
                    hashCode = hashCode * 59 + this.StartedAt.GetHashCode();
                if (this.FinishedAt != null)
                    hashCode = hashCode * 59 + this.FinishedAt.GetHashCode();
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
