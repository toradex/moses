using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    /// <summary>
    /// Allow access to device informations
    /// </summary>
    public class TargetDevice : TorizonRestAPI.Model.TargetDevice, IObjectsCollectionItem<TorizonRestAPI.Model.TargetDevice>, ITorizonAPPDeploymentAPIObject, INotifyPropertyChanged, IReadOnlyPropertiesList
    {
        public enum ConnectionState
        {
            Unknown,
            Connected,
            Disconnected
        };

        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        TorizonRestAPI.Api.DevicesApi api;

        /// <summary>
        /// Docker images
        /// </summary>
        DockerImages images;

        /// <summary>
        /// Docker containers
        /// </summary>
        DockerContainers containers;

        /// <summary>
        /// Processes running on the device
        /// </summary>
        Processes processes;

        /// <summary>
        /// Storage mount points
        /// </summary>
        MountPoints mountpoints;

        /// <summary>
        /// Information about memory usage
        /// </summary>
        MemInfo meminfo;

        public event PropertyChangedEventHandler PropertyChanged;

        public TargetDevice(TorizonRestAPI.Model.TargetDevice model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.TargetDevice>(model, this, PropertyChanged);

            api= TorizonAPIManager.GetDevicesApi();

            this.images = new DockerImages(this);
            this.containers = new DockerContainers(this);
            this.processes = new Processes(this);
            this.mountpoints = new MountPoints(this);
            this.meminfo = new MemInfo(this);

            State = ConnectionState.Unknown;
            ErrorMessage = "";
        }

        public DockerImages Images { get => images; }
        public DockerContainers Containers { get => containers; }
        public Processes Processes { get => processes; }
        public MountPoints MountPoints { get => mountpoints; }
        public MemInfo MemInfo { get => meminfo; }


        /// <summary>
        /// Property that reflect connection status of the device, set to false if we can't communicate to it
        /// </summary>
        public ConnectionState State { get; private set; }
        public string ErrorMessage { get; private set; }

        public string[] ReadOnlyProperties { get { return new string[] { "Id", "Model", "Hwrev", "Kernelversion", "Kernelrelease", "Torizonversion" }; } }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            try
            {
                TorizonRestAPI.Model.TargetDevice model = Utils.ObjectOrException<TorizonRestAPI.Model.TargetDevice>(await api.DeviceGetAsync(this.Id));

                Update(model);

                if (full)
                {
                    await images.RefreshAsync(null, false);
                    await containers.RefreshAsync(null, false);
                    await processes.RefreshAsync(null, false);
                    await mountpoints.RefreshAsync(null, false);
                    await meminfo.RefreshAsync(null, false);
                }

                if (State != ConnectionState.Connected)
                {
                    State = ConnectionState.Connected;
                    ErrorMessage = "";
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("State"));
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("ErrorMessage"));
                }
            }
            catch (Exception e)
            {
                if ((State != ConnectionState.Disconnected)&&(ErrorMessage!=e.Message))
                {
                    State = ConnectionState.Disconnected;
                    ErrorMessage = e.Message;
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("State"));
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("ErrorMessage"));
                }
            }
            OnRefreshCompleted?.Invoke();
        }

        public async Task CommitAsync(Action OnCommitCompleted)
        {
            TorizonRestAPI.Model.TargetDevice model = Utils.ObjectOrException<TorizonRestAPI.Model.TargetDevice>(await api.DeviceModifyAsync(this.Id,this));
            Utils.CopyProperties<TorizonRestAPI.Model.TargetDevice>(model, this, PropertyChanged, true);
            OnCommitCompleted?.Invoke();
        }

        public void Update(TorizonRestAPI.Model.TargetDevice model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.TargetDevice>(model, this, PropertyChanged);
        }

        public async Task UpdateInfo()
        {
            TorizonRestAPI.Model.TargetDevice model = Utils.ObjectOrException<TorizonRestAPI.Model.TargetDevice>(await api.DeviceUpdateAsync(this.Id));
            Utils.CopyProperties<TorizonRestAPI.Model.TargetDevice>(model, this, PropertyChanged);
        }

        public async Task Delete()
        {
            await api.DeviceDeleteAsync(this.Id);
        }
    }
    public class TargetDeviceInstantiator : IObjectsCollectionInstantiator<TargetDevice, TorizonRestAPI.Model.TargetDevice>
    {
        public TargetDevice NewObjectFromModel(TorizonRestAPI.Model.TargetDevice model)
        {
            return new TargetDevice(model);
        }
    }

    /// <summary>
    /// Class allowing access to devices and their properties
    /// </summary>
    public class TargetDevices : ObjectsCollection<TargetDevice, TorizonRestAPI.Model.TargetDevice>, ITorizonAPPDeploymentAPIObject
    {
        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        private TorizonRestAPI.Api.DevicesApi api;

        // Public constructor using default instantiator
        public TargetDevices() : this(new TargetDeviceInstantiator())
        {
        }      

        protected TargetDevices(IObjectsCollectionInstantiator<TargetDevice, TorizonRestAPI.Model.TargetDevice> instantiator) : base("Id", instantiator)
        {
            api= TorizonAPIManager.GetDevicesApi();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            List<TorizonRestAPI.Model.TargetDevice> modeldevices = Utils.ObjectOrException<List<TorizonRestAPI.Model.TargetDevice>>(await api.DevicesGetAsync());

            Update(modeldevices);

            if (full)
            {
                foreach (TargetDevice device in this.ToList())
                    await device.RefreshAsync(null, full);
            }

            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public async Task DetectSerialAsync(Action<TargetDevice> OnDeviceDetected, string port, string username, string password)
        {
            TorizonRestAPI.Model.TargetDevice model = Utils.ObjectOrException<TorizonRestAPI.Model.TargetDevice>(await api.DevicesSerialdetectAsync(port, username, password));

            TargetDevice device = this.GetObject(model.Id);

            if (device != null)
                device.Update(model);
            else
                this.AddObject(model);

            OnDeviceDetected?.Invoke(this.GetObject(model.Id));
        }

        public async Task DetectNetworkAsync(Action<TargetDevice> OnDeviceDetected, string hostname, string username, string password)
        {
            TorizonRestAPI.Model.TargetDevice model = Utils.ObjectOrException<TorizonRestAPI.Model.TargetDevice>(await api.DevicesNetworkdetectAsync(hostname, username, password));

            TargetDevice device = this.GetObject(model.Id);

            if (device != null)
                device.Update(model);
            else
                this.AddObject(model);

            OnDeviceDetected?.Invoke(GetObject(model.Id));
        }

        public async Task DeleteDeviceAsync(string id)
        {
            TargetDevice device = this.GetObject(id);

            if (device == null)
                return;

            await device.Delete();
            this.RemoveObject(id);
        }
    }

}
