using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.ComponentModel;

namespace TorizonAppDeploymentAPI
{
    public class Platform : TorizonRestAPI.Model.Platform, IObjectsCollectionItem<TorizonRestAPI.Model.Platform>, ITorizonAPPDeploymentAPIObject, INotifyPropertyChanged
    {
        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        TorizonRestAPI.Api.PlatformsApi api;

        public event PropertyChangedEventHandler PropertyChanged;

        public Platform(TorizonRestAPI.Model.Platform model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Platform>(model, this, PropertyChanged);

            this.api = new TorizonRestAPI.Api.PlatformsApi();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full)
        {
            TorizonRestAPI.Model.Platform model = Utils.ObjectOrException<TorizonRestAPI.Model.Platform>(await api.PlatformGetAsync(this.Id));

            Update(model);
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotSupportedException();
        }
        public void Update(TorizonRestAPI.Model.Platform model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Platform>(model, this, PropertyChanged);
        }

        public async Task<List<TargetDevice>> GetCompatibleDevices(IObjectsCollectionInstantiator<TargetDevice, TorizonRestAPI.Model.TargetDevice> instantiator)
        {
            List<TorizonRestAPI.Model.TargetDevice> models = Utils.ObjectOrException<List<TorizonRestAPI.Model.TargetDevice>>(await api.PlatformCompatibledevicesGetAsync(this.Id));

            List<TargetDevice> devices = new List<TargetDevice>();

            foreach(TorizonRestAPI.Model.TargetDevice model in models)
            {
                devices.Add(instantiator.NewObjectFromModel(model));
            }
            return devices;
        }
    }

    public class PlatformInstantiator : IObjectsCollectionInstantiator<Platform, TorizonRestAPI.Model.Platform>
    {
        public Platform NewObjectFromModel(TorizonRestAPI.Model.Platform model)
        {
            return new Platform(model);
        }
    }

    public class Platforms : ObjectsCollection<Platform, TorizonRestAPI.Model.Platform>, ITorizonAPPDeploymentAPIObject
    {
        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        private TorizonRestAPI.Api.PlatformsApi api;

        /// <summary>
        /// Runtime value (C/C++ etc.) used to filter the platforms
        /// </summary>
        private string runtime;

        public Platforms(string runtime) : this(new PlatformInstantiator())
        {
            this.runtime = runtime;
        }

        protected Platforms(IObjectsCollectionInstantiator<Platform,TorizonRestAPI.Model.Platform> instantiator) : base("Name",instantiator)
        {
            api=new TorizonRestAPI.Api.PlatformsApi();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted,bool full)
        {
            List<TorizonRestAPI.Model.Platform> modelplatforms = Utils.ObjectOrException<List<TorizonRestAPI.Model.Platform>>(await api.PlatformsGetAsync(this.runtime));

            Update(modelplatforms);
            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }

        public Platform GetPlatformById(string id)
        {
            foreach (Platform p in this)
            {
                if (p.Id == id)
                    return p;
            }
            return null;
        }
    }
}
