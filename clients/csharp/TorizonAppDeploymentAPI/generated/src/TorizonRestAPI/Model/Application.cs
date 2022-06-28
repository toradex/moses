/*
 * Torizon IDE-backend API
 *
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.7
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
    /// Application
    /// </summary>
    [DataContract]
    public partial class Application :  IEquatable<Application>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Application" /> class.
        /// </summary>
        /// <param name="props">Custom application properties.</param>
        /// <param name="dockercomposefile">path of docker-compose file to be used to start additional containers needed by the app.</param>
        /// <param name="startupscript">path of script to be run when application debugging starts.</param>
        /// <param name="shutdownscript">path of script to be run when application debugging stops.</param>
        /// <param name="ports">ports to be exposed from the container.</param>
        /// <param name="volumes">Local folders to be mounted \&quot;A mount points inside a container.</param>
        /// <param name="devices">Additional devices to be shared inside container.</param>
        /// <param name="networks">Networks used by container (in debug it will always be also on bridge).</param>
        /// <param name="extraparms">Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML).</param>
        /// <param name="username">user account used to run the application inside the container.</param>
        /// <param name="images">SHA-ids of the debug and release images.</param>
        /// <param name="sdkimages">SHA-ids of the debug and release SDK images.</param>
        /// <param name="imagetags">unique tag used for the images.</param>
        /// <param name="sdkimagetags">unique tag used for the SDK images (if application uses an SDK).</param>
        /// <param name="otapackagename">name of the OTA package.</param>
        /// <param name="otapackageversion">version of the OTA package.</param>
        public Application(Dictionary<string, Dictionary<string, string>> props = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, string> dockercomposefile = default(Dictionary<string, string>), Dictionary<string, string> startupscript = default(Dictionary<string, string>), Dictionary<string, string> shutdownscript = default(Dictionary<string, string>), Dictionary<string, Dictionary<string, string>> ports = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, Dictionary<string, string>> volumes = default(Dictionary<string, Dictionary<string, string>>), Dictionary<string, List<string>> devices = default(Dictionary<string, List<string>>), Dictionary<string, List<string>> networks = default(Dictionary<string, List<string>>), Dictionary<string, Dictionary<string, string>> extraparms = default(Dictionary<string, Dictionary<string, string>>), string username = default(string), Dictionary<string, string> images = default(Dictionary<string, string>), Dictionary<string, string> sdkimages = default(Dictionary<string, string>), Dictionary<string, string> imagetags = default(Dictionary<string, string>), Dictionary<string, string> sdkimagetags = default(Dictionary<string, string>), string otapackagename = default(string), string otapackageversion = default(string))
        {
            this.Props = props;
            this.Dockercomposefile = dockercomposefile;
            this.Startupscript = startupscript;
            this.Shutdownscript = shutdownscript;
            this.Ports = ports;
            this.Volumes = volumes;
            this.Devices = devices;
            this.Networks = networks;
            this.Extraparms = extraparms;
            this.Username = username;
            this.Images = images;
            this.Sdkimages = sdkimages;
            this.Imagetags = imagetags;
            this.Sdkimagetags = sdkimagetags;
            this.Otapackagename = otapackagename;
            this.Otapackageversion = otapackageversion;
        }

        /// <summary>
        /// Unique id
        /// </summary>
        /// <value>Unique id</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; private set; }

        /// <summary>
        /// id of the platform used to generate this application configuration
        /// </summary>
        /// <value>id of the platform used to generate this application configuration</value>
        [DataMember(Name="platformid", EmitDefaultValue=false)]
        public string Platformid { get; private set; }

        /// <summary>
        /// folder where application configuration and extra files are stored
        /// </summary>
        /// <value>folder where application configuration and extra files are stored</value>
        [DataMember(Name="folder", EmitDefaultValue=false)]
        public string Folder { get; private set; }

        /// <summary>
        /// Custom application properties
        /// </summary>
        /// <value>Custom application properties</value>
        [DataMember(Name="props", EmitDefaultValue=false)]
        public Dictionary<string, Dictionary<string, string>> Props { get; set; }

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
        /// Local folders to be mounted \&quot;A mount points inside a container
        /// </summary>
        /// <value>Local folders to be mounted \&quot;A mount points inside a container</value>
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
        /// user account used to run the application inside the container
        /// </summary>
        /// <value>user account used to run the application inside the container</value>
        [DataMember(Name="username", EmitDefaultValue=false)]
        public string Username { get; set; }

        /// <summary>
        /// SHA-ids of the debug and release images
        /// </summary>
        /// <value>SHA-ids of the debug and release images</value>
        [DataMember(Name="images", EmitDefaultValue=false)]
        public Dictionary<string, string> Images { get; set; }

        /// <summary>
        /// SHA-ids of the debug and release SDK images
        /// </summary>
        /// <value>SHA-ids of the debug and release SDK images</value>
        [DataMember(Name="sdkimages", EmitDefaultValue=false)]
        public Dictionary<string, string> Sdkimages { get; set; }

        /// <summary>
        /// unique tag used for the images
        /// </summary>
        /// <value>unique tag used for the images</value>
        [DataMember(Name="imagetags", EmitDefaultValue=false)]
        public Dictionary<string, string> Imagetags { get; set; }

        /// <summary>
        /// unique tag used for the SDK images (if application uses an SDK)
        /// </summary>
        /// <value>unique tag used for the SDK images (if application uses an SDK)</value>
        [DataMember(Name="sdkimagetags", EmitDefaultValue=false)]
        public Dictionary<string, string> Sdkimagetags { get; set; }

        /// <summary>
        /// name of the OTA package
        /// </summary>
        /// <value>name of the OTA package</value>
        [DataMember(Name="otapackagename", EmitDefaultValue=false)]
        public string Otapackagename { get; set; }

        /// <summary>
        /// version of the OTA package
        /// </summary>
        /// <value>version of the OTA package</value>
        [DataMember(Name="otapackageversion", EmitDefaultValue=false)]
        public string Otapackageversion { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Application {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Platformid: ").Append(Platformid).Append("\n");
            sb.Append("  Folder: ").Append(Folder).Append("\n");
            sb.Append("  Props: ").Append(Props).Append("\n");
            sb.Append("  Dockercomposefile: ").Append(Dockercomposefile).Append("\n");
            sb.Append("  Startupscript: ").Append(Startupscript).Append("\n");
            sb.Append("  Shutdownscript: ").Append(Shutdownscript).Append("\n");
            sb.Append("  Ports: ").Append(Ports).Append("\n");
            sb.Append("  Volumes: ").Append(Volumes).Append("\n");
            sb.Append("  Devices: ").Append(Devices).Append("\n");
            sb.Append("  Networks: ").Append(Networks).Append("\n");
            sb.Append("  Extraparms: ").Append(Extraparms).Append("\n");
            sb.Append("  Username: ").Append(Username).Append("\n");
            sb.Append("  Images: ").Append(Images).Append("\n");
            sb.Append("  Sdkimages: ").Append(Sdkimages).Append("\n");
            sb.Append("  Imagetags: ").Append(Imagetags).Append("\n");
            sb.Append("  Sdkimagetags: ").Append(Sdkimagetags).Append("\n");
            sb.Append("  Otapackagename: ").Append(Otapackagename).Append("\n");
            sb.Append("  Otapackageversion: ").Append(Otapackageversion).Append("\n");
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
            return this.Equals(input as Application);
        }

        /// <summary>
        /// Returns true if Application instances are equal
        /// </summary>
        /// <param name="input">Instance of Application to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Application input)
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
                    this.Platformid == input.Platformid ||
                    (this.Platformid != null &&
                    this.Platformid.Equals(input.Platformid))
                ) && 
                (
                    this.Folder == input.Folder ||
                    (this.Folder != null &&
                    this.Folder.Equals(input.Folder))
                ) && 
                (
                    this.Props == input.Props ||
                    this.Props != null &&
                    input.Props != null &&
                    this.Props.SequenceEqual(input.Props)
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
                    this.Username == input.Username ||
                    (this.Username != null &&
                    this.Username.Equals(input.Username))
                ) && 
                (
                    this.Images == input.Images ||
                    this.Images != null &&
                    input.Images != null &&
                    this.Images.SequenceEqual(input.Images)
                ) && 
                (
                    this.Sdkimages == input.Sdkimages ||
                    this.Sdkimages != null &&
                    input.Sdkimages != null &&
                    this.Sdkimages.SequenceEqual(input.Sdkimages)
                ) && 
                (
                    this.Imagetags == input.Imagetags ||
                    this.Imagetags != null &&
                    input.Imagetags != null &&
                    this.Imagetags.SequenceEqual(input.Imagetags)
                ) && 
                (
                    this.Sdkimagetags == input.Sdkimagetags ||
                    this.Sdkimagetags != null &&
                    input.Sdkimagetags != null &&
                    this.Sdkimagetags.SequenceEqual(input.Sdkimagetags)
                ) && 
                (
                    this.Otapackagename == input.Otapackagename ||
                    (this.Otapackagename != null &&
                    this.Otapackagename.Equals(input.Otapackagename))
                ) && 
                (
                    this.Otapackageversion == input.Otapackageversion ||
                    (this.Otapackageversion != null &&
                    this.Otapackageversion.Equals(input.Otapackageversion))
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
                if (this.Platformid != null)
                    hashCode = hashCode * 59 + this.Platformid.GetHashCode();
                if (this.Folder != null)
                    hashCode = hashCode * 59 + this.Folder.GetHashCode();
                if (this.Props != null)
                    hashCode = hashCode * 59 + this.Props.GetHashCode();
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
                if (this.Username != null)
                    hashCode = hashCode * 59 + this.Username.GetHashCode();
                if (this.Images != null)
                    hashCode = hashCode * 59 + this.Images.GetHashCode();
                if (this.Sdkimages != null)
                    hashCode = hashCode * 59 + this.Sdkimages.GetHashCode();
                if (this.Imagetags != null)
                    hashCode = hashCode * 59 + this.Imagetags.GetHashCode();
                if (this.Sdkimagetags != null)
                    hashCode = hashCode * 59 + this.Sdkimagetags.GetHashCode();
                if (this.Otapackagename != null)
                    hashCode = hashCode * 59 + this.Otapackagename.GetHashCode();
                if (this.Otapackageversion != null)
                    hashCode = hashCode * 59 + this.Otapackageversion.GetHashCode();
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
