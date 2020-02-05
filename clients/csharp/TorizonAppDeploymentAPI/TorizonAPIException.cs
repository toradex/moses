using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    public class TorizonAPIException : Exception
    {
        /// <summary>
        /// Enum with error codes that can be returned by server
        /// Having derived class for each exception would probably
        /// be more .NETtish, but more complex to maintain
        /// </summary>
        public enum ErrorCodes
        {
            InternalServerError=500,
            ImageNotFoundError=520,
            IncompatibleDeviceError=521,
            ConnectionError=522,
            ContainerNotRunningError=523,
            SudoError=524,
            RemoteDockerError=525,
            RemoteImageNotFoundError=526,
            PlatformDoesNotRequireSDKError=527,
            PlatformDoesNotExistError=528,
            RemoteCommandError=529,
            LocalDockerError=530,
            InvalidObjectIdError=531,
            InvalidObjectStateError=532,
            SSHError=533,
            OSError=534,
            InvalidDeviceIdError=535,
            SerialError=536,
            TimeoutError=537,
            LoginFailedError=538,
            SSHTunnelError=539,
            InvalidPathError=540,
            SDKContainerNotRunningError=541
        }

    /// <summary>
    /// Error description
    /// </summary>
    public string Description { get; private set; }
        /// <summary>
        /// Error code
        /// </summary>
        public int Code { get; private set; }
        public TorizonAPIException(TorizonRestAPI.Model.ErrorInfo info) : base(info.Message)
        {
            this.Code = info.Code;
            this.Description = info.Description;
        }
    }
}
