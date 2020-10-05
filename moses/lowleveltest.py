import json
from docker import APIClient, DockerClient

client = DockerClient.from_env()
apiclient = client.api
resp = apiclient.build(
    path="/home/valter/Work/demos/broccolinator/broccolinator-hw/appconfig_2/work",
    dockerfile="/home/valter/Work/demos/broccolinator/broccolinator-hw/appconfig_2/work/Dockerfile.debug",
    tag="dummy000",
    pull=False,
)
for r in resp:
    line = json.loads(r)
    print(line)

