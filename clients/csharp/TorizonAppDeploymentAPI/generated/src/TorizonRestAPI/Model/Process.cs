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
    /// Process
    /// </summary>
    [DataContract]
    public partial class Process :  IEquatable<Process>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Process" /> class.
        /// </summary>
        /// <param name="pid">process id.</param>
        /// <param name="ppid">parent process id.</param>
        /// <param name="user">user.</param>
        /// <param name="time">cpu time.</param>
        /// <param name="nice">nice value.</param>
        /// <param name="state">process state code.</param>
        /// <param name="args">command used to start process.</param>
        public Process(int pid = default(int), int ppid = default(int), string user = default(string), string time = default(string), int nice = default(int), string state = default(string), string args = default(string))
        {
            this.Pid = pid;
            this.Ppid = ppid;
            this.User = user;
            this.Time = time;
            this.Nice = nice;
            this.State = state;
            this.Args = args;
        }
        
        /// <summary>
        /// process id
        /// </summary>
        /// <value>process id</value>
        [DataMember(Name="pid", EmitDefaultValue=false)]
        public int Pid { get; set; }

        /// <summary>
        /// parent process id
        /// </summary>
        /// <value>parent process id</value>
        [DataMember(Name="ppid", EmitDefaultValue=false)]
        public int Ppid { get; set; }

        /// <summary>
        /// Gets or Sets User
        /// </summary>
        [DataMember(Name="user", EmitDefaultValue=false)]
        public string User { get; set; }

        /// <summary>
        /// cpu time
        /// </summary>
        /// <value>cpu time</value>
        [DataMember(Name="time", EmitDefaultValue=false)]
        public string Time { get; set; }

        /// <summary>
        /// nice value
        /// </summary>
        /// <value>nice value</value>
        [DataMember(Name="nice", EmitDefaultValue=false)]
        public int Nice { get; set; }

        /// <summary>
        /// process state code
        /// </summary>
        /// <value>process state code</value>
        [DataMember(Name="state", EmitDefaultValue=false)]
        public string State { get; set; }

        /// <summary>
        /// command used to start process
        /// </summary>
        /// <value>command used to start process</value>
        [DataMember(Name="args", EmitDefaultValue=false)]
        public string Args { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Process {\n");
            sb.Append("  Pid: ").Append(Pid).Append("\n");
            sb.Append("  Ppid: ").Append(Ppid).Append("\n");
            sb.Append("  User: ").Append(User).Append("\n");
            sb.Append("  Time: ").Append(Time).Append("\n");
            sb.Append("  Nice: ").Append(Nice).Append("\n");
            sb.Append("  State: ").Append(State).Append("\n");
            sb.Append("  Args: ").Append(Args).Append("\n");
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
            return this.Equals(input as Process);
        }

        /// <summary>
        /// Returns true if Process instances are equal
        /// </summary>
        /// <param name="input">Instance of Process to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Process input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Pid == input.Pid ||
                    (this.Pid != null &&
                    this.Pid.Equals(input.Pid))
                ) && 
                (
                    this.Ppid == input.Ppid ||
                    (this.Ppid != null &&
                    this.Ppid.Equals(input.Ppid))
                ) && 
                (
                    this.User == input.User ||
                    (this.User != null &&
                    this.User.Equals(input.User))
                ) && 
                (
                    this.Time == input.Time ||
                    (this.Time != null &&
                    this.Time.Equals(input.Time))
                ) && 
                (
                    this.Nice == input.Nice ||
                    (this.Nice != null &&
                    this.Nice.Equals(input.Nice))
                ) && 
                (
                    this.State == input.State ||
                    (this.State != null &&
                    this.State.Equals(input.State))
                ) && 
                (
                    this.Args == input.Args ||
                    (this.Args != null &&
                    this.Args.Equals(input.Args))
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
                if (this.Pid != null)
                    hashCode = hashCode * 59 + this.Pid.GetHashCode();
                if (this.Ppid != null)
                    hashCode = hashCode * 59 + this.Ppid.GetHashCode();
                if (this.User != null)
                    hashCode = hashCode * 59 + this.User.GetHashCode();
                if (this.Time != null)
                    hashCode = hashCode * 59 + this.Time.GetHashCode();
                if (this.Nice != null)
                    hashCode = hashCode * 59 + this.Nice.GetHashCode();
                if (this.State != null)
                    hashCode = hashCode * 59 + this.State.GetHashCode();
                if (this.Args != null)
                    hashCode = hashCode * 59 + this.Args.GetHashCode();
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
