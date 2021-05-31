
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.applications_api import ApplicationsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from moses_client.api.applications_api import ApplicationsApi
from moses_client.api.devices_api import DevicesApi
from moses_client.api.eulas_api import EulasApi
from moses_client.api.platforms_api import PlatformsApi
from moses_client.api.progress_api import ProgressApi
from moses_client.api.setup_api import SetupApi
from moses_client.api.version_api import VersionApi
