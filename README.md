SendCM Python API Wrapper Documentation

SendCM Python API Wrapper Documentation
=======================================

The `SendCM` class provides a Python wrapper for interacting with the Send.cm API.

Installation
------------

To use the `SendCM` API wrapper, you need to have the `requests` library installed. You can install it using the following command:

    pip install requests

Usage
-----

1.  Import the required module and create a `SendCM` instance by providing your Send.cm API key:

    import requests
    from sendcm_api_wrapper import SendCM
    
    api_key = "your-api-key"
    sendcm = SendCM(api_key)
    

### Account Information

2.  Get account information:

    ```py
    account_info = sendcm.get_account_info()
    print(account_info)
    ```
    

3.  Get account statistics:

    ```py
    account_stats = sendcm.get_account_stats()
    print(account_stats)
    ```
    

### Uploading

4.  Get the next upload server URL and session key:

    ```py
    upload_info = sendcm.get_next_upload_server_url()
    print(upload_info)
    ```
    

5.  Upload a file from a remote URL:

    ```py
    remote_url = "https://example.com/path/to/remote/file.mp4"
    uploaded_file = sendcm.upload_remote_url(remote_url)
    print(uploaded_file)
    ```
    

### File Information

6.  Get information about a specific file:

    ```py
    file_code = "your-file-code"
    file_info = sendcm.get_file_info(file_code)
    print(file_info)
    ```
    


License
-------

This SendCM Python API Wrapper is provided under the MIT License.

* * *

For more information about the Send.cm API and its parameters, please refer to the [Send.cm API](https://github.com/immodded/send-cm/blob/main/sendcm.apib).