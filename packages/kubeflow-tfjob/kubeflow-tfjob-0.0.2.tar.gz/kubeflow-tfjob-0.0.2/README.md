# Kubeflow TFJob SDK
Python SDK for TF-Operator

## Requirements.

Python 2.7 and 3.5+

## Installation & Usage
### pip install

```sh
pip install kubeflow-tfjob
```

Then import the package:
```python
import kubeflow.tfjob 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)


## Getting Started

Please follow the [sample](../../examples/sdk/tfjob-sdk.ipynb) to create, update and delete TFJob.

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
[TFJobClient](docs/TFJobClient.md) | [create](docs/TFJobClient.md#create) | Create TFJob|
[TFJobClient](docs/TFJobClient.md) | [get](docs/TFJobClient.md#get)    | Get or watch the specified TFJob or all TFJob in the namespace |
[TFJobClient](docs/TFJobClient.md) | [patch](docs/TFJobClient.md#patch)  | Patch the specified TFJob|
[TFJobClient](docs/TFJobClient.md) | [delete](docs/TFJobClient.md#delete) | Delete the specified TFJob |

## Documentation For Models

 - [V1JobCondition](docs/V1JobCondition.md)
 - [V1JobStatus](docs/V1JobStatus.md)
 - [V1ReplicaSpec](docs/V1ReplicaSpec.md)
 - [V1ReplicaStatus](docs/V1ReplicaStatus.md)
 - [V1TFJob](docs/V1TFJob.md)
 - [V1TFJobList](docs/V1TFJobList.md)
 - [V1TFJobSpec](docs/V1TFJobSpec.md)

