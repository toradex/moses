using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.ComponentModel;

namespace TorizonAppDeploymentAPI
{
    public class Eula : TorizonRestAPI.Model.Eula, IObjectsCollectionItem<TorizonRestAPI.Model.Eula>, ITorizonAPPDeploymentAPIObject, INotifyPropertyChanged
    {
        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        private TorizonRestAPI.Api.EulasApi api;

        public event PropertyChangedEventHandler PropertyChanged;

        public Eula(TorizonRestAPI.Model.Eula model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Eula>(model, this, PropertyChanged);

            api = TorizonAPIManager.GetEulasApi();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full, bool reboot = false)
        {
            TorizonRestAPI.Model.Eula model = Utils.ObjectOrException<TorizonRestAPI.Model.Eula>(await api.EulaGetAsync(this.Id));

            Update(model);
        }

        public async Task CommitAsync(Action OnCommitCompleted)
        {
            TorizonRestAPI.Model.Eula model = Utils.ObjectOrException<TorizonRestAPI.Model.Eula>(await api.EulaModifyAsync(this.Id, this));
            Utils.CopyProperties<TorizonRestAPI.Model.Eula>(model, this, PropertyChanged, true);
            OnCommitCompleted?.Invoke();
        }

        public void Update(TorizonRestAPI.Model.Eula model)
        {
            Utils.CopyProperties<TorizonRestAPI.Model.Eula>(model, this, PropertyChanged);
        }
    }

    public class EulaInstantiator : IObjectsCollectionInstantiator<Eula, TorizonRestAPI.Model.Eula>
    {
        public Eula NewObjectFromModel(TorizonRestAPI.Model.Eula model)
        {
            return new Eula(model);
        }
    }

    public class Eulas : ObjectsCollection<Eula, TorizonRestAPI.Model.Eula>, ITorizonAPPDeploymentAPIObject
    {
        /// <summary>
        /// Client used to access the REST interface
        /// </summary>
        private TorizonRestAPI.Api.EulasApi api;

        public Eulas() : this(new EulaInstantiator())
        {
        }

        protected Eulas(IObjectsCollectionInstantiator<Eula, TorizonRestAPI.Model.Eula> instantiator) : base("Id", instantiator)
        {
            api = TorizonAPIManager.GetEulasApi();
        }

        public async Task RefreshAsync(Action OnRefreshCompleted, bool full, bool reboot = false)
        {
            List<TorizonRestAPI.Model.Eula> modeleulas = Utils.ObjectOrException<List<TorizonRestAPI.Model.Eula>>(await api.EulasGetAsync());

            Update(modeleulas);
            OnRefreshCompleted?.Invoke();
        }

        public Task CommitAsync(Action OnCommitCompleted)
        {
            throw new NotImplementedException();
        }
    }

}
