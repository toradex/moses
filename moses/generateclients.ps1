#!/bin/sh

docker run -v ${PWD}/..:/local openapitools/openapi-generator-cli generate -i /local/moses/swagger.yaml -g csharp -o /local/clients/csharp/TorizonAppDeploymentAPI/generated --additional-properties packageName=TorizonRestAPI --additional-properties targetFramework=v4.5
docker run -v ${PWD}/..:/local openapitools/openapi-generator-cli generate -i /local/moses/swagger.yaml -g python -o /local/clients/python --additional-properties packageName=moses_client
