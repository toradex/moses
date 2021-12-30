using System;
using System.ComponentModel;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    public class MemInfo : TorizonRestAPI.Model.MemInfo, INotifyPropertyChanged, ITorizonAPPDeploymentAPIObject
    {
        TorizonRestAPI.Api.DevicesApi api;
        DockerContainer container;
        TargetDevice device;

        public event PropertyChangedEventHandler PropertyChanged;

        public MemInfo(DockerContainer container)
        {
            this.container = container;
            this.device = container.Device;

            api = TorizonAPIManager.GetDevicesApi();
        }
        public MemInfo(TargetDevice device)
        {
            this.device = device;

            api = TorizonAPIManager.GetDevicesApi();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full, bool reboot = false)
        {
            TorizonRestAPI.Model.MemInfo mi;
            
            if (container!=null)
                mi = Utils.ObjectOrException<TorizonRestAPI.Model.MemInfo>(await api.ContainerGetmemoryAsync(container.Device.Id, container.Id));
            else
                mi = Utils.ObjectOrException<TorizonRestAPI.Model.MemInfo>(await api.DeviceGetmemoryAsync(device.Id));

            Utils.CopyProperties<TorizonRestAPI.Model.MemInfo>(mi, this, PropertyChanged);
        }
    }
}
