# Affilitest-Python
AffiliTest API implemented in Python


## Examples of usage

### Testing
  * Regular testing and compare to preview - [Example code](example.testing.py)
  * Multithreaded example (Checking multiple offers) - [Example code](example.testing.multithreaded.py)

### App Info
  [Example code](example.appinfo.py)

### Calls Left
  [Example code](example.callsleft.py)

### Retrieving HTTP Status codes
  In order to view the redirections' status codes, a query string is needed to be appended to the endpoints.

  Open the [endpoints.py](affilitest/endpoints.py) file and append `?codes` to the desired endpoint.

  Currently, only `/test` and `/compareToPreview` are the ones which support this feature.

  ```
  ...
  POST https://affilitest.com/api/v1/test?codes
  ...
  HTTP 200 OK
  ...
  {
    error: null,
    meta: {
      codes : [200, 301, 302]
    },
    data: ["example.com", "redirection.com", "destination.com"]
  }

  ```