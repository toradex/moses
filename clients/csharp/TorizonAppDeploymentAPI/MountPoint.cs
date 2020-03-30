using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    public class MountPoint: TorizonRestAPI.Model.MountPoint, IObjectsCollectionItem<TorizonRestAPI.Model.MountPoint>, INotifyPropertyChanged
    {
        public MountPoint(TorizonRestAPI.Model.MountPoint model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.MountPoint>(model, this, PropertyChanged);
        }

        public event PropertyChangedEventHandler PropertyChanged;

        public void Update(TorizonRestAPI.Model.MountPoint model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.MountPoint>(model, this, PropertyChanged);
        }
    }

    public class MountPointInstantiator : IObjectsCollectionInstantiator<MountPoint, TorizonRestAPI.Model.MountPoint>
    {
        public MountPoint NewObjectFromModel(TorizonRestAPI.Model.MountPoint model)
        {
            return new MountPoint(model);
        }
    }

    public class MountPoints : ObjectsCollection<MountPoint, TorizonRestAPI.Model.MountPoint>, ITorizonAPPDeploymentAPIObject
    {
        TorizonRestAPI.Api.DevicesApi api;
        TargetDevice device;
        DockerContainer container;

        public MountPoints(DockerContainer container) : base("_Mountpoint", new MountPointInstantiator())
        {
            this.container = container;
            this.device = container.Device;

            api = TorizonAPIManager.GetDevicesApi();
        }

        public MountPoints(TargetDevice device) : base("_Mountpoint", new MountPointInstantiator())
        {
            this.device=device;

            api = TorizonAPIManager.GetDevicesApi();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            List<TorizonRestAPI.Model.MountPoint> mountpointsList = null;

            if (this.container!=null)
            {
                mountpointsList = Utils.ObjectOrException<List<TorizonRestAPI.Model.MountPoint>>(await api.ContainerGetmountpointsAsync(device.Id,container.Id));
            }
            else
            {
                mountpointsList = Utils.ObjectOrException<List<TorizonRestAPI.Model.MountPoint>>(await api.DeviceGetmountpointsAsync(device.Id));
            }

            Update(mountpointsList);
            OnRefreshCompleted?.Invoke();
        }
    }

}
