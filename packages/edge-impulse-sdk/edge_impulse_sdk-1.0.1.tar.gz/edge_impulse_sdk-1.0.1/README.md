# Edge Impulse Python SDK

This is the Python SDK to interact with the [Edge Impulse API](https://docs.edgeimpulse.com/reference-link/edge-impulse-api). At Edge Impulse we enable developers to create the next generation of intelligent device solutions with embedded Machine Learning.

## How to install

Install using via pip (Python 2.7 or Python 3.4+):

```
$ pip3 install edge_impulse_sdk
```

## Usage

```py
import edge_impulse_sdk.openapi_client as ei_sdk

# Enter your API key and project ID here
API_KEY = 'ei_...'
PROJECT_ID = 12

configuration = ei_sdk.Configuration()
configuration.api_key['x-api-key'] = API_KEY

# Create an instance of the raw data API
raw_data_api = ei_sdk.RawDataApi(ei_sdk.ApiClient(configuration))

# And list all examples in your training set
samples = raw_data_api.list_samples(PROJECT_ID, 'training')
print('Samples', samples)
```

For more examples head over to the [documentation](https://docs.edgeimpulse.com).
