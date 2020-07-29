/* 
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.6
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
    /// DockerContainer
    /// </summary>
    [DataContract]
    public partial class DockerContainer :  IEquatable<DockerContainer>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerContainer" /> class.
        /// </summary>
        /// <param name="id">The ID of the container.</param>
        /// <param name="created">The time the container was created.</param>
        /// <param name="path">The path to the command being run.</param>
        /// <param name="args">The arguments to the command being run.</param>
        /// <param name="state">state.</param>
        /// <param name="image">The container&#39;s image.</param>
        /// <param name="resolvConfPath">resolvConfPath.</param>
        /// <param name="hostnamePath">hostnamePath.</param>
        /// <param name="hostsPath">hostsPath.</param>
        /// <param name="logPath">logPath.</param>
        /// <param name="node">TODO.</param>
        /// <param name="name">name.</param>
        /// <param name="restartCount">restartCount.</param>
        /// <param name="driver">driver.</param>
        /// <param name="mountLabel">mountLabel.</param>
        /// <param name="processLabel">processLabel.</param>
        /// <param name="appArmorProfile">appArmorProfile.</param>
        /// <param name="execIDs">execIDs.</param>
        /// <param name="hostConfig">hostConfig.</param>
        /// <param name="graphDriver">graphDriver.</param>
        /// <param name="sizeRw">The size of files that have been created or changed by this container..</param>
        /// <param name="sizeRootFs">The total size of all the files in this container..</param>
        /// <param name="mounts">mounts.</param>
        /// <param name="config">config.</param>
        /// <param name="networkSettings">networkSettings.</param>
        public DockerContainer(string id = default(string), string created = default(string), string path = default(string), List<string> args = default(List<string>), DockerContainerState state = default(DockerContainerState), string image = default(string), string resolvConfPath = default(string), string hostnamePath = default(string), string hostsPath = default(string), string logPath = default(string), Object node = default(Object), string name = default(string), int restartCount = default(int), string driver = default(string), string mountLabel = default(string), string processLabel = default(string), string appArmorProfile = default(string), List<string> execIDs = default(List<string>), DockerHostConfig hostConfig = default(DockerHostConfig), DockerGraphDriverData graphDriver = default(DockerGraphDriverData), long sizeRw = default(long), long sizeRootFs = default(long), List<DockerMountPoint> mounts = default(List<DockerMountPoint>), DockerContainerConfig config = default(DockerContainerConfig), DockerNetworkSettings networkSettings = default(DockerNetworkSettings))
        {
            this.Id = id;
            this.Created = created;
            this.Path = path;
            this.Args = args;
            this.State = state;
            this.Image = image;
            this.ResolvConfPath = resolvConfPath;
            this.HostnamePath = hostnamePath;
            this.HostsPath = hostsPath;
            this.LogPath = logPath;
            this.Node = node;
            this.Name = name;
            this.RestartCount = restartCount;
            this.Driver = driver;
            this.MountLabel = mountLabel;
            this.ProcessLabel = processLabel;
            this.AppArmorProfile = appArmorProfile;
            this.ExecIDs = execIDs;
            this.HostConfig = hostConfig;
            this.GraphDriver = graphDriver;
            this.SizeRw = sizeRw;
            this.SizeRootFs = sizeRootFs;
            this.Mounts = mounts;
            this.Config = config;
            this.NetworkSettings = networkSettings;
        }
        
        /// <summary>
        /// The ID of the container
        /// </summary>
        /// <value>The ID of the container</value>
        [DataMember(Name="Id", EmitDefaultValue=false)]
        public string Id { get; set; }

        /// <summary>
        /// The time the container was created
        /// </summary>
        /// <value>The time the container was created</value>
        [DataMember(Name="Created", EmitDefaultValue=false)]
        public string Created { get; set; }

        /// <summary>
        /// The path to the command being run
        /// </summary>
        /// <value>The path to the command being run</value>
        [DataMember(Name="Path", EmitDefaultValue=false)]
        public string Path { get; set; }

        /// <summary>
        /// The arguments to the command being run
        /// </summary>
        /// <value>The arguments to the command being run</value>
        [DataMember(Name="Args", EmitDefaultValue=false)]
        public List<string> Args { get; set; }

        /// <summary>
        /// Gets or Sets State
        /// </summary>
        [DataMember(Name="State", EmitDefaultValue=false)]
        public DockerContainerState State { get; set; }

        /// <summary>
        /// The container&#39;s image
        /// </summary>
        /// <value>The container&#39;s image</value>
        [DataMember(Name="Image", EmitDefaultValue=false)]
        public string Image { get; set; }

        /// <summary>
        /// Gets or Sets ResolvConfPath
        /// </summary>
        [DataMember(Name="ResolvConfPath", EmitDefaultValue=false)]
        public string ResolvConfPath { get; set; }

        /// <summary>
        /// Gets or Sets HostnamePath
        /// </summary>
        [DataMember(Name="HostnamePath", EmitDefaultValue=false)]
        public string HostnamePath { get; set; }

        /// <summary>
        /// Gets or Sets HostsPath
        /// </summary>
        [DataMember(Name="HostsPath", EmitDefaultValue=false)]
        public string HostsPath { get; set; }

        /// <summary>
        /// Gets or Sets LogPath
        /// </summary>
        [DataMember(Name="LogPath", EmitDefaultValue=false)]
        public string LogPath { get; set; }

        /// <summary>
        /// TODO
        /// </summary>
        /// <value>TODO</value>
        [DataMember(Name="Node", EmitDefaultValue=false)]
        public Object Node { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets RestartCount
        /// </summary>
        [DataMember(Name="RestartCount", EmitDefaultValue=false)]
        public int RestartCount { get; set; }

        /// <summary>
        /// Gets or Sets Driver
        /// </summary>
        [DataMember(Name="Driver", EmitDefaultValue=false)]
        public string Driver { get; set; }

        /// <summary>
        /// Gets or Sets MountLabel
        /// </summary>
        [DataMember(Name="MountLabel", EmitDefaultValue=false)]
        public string MountLabel { get; set; }

        /// <summary>
        /// Gets or Sets ProcessLabel
        /// </summary>
        [DataMember(Name="ProcessLabel", EmitDefaultValue=false)]
        public string ProcessLabel { get; set; }

        /// <summary>
        /// Gets or Sets AppArmorProfile
        /// </summary>
        [DataMember(Name="AppArmorProfile", EmitDefaultValue=false)]
        public string AppArmorProfile { get; set; }

        /// <summary>
        /// Gets or Sets ExecIDs
        /// </summary>
        [DataMember(Name="ExecIDs", EmitDefaultValue=false)]
        public List<string> ExecIDs { get; set; }

        /// <summary>
        /// Gets or Sets HostConfig
        /// </summary>
        [DataMember(Name="HostConfig", EmitDefaultValue=false)]
        public DockerHostConfig HostConfig { get; set; }

        /// <summary>
        /// Gets or Sets GraphDriver
        /// </summary>
        [DataMember(Name="GraphDriver", EmitDefaultValue=false)]
        public DockerGraphDriverData GraphDriver { get; set; }

        /// <summary>
        /// The size of files that have been created or changed by this container.
        /// </summary>
        /// <value>The size of files that have been created or changed by this container.</value>
        [DataMember(Name="SizeRw", EmitDefaultValue=false)]
        public long SizeRw { get; set; }

        /// <summary>
        /// The total size of all the files in this container.
        /// </summary>
        /// <value>The total size of all the files in this container.</value>
        [DataMember(Name="SizeRootFs", EmitDefaultValue=false)]
        public long SizeRootFs { get; set; }

        /// <summary>
        /// Gets or Sets Mounts
        /// </summary>
        [DataMember(Name="Mounts", EmitDefaultValue=false)]
        public List<DockerMountPoint> Mounts { get; set; }

        /// <summary>
        /// Gets or Sets Config
        /// </summary>
        [DataMember(Name="Config", EmitDefaultValue=false)]
        public DockerContainerConfig Config { get; set; }

        /// <summary>
        /// Gets or Sets NetworkSettings
        /// </summary>
        [DataMember(Name="NetworkSettings", EmitDefaultValue=false)]
        public DockerNetworkSettings NetworkSettings { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerContainer {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Created: ").Append(Created).Append("\n");
            sb.Append("  Path: ").Append(Path).Append("\n");
            sb.Append("  Args: ").Append(Args).Append("\n");
            sb.Append("  State: ").Append(State).Append("\n");
            sb.Append("  Image: ").Append(Image).Append("\n");
            sb.Append("  ResolvConfPath: ").Append(ResolvConfPath).Append("\n");
            sb.Append("  HostnamePath: ").Append(HostnamePath).Append("\n");
            sb.Append("  HostsPath: ").Append(HostsPath).Append("\n");
            sb.Append("  LogPath: ").Append(LogPath).Append("\n");
            sb.Append("  Node: ").Append(Node).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  RestartCount: ").Append(RestartCount).Append("\n");
            sb.Append("  Driver: ").Append(Driver).Append("\n");
            sb.Append("  MountLabel: ").Append(MountLabel).Append("\n");
            sb.Append("  ProcessLabel: ").Append(ProcessLabel).Append("\n");
            sb.Append("  AppArmorProfile: ").Append(AppArmorProfile).Append("\n");
            sb.Append("  ExecIDs: ").Append(ExecIDs).Append("\n");
            sb.Append("  HostConfig: ").Append(HostConfig).Append("\n");
            sb.Append("  GraphDriver: ").Append(GraphDriver).Append("\n");
            sb.Append("  SizeRw: ").Append(SizeRw).Append("\n");
            sb.Append("  SizeRootFs: ").Append(SizeRootFs).Append("\n");
            sb.Append("  Mounts: ").Append(Mounts).Append("\n");
            sb.Append("  Config: ").Append(Config).Append("\n");
            sb.Append("  NetworkSettings: ").Append(NetworkSettings).Append("\n");
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
            return this.Equals(input as DockerContainer);
        }

        /// <summary>
        /// Returns true if DockerContainer instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerContainer to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerContainer input)
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
                    this.Created == input.Created ||
                    (this.Created != null &&
                    this.Created.Equals(input.Created))
                ) && 
                (
                    this.Path == input.Path ||
                    (this.Path != null &&
                    this.Path.Equals(input.Path))
                ) && 
                (
                    this.Args == input.Args ||
                    this.Args != null &&
                    input.Args != null &&
                    this.Args.SequenceEqual(input.Args)
                ) && 
                (
                    this.State == input.State ||
                    (this.State != null &&
                    this.State.Equals(input.State))
                ) && 
                (
                    this.Image == input.Image ||
                    (this.Image != null &&
                    this.Image.Equals(input.Image))
                ) && 
                (
                    this.ResolvConfPath == input.ResolvConfPath ||
                    (this.ResolvConfPath != null &&
                    this.ResolvConfPath.Equals(input.ResolvConfPath))
                ) && 
                (
                    this.HostnamePath == input.HostnamePath ||
                    (this.HostnamePath != null &&
                    this.HostnamePath.Equals(input.HostnamePath))
                ) && 
                (
                    this.HostsPath == input.HostsPath ||
                    (this.HostsPath != null &&
                    this.HostsPath.Equals(input.HostsPath))
                ) && 
                (
                    this.LogPath == input.LogPath ||
                    (this.LogPath != null &&
                    this.LogPath.Equals(input.LogPath))
                ) && 
                (
                    this.Node == input.Node ||
                    (this.Node != null &&
                    this.Node.Equals(input.Node))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.RestartCount == input.RestartCount ||
                    (this.RestartCount != null &&
                    this.RestartCount.Equals(input.RestartCount))
                ) && 
                (
                    this.Driver == input.Driver ||
                    (this.Driver != null &&
                    this.Driver.Equals(input.Driver))
                ) && 
                (
                    this.MountLabel == input.MountLabel ||
                    (this.MountLabel != null &&
                    this.MountLabel.Equals(input.MountLabel))
                ) && 
                (
                    this.ProcessLabel == input.ProcessLabel ||
                    (this.ProcessLabel != null &&
                    this.ProcessLabel.Equals(input.ProcessLabel))
                ) && 
                (
                    this.AppArmorProfile == input.AppArmorProfile ||
                    (this.AppArmorProfile != null &&
                    this.AppArmorProfile.Equals(input.AppArmorProfile))
                ) && 
                (
                    this.ExecIDs == input.ExecIDs ||
                    this.ExecIDs != null &&
                    input.ExecIDs != null &&
                    this.ExecIDs.SequenceEqual(input.ExecIDs)
                ) && 
                (
                    this.HostConfig == input.HostConfig ||
                    (this.HostConfig != null &&
                    this.HostConfig.Equals(input.HostConfig))
                ) && 
                (
                    this.GraphDriver == input.GraphDriver ||
                    (this.GraphDriver != null &&
                    this.GraphDriver.Equals(input.GraphDriver))
                ) && 
                (
                    this.SizeRw == input.SizeRw ||
                    (this.SizeRw != null &&
                    this.SizeRw.Equals(input.SizeRw))
                ) && 
                (
                    this.SizeRootFs == input.SizeRootFs ||
                    (this.SizeRootFs != null &&
                    this.SizeRootFs.Equals(input.SizeRootFs))
                ) && 
                (
                    this.Mounts == input.Mounts ||
                    this.Mounts != null &&
                    input.Mounts != null &&
                    this.Mounts.SequenceEqual(input.Mounts)
                ) && 
                (
                    this.Config == input.Config ||
                    (this.Config != null &&
                    this.Config.Equals(input.Config))
                ) && 
                (
                    this.NetworkSettings == input.NetworkSettings ||
                    (this.NetworkSettings != null &&
                    this.NetworkSettings.Equals(input.NetworkSettings))
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
                if (this.Created != null)
                    hashCode = hashCode * 59 + this.Created.GetHashCode();
                if (this.Path != null)
                    hashCode = hashCode * 59 + this.Path.GetHashCode();
                if (this.Args != null)
                    hashCode = hashCode * 59 + this.Args.GetHashCode();
                if (this.State != null)
                    hashCode = hashCode * 59 + this.State.GetHashCode();
                if (this.Image != null)
                    hashCode = hashCode * 59 + this.Image.GetHashCode();
                if (this.ResolvConfPath != null)
                    hashCode = hashCode * 59 + this.ResolvConfPath.GetHashCode();
                if (this.HostnamePath != null)
                    hashCode = hashCode * 59 + this.HostnamePath.GetHashCode();
                if (this.HostsPath != null)
                    hashCode = hashCode * 59 + this.HostsPath.GetHashCode();
                if (this.LogPath != null)
                    hashCode = hashCode * 59 + this.LogPath.GetHashCode();
                if (this.Node != null)
                    hashCode = hashCode * 59 + this.Node.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.RestartCount != null)
                    hashCode = hashCode * 59 + this.RestartCount.GetHashCode();
                if (this.Driver != null)
                    hashCode = hashCode * 59 + this.Driver.GetHashCode();
                if (this.MountLabel != null)
                    hashCode = hashCode * 59 + this.MountLabel.GetHashCode();
                if (this.ProcessLabel != null)
                    hashCode = hashCode * 59 + this.ProcessLabel.GetHashCode();
                if (this.AppArmorProfile != null)
                    hashCode = hashCode * 59 + this.AppArmorProfile.GetHashCode();
                if (this.ExecIDs != null)
                    hashCode = hashCode * 59 + this.ExecIDs.GetHashCode();
                if (this.HostConfig != null)
                    hashCode = hashCode * 59 + this.HostConfig.GetHashCode();
                if (this.GraphDriver != null)
                    hashCode = hashCode * 59 + this.GraphDriver.GetHashCode();
                if (this.SizeRw != null)
                    hashCode = hashCode * 59 + this.SizeRw.GetHashCode();
                if (this.SizeRootFs != null)
                    hashCode = hashCode * 59 + this.SizeRootFs.GetHashCode();
                if (this.Mounts != null)
                    hashCode = hashCode * 59 + this.Mounts.GetHashCode();
                if (this.Config != null)
                    hashCode = hashCode * 59 + this.Config.GetHashCode();
                if (this.NetworkSettings != null)
                    hashCode = hashCode * 59 + this.NetworkSettings.GetHashCode();
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
