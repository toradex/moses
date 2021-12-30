using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TorizonAppDeploymentAPI
{
    public interface ITorizonAPPDeploymentAPIObject
    {
        Task RefreshAsync(Action OnRefreshCompleted, bool full, bool reboot = false);
        Task CommitAsync(Action OnCommitCompleted);
    }
}
