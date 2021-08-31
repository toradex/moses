using System;
using System.Threading.Tasks;
using System.ComponentModel;
using System.Net;
using TorizonRestAPI.Api;
using TorizonRestAPI.Model;

namespace TorizonAppDeploymentAPI
{
    public class ApplicationSDKContainerAddress
    {
        public IPAddress IP { get; private set; }
        public UInt16 Port { get; private set; }
        public ApplicationSDKContainerAddress(string ip, string port)
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

        public string[] ReadOnlyProperties { get { return new string[] { "Id", "Platformid", "Folder" }; } }

        public event PropertyChangedEventHandler PropertyChanged;

        public static Action CreateProgressTask(ref Progress progressRef, Action<string, int> taskUpdateStatus)
        {
            ProgressApi progressApi = TorizonAPIManager.GetProgressApi();
            Progress progress = progressApi.ProgressCreate();
            progressRef = progress;

            return () => {
                while (progress.Pending)
                {
                    progress = progressApi.ProgressStatus(progress.Id);

                    foreach (string msg in progress.Messages)
                    {
                        taskUpdateStatus?.Invoke(msg, progress._Progress);
                    }
                }

                // send 100% for the current task
                taskUpdateStatus?.Invoke("Done", -100);
            };
        }

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

        public async Task<ApplicationSDKContainerAddress> RunSDKContainerAsync(string configuration, bool build, Action StartupCompleted)
        {
            TorizonRestAPI.Model.InlineResponse200 resp = Utils.ObjectOrException<TorizonRestAPI.Model.InlineResponse200>(await api.ApplicationRunsdkAsync(this.Id, configuration, build));

            StartupCompleted?.Invoke();
            return new ApplicationSDKContainerAddress(resp.HostIp, resp.HostPort);
        }

        public DockerContainer GetSDKContainer(string configuration)
        {
            TorizonRestAPI.Model.DockerContainer model =
                Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(
                    api.ApplicationSdkContainer(this.Id, configuration)
                );

            DockerContainer container = new DockerContainer(model, null);
            return container;
        }

        public async Task<bool> IsContainerUpToDateAsync(string configuration, Action<bool> CheckCompleted)
        {
            bool updated = Utils.ObjectOrException<bool>(await api.ApplicationUpdatedAsync(this.Id, configuration));

            CheckCompleted?.Invoke(updated);
            return updated;
        }

        public async Task BuildContainerAsync(string configuration, Action<string, int> buildCompleted)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, buildCompleted);

            var task =  api.ApplicationBuildAsync(this.Id, configuration, progress?.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }

        public async Task DeployContainerAsync(string configuration, TargetDevice targetdevice, Action<string, int> DeploymentCompleted)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, DeploymentCompleted);

            var task =  api.ApplicationDeployAsync(this.Id, configuration, targetdevice.Id, progress.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }

        public async Task<DockerContainer> RunAsync(string configuration, TargetDevice targetdevice, Action<string, int> runningAction, Action<DockerContainer> ApplicationStarted)
        {
            Progress progress = null;
            DockerContainer container = null;

            var taskBuild = CreateProgressTask(ref progress, runningAction);

            _ =  api.ApplicationRunAsync(this.Id, configuration, targetdevice.Id, progress?.Id).ContinueWith( task => {
                TorizonRestAPI.Model.DockerContainer model =
                    Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(task.Result);

                container = new DockerContainer(model, targetdevice);
                ApplicationStarted?.Invoke(container);
            });

            await Task.Run(taskBuild);
            return container;
        }

        public async Task StopAsync(string configuration, TargetDevice targetdevice, Action ApplicationStopped)
        {
            await api.ApplicationStopAsync(this.Id, configuration, targetdevice.Id);
            ApplicationStopped?.Invoke();
        }

        public async Task<DockerContainer> GetContainerAsync(string configuration, TargetDevice targetdevice, Action<DockerContainer> ContainerUpdated)
        {
            TorizonRestAPI.Model.DockerContainer model = Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(await api.ApplicationGetcontainerAsync(this.Id, configuration, targetdevice.Id));

            DockerContainer container = new DockerContainer(model, targetdevice);

            ContainerUpdated?.Invoke(container);
            return container;
        }

        public async Task SyncFoldersAsync(string sdkfolder, string configuration, TargetDevice device, string destfolder, Action<string, int> FolderSynced)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, FolderSynced);

            var task =  api.ApplicationSyncfoldersAsync(this.Id, sdkfolder, configuration, device.Id, destfolder, true, progress?.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }

        public async Task UpdateSDKAsync(string configuration, Action<string, int> UpdateCompleted)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, UpdateCompleted);

            var task =  api.ApplicationUpdatesdkAsync(this.Id, configuration, progress?.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }

        public async Task<string> GetDockerCommandLineAsync(string configuration)
        {
            string cmdline=Utils.ObjectOrException<string>(await api.ApplicationGetdockerCommandlineAsync(this.Id, configuration));

            cmdline = cmdline.Trim(new char[] { '\n' });
            cmdline = cmdline.Trim(new char[] { '\"' });

            return cmdline;
        }

        public async Task<string> GetDockerComposeFileAsync(string configuration)
        {
            string composefile =  Utils.ObjectOrException<string>(await api.ApplicationGetdockerComposefileAsync(this.Id, configuration));

            composefile = composefile.Trim(new char[] { '\n' });
            composefile = composefile.Trim(new char[] { '\"' });

            return composefile;
        }

        public async Task PushToDockerRegistryAsync(string configuration, string username, string password, Action<string,int> PushCompleted)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, PushCompleted);

            var task = api.ApplicationPushToRegistryAsync(this.Id, configuration, username, password, progress.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }

        public async Task PublishAsync(string username, string password, string credentials, Action<string,int> PublishCompleted)
        {
            Progress progress = null;
            var taskBuild = CreateProgressTask(ref progress, PublishCompleted);

            var task = api.ApplicationPublishAsync(this.Id, credentials, username, password, progress.Id);
            await Task.Run(taskBuild);
            await task; // in this way exceptions will be generated
        }
    }
}
