using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    public class Process : TorizonRestAPI.Model.Process, IObjectsCollectionItem<TorizonRestAPI.Model.Process>, INotifyPropertyChanged
    {
        public Process(TorizonRestAPI.Model.Process model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Process>(model, this, PropertyChanged);
        }

        public event PropertyChangedEventHandler PropertyChanged;

        public void Update(TorizonRestAPI.Model.Process model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Process>(model, this, PropertyChanged);
        }
    }

    public class ProcessInstantiator : IObjectsCollectionInstantiator<Process, TorizonRestAPI.Model.Process>
    {
        public Process NewObjectFromModel(TorizonRestAPI.Model.Process model)
        {
            return new Process(model);
        }
    }

    public class Processes : ObjectsCollection<Process,TorizonRestAPI.Model.Process>, ITorizonAPPDeploymentAPIObject
    {
        TorizonRestAPI.Api.DevicesApi api;
        TargetDevice device;
        DockerContainer container;

        public Processes(DockerContainer container) : base("Pid",new ProcessInstantiator())
        {
            this.container = container;
            this.device = container.Device;

            api = TorizonAPIManager.GetDevicesApi();
        }

        public Processes(TargetDevice device) : base("Pid", new ProcessInstantiator())
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
            List<TorizonRestAPI.Model.Process> processesList = null;

            if (container!=null)
            {
                processesList = Utils.ObjectOrException<List<TorizonRestAPI.Model.Process>>(await api.ContainerGetprocessesAsync(device.Id,container.Id));
            }
            else
            {
                processesList = Utils.ObjectOrException < List<TorizonRestAPI.Model.Process> >(await api.DeviceGetprocessesAsync(device.Id));
            }

            Update(processesList);
            OnRefreshCompleted?.Invoke();
        }
    }
}
