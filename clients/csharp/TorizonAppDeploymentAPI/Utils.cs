using System;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;
using System.Reflection;
using TorizonRestAPI.Api;
using TorizonRestAPI.Model;
using System.Threading;

namespace TorizonAppDeploymentAPI
{
    /// <summary>
    /// Used to support read only properties that must be removed from PUT requests
    /// </summary>
    public interface IReadOnlyPropertiesList
    {
        string [] ReadOnlyProperties { get;  }
    }

    public static class Utils
    {
        /// <summary>
        /// Generates and object with all read-only properties set to null, to prevend validation issues on PUT requests
        /// </summary>
        /// <typeparam name="T">Must be a TorizonRestAPI.Model object with nullable properties</typeparam>
        /// <param name="source">Object with all properties (readonly and modifiable ones)</param>
        /// <returns>Instance where all read-only properties are set to null</returns>
        public static T GetRequestObject<T>(T source) where T : new()
        {
            T dest = new T();
            IReadOnlyPropertiesList roprops = source as IReadOnlyPropertiesList;
            string[] readOnlyProps = roprops?.ReadOnlyProperties;

            foreach (PropertyInfo p in typeof(T).GetProperties())
            {
                if (!p.CanWrite)
                    continue;

                if ((readOnlyProps==null) || (readOnlyProps.Contains(p.Name)))
                    continue;

                object val = p.GetValue(source, null);
                p.SetValue(dest, val);
            }

            return dest;
        }
        public static void CopyProperties<T>(this T source, T dest, PropertyChangedEventHandler propertyChanged=null, bool notifyall=false)
        {
            var props = typeof(T).GetProperties().Where(x => x.CanWrite).ToList();

            foreach (var prop in props)
            {
                object sourceval = prop.GetValue(source, null);
                object destval = prop.GetValue(dest, null);
                bool notify = notifyall;

                if (sourceval == null)
                {
                    if (destval!=null)
                    {
                        prop.SetValue(dest, null);
                        notify = true;
                    }
                }
                else
                {
                    if (!sourceval.Equals(destval))
                    {
                        prop.SetValue(dest, sourceval);
                        notify = true;
                    }
                }

                if (prop.PropertyType.FullName.StartsWith("TorizonRestAPI.Model."))
                {
                    notify = true;
                }

                if (notify)
                    propertyChanged?.Invoke(dest, new PropertyChangedEventArgs(prop.Name));
            }
        }

        public static T ObjectOrException<T>(object obj)
        {
            if (obj is T)
            {
                return (T)obj;
            }

            if (obj is TorizonRestAPI.Model.ErrorInfo)
            {
                throw new TorizonAPIException((TorizonRestAPI.Model.ErrorInfo)obj);
            }

            throw new Exception("Invalid API return type.");
        }

        public static void OkOrException(object obj)
        {
            if (obj == null)
                return;

            if (obj is TorizonRestAPI.Model.ErrorInfo)
            {
                TorizonRestAPI.Model.ErrorInfo ei = obj as TorizonRestAPI.Model.ErrorInfo;

                if ((ei.Code >= 200) && (ei.Code < 300))
                    return;

                throw new TorizonAPIException((TorizonRestAPI.Model.ErrorInfo)obj);
            }

            throw new Exception("Invalid API return type.");
        }

        public static async Task<bool> CheckDockerAsync()
        {
            try
            {
                TorizonRestAPI.Api.VersionApi api = TorizonAPIManager.GetVersionApi();
                TorizonRestAPI.Model.DockerVersion dockerVersion = Utils.ObjectOrException<TorizonRestAPI.Model.DockerVersion>(await api.VersionDockerAsync());
            }
            catch (Exception)
            {
                return false;
            }
            return true;
        }

        public static async Task PullContainersAsync(Action<Exception, string, int> operationCompleted=null)
        {
            try
            {
                TorizonRestAPI.Api.SetupApi api = new TorizonRestAPI.Api.SetupApi();
                ProgressApi progressApi = new ProgressApi();
                Progress progress = progressApi.ProgressCreate();

                _ = api.SetupPullcontainersAsync(progress.Id);

                // check the status
                await Task.Run(() => {
                    while (progress.Pending)
                    {
                        progress = progressApi.ProgressStatus(progress.Id);

                        foreach (string msg in progress.Messages)
                        {
                            operationCompleted?.Invoke(null, msg, progress._Progress);
                        }
                    }

                    // send 100% for the current task
                    operationCompleted?.Invoke(null, "Done", 100);
                });
            }
            catch (Exception e)
            {
                operationCompleted?.Invoke(e, null, 0);
            }
        }

    }
}

namespace TorizonRestAPI.Client
{
    /// <summary>
    /// API client is mainly responsible for making the HTTP call to the API backend.
    /// </summary>
    public partial class GlobalConfiguration : Configuration
    {
        public GlobalConfiguration()
        {
            Timeout = 1800000;
        }
    }

}
