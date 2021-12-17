#!/bin/sh

# csharp
docker run `
    --rm `
    -v ${PWD}/..:/local `
    openapitools/openapi-generator-cli `
    generate `
    -i /local/moses/swagger.yaml `
    -g csharp `
    -o /local/clients/csharp/TorizonAppDeploymentAPI/generated `
    --additional-properties packageName=TorizonRestAPI `
    --additional-properties targetFramework=v4.5

# python
docker run `
    --rm `
    -v ${PWD}/..:/local `
    openapitools/openapi-generator-cli `
    generate `
    -i /local/moses/swagger.yaml `
    -g python `
    -o /local/clients/python `
    --additional-properties packageName=moses_client

# typescript
docker run `
    --rm `
    -v ${PWD}/..:/local `
    openapitools/openapi-generator-cli `
    generate `
    -i /local/moses/swagger.yaml `
    -g typescript-node `
    -o /local/clients/typescript `
    --additional-properties npmName=torizonrestapi `
    --additional-properties supportsES6=true
