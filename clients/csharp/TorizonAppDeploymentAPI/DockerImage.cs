using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    /// <summary>
    /// Class used to manage summary information about an image
    /// </summary>
    public class DockerImage : TorizonRestAPI.Model.DockerImage, IObjectsCollectionItem<TorizonRestAPI.Model.DockerImage>, INotifyPropertyChanged, ITorizonAPPDeploymentAPIObject
    {
        TorizonRestAPI.Api.DevicesApi api;

        public TargetDevice Device { get; private set; }

        public DockerImage(TorizonRestAPI.Model.DockerImage model, TargetDevice device)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.DockerImage>(model, this, PropertyChanged);
            api = TorizonAPIManager.GetDevicesApi();

            this.Device = device;
        }

        public string Name
        {
            get
            {
                if ((this.RepoTags == null) || (this.RepoTags.Count==0) || (this.RepoTags[0] == null))
                    return "";

                return RepoTags[0];
            }
        }

        public DateTime CreatedDate
        {
            get
            {
                return DateTime.Parse(this.Created, null, System.Globalization.DateTimeStyles.RoundtripKind);
            }
        }        

        public event PropertyChangedEventHandler PropertyChanged;

        public void Update(TorizonRestAPI.Model.DockerImage model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.DockerImage>(model, this,PropertyChanged);
        }

        public async Task DeleteAsync()
        {
            await api.ImagesDeleteimageAsync(this.Device.Id,this.Id);
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            TorizonRestAPI.Model.DockerImage model = Utils.ObjectOrException<TorizonRestAPI.Model.DockerImage>(await api.ImagesGetimageAsync(this.Device.Id,this.Id));
            this.Update(model);
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }
    }
    class DockerImageInstantiator : IObjectsCollectionInstantiator<DockerImage, TorizonRestAPI.Model.DockerImage>
    {
        TargetDevice device;

        public DockerImageInstantiator(TargetDevice device)
        {
            this.device = device;
        }

        public DockerImage NewObjectFromModel(TorizonRestAPI.Model.DockerImage model)
        {
            return new DockerImage(model,device);
        }
    }

    /// <summary>
    /// Class used to store list of images
    /// </summary>
    public class DockerImages : ObjectsCollection<DockerImage, TorizonRestAPI.Model.DockerImage>, ITorizonAPPDeploymentAPIObject
    {
        /// <summary>
        /// Client used to read information (shared with device)
        /// </summary>
        TorizonRestAPI.Api.DevicesApi api;
        TargetDevice device;

        public DockerImages(TargetDevice device) : base("Id",new DockerImageInstantiator(device))
        {
            this.api = TorizonAPIManager.GetDevicesApi();
            this.device = device;
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            List<TorizonRestAPI.Model.DockerImage> imagelist = Utils.ObjectOrException<List<TorizonRestAPI.Model.DockerImage>>(await api.DeviceGetimagesAsync(this.device.Id));

            Update(imagelist);
            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public async Task DeleteImageAsync(string id)
        {
            DockerImage img = GetObject(id) as DockerImage;

            await img.DeleteAsync();
            RemoveObject(img.Id);
        }
    }
}
