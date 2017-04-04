import requests
from urllib import parse
from affilitest import endpoints

class AffiliTest(object):
  def __init__(self, email, password):
    self.email = email
    self.password = password


  def login(self):
    return self._post(endpoints.LOGIN, {'email' : self.email, 'password' : self.password})

  def logout(self):
    return self._get(endpoints.LOGOUT)

  def app_info(self, url = None, package = None, country = None):
    if url is None and package is None:
      raise APIException('No parameters were passed to appInfo', endpoints.APPINFO)
    if url is not None and package is not None:
      raise APIException('Only one parameter should be passed', endpoints.APPINFO)
    if url is not None:
      return self._app_info_fetch(url, 'url')
    return self._app_info_fetch(package, 'package', country)

  def _app_info_fetch(self, data, type, country = None):
    payload = {type : data}
    if country:
      payload['country'] = country
    return self._get(endpoints.APPINFO, payload)

  def test(self, url, country, device):
    return self._post(endpoints.TEST, {
      'url' : parse.quote(url),
      'country' : country,
      'device' : device
    })

  def compare_to_preview(self, url, preview_url, country, device):
    return self._post(endpoints.TEST, {
      'url' : parse.quote(url),
      'previewURL' : parse.quote(preview_url),
      'country' : country,
      'device' : device
    })

  def _post(self, endpoint, payload):
    self._last_response = self.requests_session().post(endpoint, data = payload)
    resData = self._last_response.json()
    if resData['error']:
      raise APIException(resData['error'], endpoint)
    return resData['data']

  def _get(self, endpoint, payload = None):
    url = endpoint
    if payload is not None:
      url = endpoint + '?' + parse.urlencode(payload)
    self._last_response = self.requests_session().get(url)
    resData = self._last_response.json()
    if resData['error']:
      raise APIException(resData['error'], endpoint)
    return resData['data']

  def last_response(self):
    return self._last_response

  def requests_session(self):
    if hasattr(self, '_request_session'):
      return self._request_session
    self._request_session = requests.Session()
    return self._request_session


class APIException(Exception):
  def __init__(self, error, endpoint):
    super(APIException, self).__init__(error, endpoint)
    self.endpoint = endpoint