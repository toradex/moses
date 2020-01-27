using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    /// <summary>
    /// Class used to store summary information about a container
    /// </summary>
    public class DockerContainer : TorizonRestAPI.Model.DockerContainer, IObjectsCollectionItem<TorizonRestAPI.Model.DockerContainer>, INotifyPropertyChanged, ITorizonAPPDeploymentAPIObject
    {
        TorizonRestAPI.Api.DevicesApi api;

        /// <summary>
        /// Processes running inside the container
        /// </summary>
        Processes processes;

        /// <summary>
        /// Storage information
        /// </summary>
        MountPoints mountpoints;

        /// <summary>
        /// Memory information
        /// </summary>
        MemInfo meminfo;

        public Processes Processes { get => processes;  }
        public MountPoints MountPoints { get => mountpoints; }
        public MemInfo MemInfo { get => meminfo; }


        public TargetDevice Device { get; private set; }

        public DockerContainer(TorizonRestAPI.Model.DockerContainer model,TargetDevice device)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.DockerContainer>(model, this, PropertyChanged);
            api = new TorizonRestAPI.Api.DevicesApi();

            this.Device = device;

            this.processes = new Processes(this);
            this.mountpoints = new MountPoints(this);
            this.meminfo = new MemInfo(this);
        }

        public DateTime CreatedDate
        {
            get
            {
                return DateTime.Parse(this.Created, null, System.Globalization.DateTimeStyles.RoundtripKind);
            }
        }

        protected string imagename;

        public string ImageName
        {
            get
            {
                return imagename;
            }

            set
            {
                if (value!=ImageName)
                {
                    imagename = value;
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("ImageName"));
                }
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        public void Update(TorizonRestAPI.Model.DockerContainer model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.DockerContainer>(model, this, PropertyChanged);
        }

        public async Task DeleteAsync()
        {
            await api.ContainersDeletecontainerAsync(this.Device.Id, this.Id);
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            TorizonRestAPI.Model.DockerContainer model = Utils.ObjectOrException<TorizonRestAPI.Model.DockerContainer>(await api.ContainersGetcontainerAsync(this.Device.Id,this.Id));
            this.Update(model);

            if ((full)&&(this.State.Status == TorizonRestAPI.Model.DockerContainerState.StatusEnum.Running))
            {
                await this.processes.RefreshAsync(null, false);
                await this.mountpoints.RefreshAsync(null, false);
                await this.meminfo.RefreshAsync(null, false);
            }

            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

    }

    public class DockerContainerInstantiator : IObjectsCollectionInstantiator<DockerContainer, TorizonRestAPI.Model.DockerContainer>
    {
        TargetDevice device;

        public DockerContainerInstantiator(TargetDevice device)
        {
            this.device = device;
        }

        public DockerContainer NewObjectFromModel(TorizonRestAPI.Model.DockerContainer model)
        {
            return new DockerContainer(model,device);
        }
    }

    /// <summary>
    /// Class used to store list of images
    /// </summary>
    public class DockerContainers : ObjectsCollection<DockerContainer, TorizonRestAPI.Model.DockerContainer>, ITorizonAPPDeploymentAPIObject
    {
        /// <summary>
        /// Client used to read information (shared with device)
        /// </summary>
        TorizonRestAPI.Api.DevicesApi api;

        TargetDevice device;

        /// <summary>
        /// We need a ref to the image list to be able to get image name
        /// </summary>
        DockerImages images;

        public DockerContainers(TargetDevice device) : base("Name", new DockerContainerInstantiator(device))
        {
            api = new TorizonRestAPI.Api.DevicesApi();
            this.device = device;
            this.images = device.Images;
        }

        public async Task RefreshAsync(Action OnRefreshCompleted,bool full)
        {
            List<TorizonRestAPI.Model.DockerContainer> containerslist = Utils.ObjectOrException<List<TorizonRestAPI.Model.DockerContainer>>(await api.DeviceGetcontainersAsync(this.device.Id));

            Update(containerslist);

            foreach (DockerContainer container in this)
            {
                DockerImage img = images.GetObject(container.Image);

                if (img != null)
                    container.ImageName = img.Name;
            }

            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public async Task DeleteContainerAsync(string name)
        {
            DockerContainer container = GetObject(name) as DockerContainer;

            await container.DeleteAsync();
            RemoveObject(container.Name);
        }
    }

}
