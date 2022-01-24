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
    /// DockerImage
    /// </summary>
    [DataContract]
    public partial class DockerImage :  IEquatable<DockerImage>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerImage" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected DockerImage() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="DockerImage" /> class.
        /// </summary>
        /// <param name="id">id (required).</param>
        /// <param name="repoTags">repoTags.</param>
        /// <param name="repoDigests">repoDigests.</param>
        /// <param name="parent">parent (required).</param>
        /// <param name="comment">comment (required).</param>
        /// <param name="created">created (required).</param>
        /// <param name="container">container (required).</param>
        /// <param name="containerConfig">containerConfig.</param>
        /// <param name="dockerVersion">dockerVersion (required).</param>
        /// <param name="author">author (required).</param>
        /// <param name="config">config.</param>
        /// <param name="architecture">architecture (required).</param>
        /// <param name="os">os (required).</param>
        /// <param name="osVersion">osVersion.</param>
        /// <param name="size">size (required).</param>
        /// <param name="virtualSize">virtualSize (required).</param>
        /// <param name="graphDriver">graphDriver (required).</param>
        /// <param name="rootFS">rootFS (required).</param>
        /// <param name="metadata">metadata.</param>
        public DockerImage(string id = default(string), List<string> repoTags = default(List<string>), List<string> repoDigests = default(List<string>), string parent = default(string), string comment = default(string), string created = default(string), string container = default(string), DockerContainerConfig containerConfig = default(DockerContainerConfig), string dockerVersion = default(string), string author = default(string), DockerContainerConfig config = default(DockerContainerConfig), string architecture = default(string), string os = default(string), string osVersion = default(string), long size = default(long), long virtualSize = default(long), DockerGraphDriverData graphDriver = default(DockerGraphDriverData), DockerImageRootFS rootFS = default(DockerImageRootFS), DockerImageMetadata metadata = default(DockerImageMetadata))
        {
            // to ensure "id" is required (not null)
            if (id == null)
            {
                throw new InvalidDataException("id is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Id = id;
            }

            // to ensure "parent" is required (not null)
            if (parent == null)
            {
                throw new InvalidDataException("parent is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Parent = parent;
            }

            // to ensure "comment" is required (not null)
            if (comment == null)
            {
                throw new InvalidDataException("comment is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Comment = comment;
            }

            // to ensure "created" is required (not null)
            if (created == null)
            {
                throw new InvalidDataException("created is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Created = created;
            }

            // to ensure "container" is required (not null)
            if (container == null)
            {
                throw new InvalidDataException("container is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Container = container;
            }

            // to ensure "dockerVersion" is required (not null)
            if (dockerVersion == null)
            {
                throw new InvalidDataException("dockerVersion is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.DockerVersion = dockerVersion;
            }

            // to ensure "author" is required (not null)
            if (author == null)
            {
                throw new InvalidDataException("author is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Author = author;
            }

            // to ensure "architecture" is required (not null)
            if (architecture == null)
            {
                throw new InvalidDataException("architecture is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Architecture = architecture;
            }

            // to ensure "os" is required (not null)
            if (os == null)
            {
                throw new InvalidDataException("os is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Os = os;
            }

            // to ensure "size" is required (not null)
            if (size == null)
            {
                throw new InvalidDataException("size is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.Size = size;
            }

            // to ensure "virtualSize" is required (not null)
            if (virtualSize == null)
            {
                throw new InvalidDataException("virtualSize is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.VirtualSize = virtualSize;
            }

            // to ensure "graphDriver" is required (not null)
            if (graphDriver == null)
            {
                throw new InvalidDataException("graphDriver is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.GraphDriver = graphDriver;
            }

            // to ensure "rootFS" is required (not null)
            if (rootFS == null)
            {
                throw new InvalidDataException("rootFS is a required property for DockerImage and cannot be null");
            }
            else
            {
                this.RootFS = rootFS;
            }

            this.RepoTags = repoTags;
            this.RepoDigests = repoDigests;
            this.ContainerConfig = containerConfig;
            this.Config = config;
            this.OsVersion = osVersion;
            this.Metadata = metadata;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="Id", EmitDefaultValue=true)]
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets RepoTags
        /// </summary>
        [DataMember(Name="RepoTags", EmitDefaultValue=false)]
        public List<string> RepoTags { get; set; }

        /// <summary>
        /// Gets or Sets RepoDigests
        /// </summary>
        [DataMember(Name="RepoDigests", EmitDefaultValue=false)]
        public List<string> RepoDigests { get; set; }

        /// <summary>
        /// Gets or Sets Parent
        /// </summary>
        [DataMember(Name="Parent", EmitDefaultValue=true)]
        public string Parent { get; set; }

        /// <summary>
        /// Gets or Sets Comment
        /// </summary>
        [DataMember(Name="Comment", EmitDefaultValue=true)]
        public string Comment { get; set; }

        /// <summary>
        /// Gets or Sets Created
        /// </summary>
        [DataMember(Name="Created", EmitDefaultValue=true)]
        public string Created { get; set; }

        /// <summary>
        /// Gets or Sets Container
        /// </summary>
        [DataMember(Name="Container", EmitDefaultValue=true)]
        public string Container { get; set; }

        /// <summary>
        /// Gets or Sets ContainerConfig
        /// </summary>
        [DataMember(Name="ContainerConfig", EmitDefaultValue=false)]
        public DockerContainerConfig ContainerConfig { get; set; }

        /// <summary>
        /// Gets or Sets DockerVersion
        /// </summary>
        [DataMember(Name="DockerVersion", EmitDefaultValue=true)]
        public string DockerVersion { get; set; }

        /// <summary>
        /// Gets or Sets Author
        /// </summary>
        [DataMember(Name="Author", EmitDefaultValue=true)]
        public string Author { get; set; }

        /// <summary>
        /// Gets or Sets Config
        /// </summary>
        [DataMember(Name="Config", EmitDefaultValue=false)]
        public DockerContainerConfig Config { get; set; }

        /// <summary>
        /// Gets or Sets Architecture
        /// </summary>
        [DataMember(Name="Architecture", EmitDefaultValue=true)]
        public string Architecture { get; set; }

        /// <summary>
        /// Gets or Sets Os
        /// </summary>
        [DataMember(Name="Os", EmitDefaultValue=true)]
        public string Os { get; set; }

        /// <summary>
        /// Gets or Sets OsVersion
        /// </summary>
        [DataMember(Name="OsVersion", EmitDefaultValue=false)]
        public string OsVersion { get; set; }

        /// <summary>
        /// Gets or Sets Size
        /// </summary>
        [DataMember(Name="Size", EmitDefaultValue=true)]
        public long Size { get; set; }

        /// <summary>
        /// Gets or Sets VirtualSize
        /// </summary>
        [DataMember(Name="VirtualSize", EmitDefaultValue=true)]
        public long VirtualSize { get; set; }

        /// <summary>
        /// Gets or Sets GraphDriver
        /// </summary>
        [DataMember(Name="GraphDriver", EmitDefaultValue=true)]
        public DockerGraphDriverData GraphDriver { get; set; }

        /// <summary>
        /// Gets or Sets RootFS
        /// </summary>
        [DataMember(Name="RootFS", EmitDefaultValue=true)]
        public DockerImageRootFS RootFS { get; set; }

        /// <summary>
        /// Gets or Sets Metadata
        /// </summary>
        [DataMember(Name="Metadata", EmitDefaultValue=false)]
        public DockerImageMetadata Metadata { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DockerImage {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  RepoTags: ").Append(RepoTags).Append("\n");
            sb.Append("  RepoDigests: ").Append(RepoDigests).Append("\n");
            sb.Append("  Parent: ").Append(Parent).Append("\n");
            sb.Append("  Comment: ").Append(Comment).Append("\n");
            sb.Append("  Created: ").Append(Created).Append("\n");
            sb.Append("  Container: ").Append(Container).Append("\n");
            sb.Append("  ContainerConfig: ").Append(ContainerConfig).Append("\n");
            sb.Append("  DockerVersion: ").Append(DockerVersion).Append("\n");
            sb.Append("  Author: ").Append(Author).Append("\n");
            sb.Append("  Config: ").Append(Config).Append("\n");
            sb.Append("  Architecture: ").Append(Architecture).Append("\n");
            sb.Append("  Os: ").Append(Os).Append("\n");
            sb.Append("  OsVersion: ").Append(OsVersion).Append("\n");
            sb.Append("  Size: ").Append(Size).Append("\n");
            sb.Append("  VirtualSize: ").Append(VirtualSize).Append("\n");
            sb.Append("  GraphDriver: ").Append(GraphDriver).Append("\n");
            sb.Append("  RootFS: ").Append(RootFS).Append("\n");
            sb.Append("  Metadata: ").Append(Metadata).Append("\n");
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
            return this.Equals(input as DockerImage);
        }

        /// <summary>
        /// Returns true if DockerImage instances are equal
        /// </summary>
        /// <param name="input">Instance of DockerImage to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DockerImage input)
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
                    this.RepoTags == input.RepoTags ||
                    this.RepoTags != null &&
                    input.RepoTags != null &&
                    this.RepoTags.SequenceEqual(input.RepoTags)
                ) && 
                (
                    this.RepoDigests == input.RepoDigests ||
                    this.RepoDigests != null &&
                    input.RepoDigests != null &&
                    this.RepoDigests.SequenceEqual(input.RepoDigests)
                ) && 
                (
                    this.Parent == input.Parent ||
                    (this.Parent != null &&
                    this.Parent.Equals(input.Parent))
                ) && 
                (
                    this.Comment == input.Comment ||
                    (this.Comment != null &&
                    this.Comment.Equals(input.Comment))
                ) && 
                (
                    this.Created == input.Created ||
                    (this.Created != null &&
                    this.Created.Equals(input.Created))
                ) && 
                (
                    this.Container == input.Container ||
                    (this.Container != null &&
                    this.Container.Equals(input.Container))
                ) && 
                (
                    this.ContainerConfig == input.ContainerConfig ||
                    (this.ContainerConfig != null &&
                    this.ContainerConfig.Equals(input.ContainerConfig))
                ) && 
                (
                    this.DockerVersion == input.DockerVersion ||
                    (this.DockerVersion != null &&
                    this.DockerVersion.Equals(input.DockerVersion))
                ) && 
                (
                    this.Author == input.Author ||
                    (this.Author != null &&
                    this.Author.Equals(input.Author))
                ) && 
                (
                    this.Config == input.Config ||
                    (this.Config != null &&
                    this.Config.Equals(input.Config))
                ) && 
                (
                    this.Architecture == input.Architecture ||
                    (this.Architecture != null &&
                    this.Architecture.Equals(input.Architecture))
                ) && 
                (
                    this.Os == input.Os ||
                    (this.Os != null &&
                    this.Os.Equals(input.Os))
                ) && 
                (
                    this.OsVersion == input.OsVersion ||
                    (this.OsVersion != null &&
                    this.OsVersion.Equals(input.OsVersion))
                ) && 
                (
                    this.Size == input.Size ||
                    (this.Size != null &&
                    this.Size.Equals(input.Size))
                ) && 
                (
                    this.VirtualSize == input.VirtualSize ||
                    (this.VirtualSize != null &&
                    this.VirtualSize.Equals(input.VirtualSize))
                ) && 
                (
                    this.GraphDriver == input.GraphDriver ||
                    (this.GraphDriver != null &&
                    this.GraphDriver.Equals(input.GraphDriver))
                ) && 
                (
                    this.RootFS == input.RootFS ||
                    (this.RootFS != null &&
                    this.RootFS.Equals(input.RootFS))
                ) && 
                (
                    this.Metadata == input.Metadata ||
                    (this.Metadata != null &&
                    this.Metadata.Equals(input.Metadata))
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
                if (this.RepoTags != null)
                    hashCode = hashCode * 59 + this.RepoTags.GetHashCode();
                if (this.RepoDigests != null)
                    hashCode = hashCode * 59 + this.RepoDigests.GetHashCode();
                if (this.Parent != null)
                    hashCode = hashCode * 59 + this.Parent.GetHashCode();
                if (this.Comment != null)
                    hashCode = hashCode * 59 + this.Comment.GetHashCode();
                if (this.Created != null)
                    hashCode = hashCode * 59 + this.Created.GetHashCode();
                if (this.Container != null)
                    hashCode = hashCode * 59 + this.Container.GetHashCode();
                if (this.ContainerConfig != null)
                    hashCode = hashCode * 59 + this.ContainerConfig.GetHashCode();
                if (this.DockerVersion != null)
                    hashCode = hashCode * 59 + this.DockerVersion.GetHashCode();
                if (this.Author != null)
                    hashCode = hashCode * 59 + this.Author.GetHashCode();
                if (this.Config != null)
                    hashCode = hashCode * 59 + this.Config.GetHashCode();
                if (this.Architecture != null)
                    hashCode = hashCode * 59 + this.Architecture.GetHashCode();
                if (this.Os != null)
                    hashCode = hashCode * 59 + this.Os.GetHashCode();
                if (this.OsVersion != null)
                    hashCode = hashCode * 59 + this.OsVersion.GetHashCode();
                if (this.Size != null)
                    hashCode = hashCode * 59 + this.Size.GetHashCode();
                if (this.VirtualSize != null)
                    hashCode = hashCode * 59 + this.VirtualSize.GetHashCode();
                if (this.GraphDriver != null)
                    hashCode = hashCode * 59 + this.GraphDriver.GetHashCode();
                if (this.RootFS != null)
                    hashCode = hashCode * 59 + this.RootFS.GetHashCode();
                if (this.Metadata != null)
                    hashCode = hashCode * 59 + this.Metadata.GetHashCode();
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
