#
# Copyright 2013 Mortar Data Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import logging
from functools import wraps
from time import sleep

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)


def retry_with_backoff(function_to_decorate=None):
    def _decorate(func):
        t = 1.0
        sleep_times = []
        while sum(sleep_times) <= 30:
            sleep_times.append(t)
            t = 2*t
        sleep_times[-1] = StopIteration

        @wraps(func)
        def wrapper(*args, **kwargs):
            for sleep_time in sleep_times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if sleep_time == StopIteration:
                        # raise the exception
                        requests_log.warn('Failed to run %s after several retries' % func.__name__)
                        raise e
                    else:
                        requests_log.warn('Unable to run %s. Sleeping [%s] seconds and retrying' % (func.__name__, sleep_time), exc_info=True)
                        sleep(sleep_time)

        return wrapper

    if function_to_decorate:
        return _decorate(function_to_decorate)

    return _decorate


class API(object):
    """
    Represents a connection to the Mortar API.
    """

    HEADERS = {'Accept': 'application/json',
               'Accept-Encoding': 'gzip',
               'Content-Type': 'application/json',
               # TODO add version
               'User-Agent': 'mortar-api-python'}

    def __init__(self, email, api_key, scheme='https', host='mdog.datadoghq.com'):
        """

        :type email: string
        :param email: Your Mortar user email address

        :type api_key: string
        :param api_key: Your Mortar api_key, available from https://app.mortardata.com/user#!/api

        :type scheme: string
        :param scheme: http or https.  Defaults to https.

        :type host: string
        :param host: Mortar API hostname.  Defaults to mdog.datadoghq.com.
        """

        self.auth = HTTPBasicAuth(email, api_key)
        self.scheme = scheme
        self.host = host

    def url(self, path):
        """
        Get a full API URL from a subpath.  For example,
        jobs => https://mdog.datadoghq.com/v2/jobs

        :type path: string
        :param path: subpath

        :rtype: str:
        :returns: full URL
        """
        return '%s://%s/v2/%s' % (self.scheme, self.host, path)

    @retry_with_backoff
    def post(self, path, payload):
        """
        Post to the API.

        :type path: string
        :param path: sub-path to post to (e.g. jobs)

        :raises: requests.exception.HTTPError: if a 40x or 50x error occurs

        :rtype: str:
        :returns: json response
        """

        # prep
        post_url = self.url(path)
        json_payload = json.dumps(payload)

        # request
        response = requests.post(post_url, data=json_payload, auth=self.auth, headers=API.HEADERS)

        # test and return
        self.raise_for_status(response)
        return response.json()

    @retry_with_backoff
    def get(self, path, params=None):
        """
        Get from the API.

        :type path: string
        :param path: sub-path to get (e.g. jobs/XYZ)

        :raises: requests.exception.HTTPError: if a 40x or 50x error occurs

        :rtype: str:
        :returns: json response
        """

        # prep
        get_url = self.url(path)

        # request
        response = requests.get(get_url, params=params, auth=self.auth, headers=API.HEADERS)

        # test and return
        self.raise_for_status(response)
        return response.json()

    @retry_with_backoff
    def put(self, path, payload):
        """
        Put to the API.

        :type path: string
        :param path: sub-path to put (e.g. jobs/XYZ)

        :raises: requests.exception.HTTPError: if a 40x or 50x error occurs

        :rtype: str:
        :returns: json response
        """

        # prep
        put_url = self.url(path)
        json_payload = json.dumps(payload)

        # request
        response = requests.put(put_url, data=json_payload, auth=self.auth, headers=API.HEADERS)

        # test and return
        self.raise_for_status(response)
        return response.json()

    @retry_with_backoff
    def delete(self, path):
        """
        Delete from the API.

        :type path: string
        :param path: sub-path to delete (e.g. jobs/XYZ)

        :raises: requests.exception.HTTPError: if a 40x or 50x error occurs
        """

        # prep
        delete_url = self.url(path)

        # request
        response = requests.delete(delete_url, auth=self.auth, headers=API.HEADERS)

        # test and return
        self.raise_for_status(response)

    @retry_with_backoff
    def delete_with_payload(self, path, payload):
        """
        Delete from the API.

        :type path: string
        :param path: sub-path to delete (e.g. jobs/XYZ)

        :raises: requests.exception.HTTPError: if a 40x or 50x error occurs
        """

        # prep
        delete_url = self.url(path)
        json_payload = json.dumps(payload)

        # request
        response = requests.delete(delete_url, data=json_payload, auth=self.auth, headers=API.HEADERS)

        # test and return
        self.raise_for_status(response)

    def raise_for_status(self, response):
        """Raises stored :class:`HTTPError`, if one occurred."""

        http_error_msg = ''

        if 400 <= response.status_code < 500:
            http_error_msg = '%s Client Error: %s\n%s' % \
                (response.status_code, response.reason, response.text)

        elif 500 <= response.status_code < 600:
            http_error_msg = '%s Server Error: %s' % (response.status_code, response.reason)

        if http_error_msg:
            raise HTTPError(http_error_msg, response=response)

