# DefaultApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**apiDiffPost**](#apidiffpost) | **POST** /api/diff | make a diff (Myers) from two text input|

# **apiDiffPost**
> DiffPrettypResponse apiDiffPost(diffPrettypRequest)


### Example

```typescript
import {
    DefaultApi,
    Configuration,
    DiffPrettypRequest
} from '@it.diamondnet/coding-challenge-125';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let diffPrettypRequest: DiffPrettypRequest; //

const { status, data } = await apiInstance.apiDiffPost(
    diffPrettypRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **diffPrettypRequest** | **DiffPrettypRequest**|  | |


### Return type

**DiffPrettypResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Diff result |  -  |
|**422** | Validation error - check format of request body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

