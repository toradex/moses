using System;
using System.Threading.Tasks;
using System.ComponentModel;
using System.Net;

namespace TorizonAppDeploymentAPI
{
    public class ApplicationSDKContainerAddress
    {
        public IPAddress IP { get; private set; }
        public UInt16 Port { get; private set; }
        public ApplicationSDKContainerAddress(string ip,string port)
        {
            if (ip == "0.0.0.0")
                IP = IPAddress.Loopback;
            else
                IP = IPAddress.Parse(ip);

            Port = UInt16.Parse(port);
        }
    }
    public class Application : TorizonRestAPI.Model.Application, IObjectsCollectionItem<TorizonRestAPI.Model.Application>, INotifyPropertyChanged, ITorizonAPPDeploymentAPIObject, IReadOnlyPropertiesList
    {
        TorizonRestAPI.Api.ApplicationsApi api;

        public string[] ReadOnlyProperties { get { return new string[] { "Id","Platformid","Folder"}; } }

        public event PropertyChangedEventHandler PropertyChanged;

        public static async Task<Application> CreateAsync(string platformid, string path, string username)
        {
            TorizonRestAPI.Api.ApplicationsApi api = TorizonAPIManager.GetApplicationsApi();

            TorizonRestAPI.Model.Application model = Utils.ObjectOrException<TorizonRestAPI.Model.Application>(await api.ApplicationsCreateAsync(platformid, path, username));

            return new Application(model);
        }

        public static async Task<Application> LoadAsync(string path)
        {
            TorizonRestAPI.Api.ApplicationsApi api = TorizonAPIManager.GetApplicationsApi();

            TorizonRestAPI.Model.Application model = Utils.ObjectOrException<TorizonRestAPI.Model.Application>(await api.ApplicationsLoadAsync(path));

            return new Application(model);
        }

        private Application(TorizonRestAPI.Model.Application model)
        {
            api = TorizonAPIManager.GetApplicationsApi();
            Utils.CopyProperties<TorizonRestAPI.Model.Application>(model, this, PropertyChanged);
        }

        public void Update(TorizonRestAPI.Model.Application model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Application>(model, this, PropertyChanged);
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            TorizonRestAPI.Model.Application model = Utils.ObjectOrException<TorizonRestAPI.Model.Application>(await api.ApplicationGetAsync(this.Id));
            Utils.CopyProperties<TorizonRestAPI.Model.Application>(model, this, PropertyChanged, true);
            OnRefreshCompleted?.Invoke();
        }

        public async Task CommitAsync(Action OnCommitCompleted)
        {
            TorizonRestAPI.Model.Application model = Utils.ObjectOrException<TorizonRestAPI.Model.Application>(await api.ApplicationModifyAsync(this.Id, this));
            Utils.CopyProperties<TorizonRestAPI.Model.Application>(model, this, PropertyChanged, true);
            OnCommitCompleted?.Invoke();
        }

        public async Task<ApplicationSDKContainerAddress> RunSDKContainerAsync(string configuration, Action StartupCompleted)
        {
            TorizonRestAPI.Model.InlineResponse200 resp= Utils.ObjectOrException<TorizonRestAPI.Model.InlineResponse200>(await api.ApplicationRunsdkAsync(this.Id,configuration));

            StartupCompleted?.Invoke();
            return new ApplicationSDKContainerAddress(resp.HostIp, resp.HostPort);
        }

        public async Task<bool> IsContainerUpToDateAsync(string configuration, Action<bool> CheckCompleted)
        {
            bool updated = Utils.ObjectOrException<bool>(await api.ApplicationUpdatedAsync(this.Id,configuration));

            CheckCompleted?.Invoke(updated);
            return updated;
        }

        public async Task BuildContainerAsync(string configuration,Action BuildCompleted)
        {            
            await api.ApplicationBuildAsync(this.Id,configuration);
            BuildCompleted?.Invoke();
        }

        public async Task DeployContainerAsync(string configuration, TargetDevice targetdevice, Action DeploymentCompleted)
        {            
            await api.ApplicationDeployAsync(this.Id,configuration, targetdevice.Id);
            DeploymentCompleted?.Invoke();
        }

        public async Task<DockerContainer> RunAsync(string configuration, TargetDevice targetdevice,Action<DockerContainer> ApplicationStarted)
        {
            TorizonRestAPI.Model.DockerContainer model=Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(await api.ApplicationRunAsync(this.Id, configuration, targetdevice.Id));

            DockerContainer container = new DockerContainer(model,targetdevice);

            ApplicationStarted?.Invoke(container);
            return container;
        }

        public async Task StopAsync(string configuration, TargetDevice targetdevice, Action ApplicationStopped)
        {
            await api.ApplicationStopAsync(this.Id, configuration, targetdevice.Id);
            ApplicationStopped?.Invoke();
        }

        public async Task<DockerContainer> GetContainerAsync(string configuration, TargetDevice targetdevice, Action<DockerContainer> ContainerUpdated)
        {
            TorizonRestAPI.Model.DockerContainer model = Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(await api.ApplicationGetcontainerAsync(this.Id,configuration,targetdevice.Id));

            DockerContainer container = new DockerContainer(model, targetdevice);

            ContainerUpdated?.Invoke(container);
            return container;
        }

        public async Task SyncFoldersAsync(string sdkfolder, string configuration, TargetDevice device, string destfolder, Action FolderSynced)
        {
            await api.ApplicationSyncfoldersAsync(this.Id, sdkfolder, configuration, device.Id, destfolder);
            FolderSynced?.Invoke();
        }

        public async Task UpdateSDKAsync(string configuration,Action UpdateCompleted)
        {
            await api.ApplicationUpdatesdkAsync(this.Id, configuration);
            UpdateCompleted?.Invoke();
        }
    }
}
