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
    /// Configuration for a container that is portable between hosts
    /// </summary>
    [DataContract]
    public partial class DockerContainerConfig :  IEquatable<DockerContainerConfig>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerContainerConfig" /> class.
        /// </summary>
        /// <param name="hostname">The hostname to use for the container, as a valid RFC 1123 hostname..</param>
        /// <param name="domainname">The domain name to use for the container..</param>
        /// <param name="user">The user that commands are run as inside the container..</param>
        /// <param name="attachStdin">Whether to attach to &#x60;stdin&#x60;. (default to false).</param>
        /// <param name="attachStdout">Whether to attach to &#x60;stdout&#x60;. (default to true).</param>
        /// <param name="attachStderr">Whether to attach to &#x60;stderr&#x60;. (default to true).</param>
        /// <param name="exposedPorts">An object mapping ports to an empty object in the form:  &#x60;{\&quot;&lt;port&gt;/&lt;tcp|udp|sctp&gt;\&quot;: {}}&#x60; .</param>
        /// <param name="tty">Attach standard streams to a TTY, including &#x60;stdin&#x60; if it is not closed. (default to false).</param>
        /// <param name="openStdin">Open &#x60;stdin&#x60; (default to false).</param>
        /// <param name="stdinOnce">Close &#x60;stdin&#x60; after one attached client disconnects (default to false).</param>
        /// <param name="env">A list of environment variables to set inside the container in the form &#x60;[\&quot;VAR&#x3D;value\&quot;, ...]&#x60;. A variable without &#x60;&#x3D;&#x60; is removed from the environment, rather than to have an empty value. .</param>
        /// <param name="cmd">Command to run specified as a string or an array of strings..</param>
        /// <param name="healthcheck">healthcheck.</param>
        /// <param name="argsEscaped">Command is already escaped (Windows only).</param>
        /// <param name="image">The name of the image to use when creating the container.</param>
        /// <param name="volumes">An object mapping mount point paths inside the container to empty objects..</param>
        /// <param name="workingDir">The working directory for commands to run in..</param>
        /// <param name="entrypoint">The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (&#x60;[\&quot;\&quot;]&#x60;) then the entry point is reset to system default (i.e., the entry point used by docker when there is no &#x60;ENTRYPOINT&#x60; instruction in the &#x60;Dockerfile&#x60;). .</param>
        /// <param name="networkDisabled">Disable networking for the container..</param>
        /// <param name="macAddress">MAC address of the container..</param>
        /// <param name="onBuild">&#x60;ONBUILD&#x60; metadata that were defined in the image&#39;s &#x60;Dockerfile&#x60;..</param>
        /// <param name="labels">User-defined key/value metadata..</param>
        /// <param name="stopSignal">Signal to stop a container as a string or unsigned integer. (default to &quot;SIGTERM&quot;).</param>
        /// <param name="stopTimeout">Timeout to stop a container in seconds..</param>
        /// <param name="shell">Shell for when &#x60;RUN&#x60;, &#x60;CMD&#x60;, and &#x60;ENTRYPOINT&#x60; uses a shell..</param>
        public DockerContainerConfig(string hostname = default(string), string domainname = default(string), string user = default(string), bool attachStdin = false, bool attachStdout = true, bool attachStderr = true, Dictionary<string, Object> exposedPorts = default(Dictionary<string, Object>), bool tty = false, bool openStdin = false, bool stdinOnce = false, List<string> env = default(List<string>), List<string> cmd = default(List<string>), DockerHealthConfig healthcheck = default(DockerHealthConfig), bool argsEscaped = default(bool), string image = default(string), Dictionary<string, Object> volumes = default(Dictionary<string, Object>), string workingDir = default(string), List<string> entrypoint = default(List<string>), bool networkDisabled = default(bool), string macAddress = default(string), List<string> onBuild = default(List<string>), Dictionary<string, string> labels = default(Dictionary<string, string>), string stopSignal = "SIGTERM", int stopTimeout = default(int), List<string> shell = default(List<string>))
        {
            this.Hostname = hostname;
            this.Domainname = domainname;
            this.User = user;
            // use default value if no "attachStdin" provided
            if (attachStdin == null)
            {
                this.AttachStdin = false;
            }
            else
            {
                this.AttachStdin = attachStdin;
            }
            // use default value if no "attachStdout" provided
            if (attachStdout == null)
            {
                this.AttachStdout = true;
            }
            else
            {
                this.AttachStdout = attachStdout;
            }
            // use default value if no "attachStderr" provided
            if (attachStderr == null)
            {
                this.AttachStderr = true;
            }
            else
            {
                this.AttachStderr = attachStderr;
            }
            this.ExposedPorts = exposedPorts;
            // use default value if no "tty" provided
            if (tty == null)
            {
                this.Tty = false;
            }
            else
            {
                this.Tty = tty;
            }
            // use default value if no "openStdin" provided
            if (openStdin == null)
            {
                this.OpenStdin = false;
            }
            else
            {
                this.OpenStdin = openStdin;
            }
            // use default value if no "stdinOnce" provided
            if (stdinOnce == null)
            {
                this.StdinOnce = false;
            }
            else
            {
                this.StdinOnce = stdinOnce;
            }
            this.Env = env;
            this.Cmd = cmd;
            this.Healthcheck = healthcheck;
            this.ArgsEscaped = argsEscaped;
            this.Image = image;
            this.Volumes = volumes;
            this.WorkingDir = workingDir;
            this.Entrypoint = entrypoint;
            this.NetworkDisabled = networkDisabled;
            this.MacAddress = macAddress;
            this.OnBuild = onBuild;
            this.Labels = labels;
            // use default value if no "stopSignal" provided
            if (stopSignal == null)
            {
                this.StopSignal = "SIGTERM";
            }
            else
            {
                this.StopSignal = stopSignal;
            }
            this.StopTimeout = stopTimeout;
            this.Shell = shell;
        }
        
        /// <summary>
        /// The hostname to use for the container, as a valid RFC 1123 hostname.
        /// </summary>
        /// <value>The hostname to use for the container, as a valid RFC 1123 hostname.</value>
        [DataMember(Name="Hostname", EmitDefaultValue=false)]
        public string Hostname { get; set; }

        /// <summary>
        /// The domain name to use for the container.
        /// </summary>
        /// <value>The domain name to use for the container.</value>
        [DataMember(Name="Domainname", EmitDefaultValue=false)]
        public string Domainname { get; set; }

        /// <summary>
        /// The user that commands are run as inside the container.
        /// </summary>
        /// <value>The user that commands are run as inside the container.</value>
        [DataMember(Name="User", EmitDefaultValue=false)]
        public string User { get; set; }

        /// <summary>
        /// Whether to attach to &#x60;stdin&#x60;.
        /// </summary>
        /// <value>Whether to attach to &#x60;stdin&#x60;.</value>
        [DataMember(Name="AttachStdin", EmitDefaultValue=false)]
        public bool AttachStdin { get; set; }

        /// <summary>
        /// Whether to attach to &#x60;stdout&#x60;.
        /// </summary>
        /// <value>Whether to attach to &#x60;stdout&#x60;.</value>
        [DataMember(Name="AttachStdout", EmitDefaultValue=false)]
        public bool AttachStdout { get; set; }

        /// <summary>
        /// Whether to attach to &#x60;stderr&#x60;.
        /// </summary>
        /// <value>Whether to attach to &#x60;stderr&#x60;.</value>
        [DataMember(Name="AttachStderr", EmitDefaultValue=false)]
        public bool AttachStderr { get; set; }

        /// <summary>
        /// An object mapping ports to an empty object in the form:  &#x60;{\&quot;&lt;port&gt;/&lt;tcp|udp|sctp&gt;\&quot;: {}}&#x60; 
        /// </summary>
        /// <value>An object mapping ports to an empty object in the form:  &#x60;{\&quot;&lt;port&gt;/&lt;tcp|udp|sctp&gt;\&quot;: {}}&#x60; </value>
        [DataMember(Name="ExposedPorts", EmitDefaultValue=false)]
        public Dictionary<string, Object> ExposedPorts { get; set; }

        /// <summary>
        /// Attach standard streams to a TTY, including &#x60;stdin&#x60; if it is not closed.
        /// </summary>
        /// <value>Attach standard streams to a TTY, including &#x60;stdin&#x60; if it is not closed.</value>
        [DataMember(Name="Tty", EmitDefaultValue=false)]
        public bool Tty { get; set; }

        /// <summary>
        /// Open &#x60;stdin&#x60;
        /// </summary>
        /// <value>Open &#x60;stdin&#x60;</value>
        [DataMember(Name="OpenStdin", EmitDefaultValue=false)]
        public bool OpenStdin { get; set; }

        /// <summary>
        /// Close &#x60;stdin&#x60; after one attached client disconnects
        /// </summary>
        /// <value>Close &#x60;stdin&#x60; after one attached client disconnects</value>
        [DataMember(Name="StdinOnce", EmitDefaultValue=false)]
        public bool StdinOnce { get; set; }

        /// <summary>
        /// A list of environment variables to set inside the container in the form &#x60;[\&quot;VAR&#x3D;value\&quot;, ...]&#x60;. A variable without &#x60;&#x3D;&#x60; is removed from the environment, rather than to have an empty value. 
        /// </summary>
        /// <value>A list of environment variables to set inside the container in the form &#x60;[\&quot;VAR&#x3D;value\&quot;, ...]&#x60;. A variable without &#x60;&#x3D;&#x60; is removed from the environment, rather than to have an empty value. </value>
        [DataMember(Name="Env", EmitDefaultValue=false)]
        public List<string> Env { get; set; }

        /// <summary>
        /// Command to run specified as a string or an array of strings.
        /// </summary>
        /// <value>Command to run specified as a string or an array of strings.</value>
        [DataMember(Name="Cmd", EmitDefaultValue=false)]
        public List<string> Cmd { get; set; }

        /// <summary>
        /// Gets or Sets Healthcheck
        /// </summary>
        [DataMember(Name="Healthcheck", EmitDefaultValue=false)]
        public DockerHealthConfig Healthcheck { get; set; }

        /// <summary>
        /// Command is already escaped (Windows only)
        /// </summary>
        /// <value>Command is already escaped (Windows only)</value>
        [DataMember(Name="ArgsEscaped", EmitDefaultValue=false)]
        public bool ArgsEscaped { get; set; }

        /// <summary>
        /// The name of the image to use when creating the container
        /// </summary>
        /// <value>The name of the image to use when creating the container</value>
        [DataMember(Name="Image", EmitDefaultValue=false)]
        public string Image { get; set; }

        /// <summary>
        /// An object mapping mount point paths inside the container to empty objects.
        /// </summary>
        /// <value>An object mapping mount point paths inside the container to empty objects.</value>
        [DataMember(Name="Volumes", EmitDefaultValue=false)]
        public Dictionary<string, Object> Volumes { get; set; }

        /// <summary>
        /// The working directory for commands to run in.
        /// </summary>
        /// <value>The working directory for commands to run in.</value>
        [DataMember(Name="WorkingDir", EmitDefaultValue=false)]
        public string WorkingDir { get; set; }

        /// <summary>
        /// The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (&#x60;[\&quot;\&quot;]&#x60;) then the entry point is reset to system default (i.e., the entry point used by docker when there is no &#x60;ENTRYPOINT&#x60; instruction in the &#x60;Dockerfile&#x60;). 
        /// </summary>
        /// <value>The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (&#x60;[\&quot;\&quot;]&#x60;) then the entry point is reset to system default (i.e., the entry point used by docker when there is no &#x60;ENTRYPOINT&#x60; instruction in the &#x60;Dockerfile&#x60;). </value>
        [DataMember(Name="Entrypoint", EmitDefaultValue=false)]
        public List<string> Entrypoint { get; set; }

        /// <summary>
        /// Disable networking for the container.
        /// </summary>
        /// <value>Disable networking for the container.</value>
        [DataMember(Name="NetworkDisabled", EmitDefaultValue=false)]
        public bool NetworkDisabled { get; set; }

        /// <summary>
        /// MAC address of the container.
        /// </summary>
        /// <value>MAC address of the container.</value>
        [DataMember(Name="MacAddress", EmitDefaultValue=false)]
        public string MacAddress { get; set; }

        /// <summary>
        /// &#x60;ONBUILD&#x60; metadata that were defined in the image&#39;s &#x60;Dockerfile&#x60;.
        /// </summary>
        /// <value>&#x60;ONBUILD&#x60; metadata that were defined in the image&#39;s &#x60;Dockerfile&#x60;.</value>
        [DataMember(Name="OnBuild", EmitDefaultValue=false)]
        public List<string> OnBuild { get; set; }

        /// <summary>
        /// User-defined key/value metadata.
        /// </summary>
        /// <value>User-defined key/value metadata.</value>
        [DataMember(Name="Labels", EmitDefaultValue=false)]
        public Dictionary<string, string> Labels { get; set; }

        /// <summary>
        /// Signal to stop a container as a string or unsigned integer.
        /// </summary>
        /// <value>Signal to stop a container as a string or unsigned integer.</value>
        [DataMember(Name="StopSignal", EmitDefaultValue=false)]
        public string StopSignal { get; set; }

        /// <summary>
        /// Timeout to stop a container in seconds.
        /// </summary>
        /// <value>Timeout to stop a container in seconds.</value>
        [DataMember(Name="StopTimeout", EmitDefaultValue=false)]
        public int StopTimeout { get; set; }

        /// <summary>
        /// Shell for when &#x60;RUN&#x60;, &#x60;CMD&#x60;, and &#x60;ENTRYPOINT&#x60; uses a shell.
        /// </summary>
        /// <value>Shell for when &#x60;RUN&#x60;, &#x60;CMD&#x60;, and &#x60;ENTRYPOINT&#x60; uses a shell.</value>
        [DataMember(Name="Shell", EmitDefaultValue=false)]
        public List<string> Shell { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerContainerConfig {\n");
            sb.Append("  Hostname: ").Append(Hostname).Append("\n");
            sb.Append("  Domainname: ").Append(Domainname).Append("\n");
            sb.Append("  User: ").Append(User).Append("\n");
            sb.Append("  AttachStdin: ").Append(AttachStdin).Append("\n");
            sb.Append("  AttachStdout: ").Append(AttachStdout).Append("\n");
            sb.Append("  AttachStderr: ").Append(AttachStderr).Append("\n");
            sb.Append("  ExposedPorts: ").Append(ExposedPorts).Append("\n");
            sb.Append("  Tty: ").Append(Tty).Append("\n");
            sb.Append("  OpenStdin: ").Append(OpenStdin).Append("\n");
            sb.Append("  StdinOnce: ").Append(StdinOnce).Append("\n");
            sb.Append("  Env: ").Append(Env).Append("\n");
            sb.Append("  Cmd: ").Append(Cmd).Append("\n");
            sb.Append("  Healthcheck: ").Append(Healthcheck).Append("\n");
            sb.Append("  ArgsEscaped: ").Append(ArgsEscaped).Append("\n");
            sb.Append("  Image: ").Append(Image).Append("\n");
            sb.Append("  Volumes: ").Append(Volumes).Append("\n");
            sb.Append("  WorkingDir: ").Append(WorkingDir).Append("\n");
            sb.Append("  Entrypoint: ").Append(Entrypoint).Append("\n");
            sb.Append("  NetworkDisabled: ").Append(NetworkDisabled).Append("\n");
            sb.Append("  MacAddress: ").Append(MacAddress).Append("\n");
            sb.Append("  OnBuild: ").Append(OnBuild).Append("\n");
            sb.Append("  Labels: ").Append(Labels).Append("\n");
            sb.Append("  StopSignal: ").Append(StopSignal).Append("\n");
            sb.Append("  StopTimeout: ").Append(StopTimeout).Append("\n");
            sb.Append("  Shell: ").Append(Shell).Append("\n");
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
            return this.Equals(input as DockerContainerConfig);
        }

        /// <summary>
        /// Returns true if DockerContainerConfig instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerContainerConfig to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerContainerConfig input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Hostname == input.Hostname ||
                    (this.Hostname != null &&
                    this.Hostname.Equals(input.Hostname))
                ) && 
                (
                    this.Domainname == input.Domainname ||
                    (this.Domainname != null &&
                    this.Domainname.Equals(input.Domainname))
                ) && 
                (
                    this.User == input.User ||
                    (this.User != null &&
                    this.User.Equals(input.User))
                ) && 
                (
                    this.AttachStdin == input.AttachStdin ||
                    (this.AttachStdin != null &&
                    this.AttachStdin.Equals(input.AttachStdin))
                ) && 
                (
                    this.AttachStdout == input.AttachStdout ||
                    (this.AttachStdout != null &&
                    this.AttachStdout.Equals(input.AttachStdout))
                ) && 
                (
                    this.AttachStderr == input.AttachStderr ||
                    (this.AttachStderr != null &&
                    this.AttachStderr.Equals(input.AttachStderr))
                ) && 
                (
                    this.ExposedPorts == input.ExposedPorts ||
                    this.ExposedPorts != null &&
                    input.ExposedPorts != null &&
                    this.ExposedPorts.SequenceEqual(input.ExposedPorts)
                ) && 
                (
                    this.Tty == input.Tty ||
                    (this.Tty != null &&
                    this.Tty.Equals(input.Tty))
                ) && 
                (
                    this.OpenStdin == input.OpenStdin ||
                    (this.OpenStdin != null &&
                    this.OpenStdin.Equals(input.OpenStdin))
                ) && 
                (
                    this.StdinOnce == input.StdinOnce ||
                    (this.StdinOnce != null &&
                    this.StdinOnce.Equals(input.StdinOnce))
                ) && 
                (
                    this.Env == input.Env ||
                    this.Env != null &&
                    input.Env != null &&
                    this.Env.SequenceEqual(input.Env)
                ) && 
                (
                    this.Cmd == input.Cmd ||
                    this.Cmd != null &&
                    input.Cmd != null &&
                    this.Cmd.SequenceEqual(input.Cmd)
                ) && 
                (
                    this.Healthcheck == input.Healthcheck ||
                    (this.Healthcheck != null &&
                    this.Healthcheck.Equals(input.Healthcheck))
                ) && 
                (
                    this.ArgsEscaped == input.ArgsEscaped ||
                    (this.ArgsEscaped != null &&
                    this.ArgsEscaped.Equals(input.ArgsEscaped))
                ) && 
                (
                    this.Image == input.Image ||
                    (this.Image != null &&
                    this.Image.Equals(input.Image))
                ) && 
                (
                    this.Volumes == input.Volumes ||
                    this.Volumes != null &&
                    input.Volumes != null &&
                    this.Volumes.SequenceEqual(input.Volumes)
                ) && 
                (
                    this.WorkingDir == input.WorkingDir ||
                    (this.WorkingDir != null &&
                    this.WorkingDir.Equals(input.WorkingDir))
                ) && 
                (
                    this.Entrypoint == input.Entrypoint ||
                    this.Entrypoint != null &&
                    input.Entrypoint != null &&
                    this.Entrypoint.SequenceEqual(input.Entrypoint)
                ) && 
                (
                    this.NetworkDisabled == input.NetworkDisabled ||
                    (this.NetworkDisabled != null &&
                    this.NetworkDisabled.Equals(input.NetworkDisabled))
                ) && 
                (
                    this.MacAddress == input.MacAddress ||
                    (this.MacAddress != null &&
                    this.MacAddress.Equals(input.MacAddress))
                ) && 
                (
                    this.OnBuild == input.OnBuild ||
                    this.OnBuild != null &&
                    input.OnBuild != null &&
                    this.OnBuild.SequenceEqual(input.OnBuild)
                ) && 
                (
                    this.Labels == input.Labels ||
                    this.Labels != null &&
                    input.Labels != null &&
                    this.Labels.SequenceEqual(input.Labels)
                ) && 
                (
                    this.StopSignal == input.StopSignal ||
                    (this.StopSignal != null &&
                    this.StopSignal.Equals(input.StopSignal))
                ) && 
                (
                    this.StopTimeout == input.StopTimeout ||
                    (this.StopTimeout != null &&
                    this.StopTimeout.Equals(input.StopTimeout))
                ) && 
                (
                    this.Shell == input.Shell ||
                    this.Shell != null &&
                    input.Shell != null &&
                    this.Shell.SequenceEqual(input.Shell)
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
                if (this.Hostname != null)
                    hashCode = hashCode * 59 + this.Hostname.GetHashCode();
                if (this.Domainname != null)
                    hashCode = hashCode * 59 + this.Domainname.GetHashCode();
                if (this.User != null)
                    hashCode = hashCode * 59 + this.User.GetHashCode();
                if (this.AttachStdin != null)
                    hashCode = hashCode * 59 + this.AttachStdin.GetHashCode();
                if (this.AttachStdout != null)
                    hashCode = hashCode * 59 + this.AttachStdout.GetHashCode();
                if (this.AttachStderr != null)
                    hashCode = hashCode * 59 + this.AttachStderr.GetHashCode();
                if (this.ExposedPorts != null)
                    hashCode = hashCode * 59 + this.ExposedPorts.GetHashCode();
                if (this.Tty != null)
                    hashCode = hashCode * 59 + this.Tty.GetHashCode();
                if (this.OpenStdin != null)
                    hashCode = hashCode * 59 + this.OpenStdin.GetHashCode();
                if (this.StdinOnce != null)
                    hashCode = hashCode * 59 + this.StdinOnce.GetHashCode();
                if (this.Env != null)
                    hashCode = hashCode * 59 + this.Env.GetHashCode();
                if (this.Cmd != null)
                    hashCode = hashCode * 59 + this.Cmd.GetHashCode();
                if (this.Healthcheck != null)
                    hashCode = hashCode * 59 + this.Healthcheck.GetHashCode();
                if (this.ArgsEscaped != null)
                    hashCode = hashCode * 59 + this.ArgsEscaped.GetHashCode();
                if (this.Image != null)
                    hashCode = hashCode * 59 + this.Image.GetHashCode();
                if (this.Volumes != null)
                    hashCode = hashCode * 59 + this.Volumes.GetHashCode();
                if (this.WorkingDir != null)
                    hashCode = hashCode * 59 + this.WorkingDir.GetHashCode();
                if (this.Entrypoint != null)
                    hashCode = hashCode * 59 + this.Entrypoint.GetHashCode();
                if (this.NetworkDisabled != null)
                    hashCode = hashCode * 59 + this.NetworkDisabled.GetHashCode();
                if (this.MacAddress != null)
                    hashCode = hashCode * 59 + this.MacAddress.GetHashCode();
                if (this.OnBuild != null)
                    hashCode = hashCode * 59 + this.OnBuild.GetHashCode();
                if (this.Labels != null)
                    hashCode = hashCode * 59 + this.Labels.GetHashCode();
                if (this.StopSignal != null)
                    hashCode = hashCode * 59 + this.StopSignal.GetHashCode();
                if (this.StopTimeout != null)
                    hashCode = hashCode * 59 + this.StopTimeout.GetHashCode();
                if (this.Shell != null)
                    hashCode = hashCode * 59 + this.Shell.GetHashCode();
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
