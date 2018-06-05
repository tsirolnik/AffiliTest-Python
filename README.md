# Affilitest-Python
AffiliTest API implemented in Python

## Installation
  * Clone the repo `git clone https://github.com/tsirolnik/AffiliTest-Python.git`
  * Run `sudo python setup.py install` (Linux) or `python setup.py install` (Windows)

The API will be available via the affilitest package and importing it as the following will then work
```
> python3
Python 3.5.3 (default)
[GCC 6.0.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import affilitest
>>> affilitest
<module 'affilitest' from '/home/user/development/AffiliTest-Python/affilitest/__init__.py'>
```

Please view the examples in order to understand how to use the package.

## Examples

### Testing
  * Regular testing and compare to preview - [Example code](examples/example.testing.py)
  * Multithreaded example (Checking multiple offers) - [Example code](examples/example.testing.multithreaded.py)

### App Info
  [Example code](examples/example.appinfo.py)

### Calls Left
  [Example code](examples/example.callsleft.py)

### Retrieving HTTP Status codes
  In order to view the redirections' status codes, a query string is needed to be appended to the endpoints.

  Open the [endpoints.py](affilitest/endpoints.py) file and append the `?codes` string to the desired endpoint.

  Currently, only `/test` and `/compareToPreview` are the endpoints which support this feature. 
  
  For example - 

  ```python
  # affilitest/endpoints.py
  # Original
  TEST = __MAIN + 'api/v1/test'
  # In order to retrieve the codes
  # After editing
  TEST = __MAIN + 'api/v1/test?codes'
  ```

  And the result output
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