using TorizonRestAPI.Api;

namespace TorizonAppDeploymentAPI
{
    public class TorizonAPIManager
    {
        public static DevicesApi GetDevicesApi()
        {
            DevicesApi api = new DevicesApi();

            api.ExceptionFactory = TorizonAPIException.DefaultExceptionFactory;
            return api;
        }

        public static ApplicationsApi GetApplicationsApi()
        {
            ApplicationsApi api = new ApplicationsApi();

            api.ExceptionFactory = TorizonAPIException.DefaultExceptionFactory;
            return api;
        }

        public static PlatformsApi GetPlatformsApi()
        {
            PlatformsApi api = new PlatformsApi();

            api.ExceptionFactory = TorizonAPIException.DefaultExceptionFactory;
            return api;
        }

        public static VersionApi GetVersionApi()
        {
            VersionApi api = new VersionApi();

            api.ExceptionFactory = TorizonAPIException.DefaultExceptionFactory;
            return api;
        }

        public static SetupApi GetSetupApi()
        {
            SetupApi api = TorizonAPIManager.GetSetupApi();

            api.ExceptionFactory = TorizonAPIException.DefaultExceptionFactory;
            return api;
        }
        
    }
}
