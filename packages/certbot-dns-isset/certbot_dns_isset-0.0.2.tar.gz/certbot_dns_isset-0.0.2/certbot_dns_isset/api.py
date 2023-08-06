# -*- coding: utf-8 -*-=
"""
API object
"""
import requests

TIMEOUT = 3


def url(endpoint: str, path: str) -> str:
    """
    :param endpoint:
    :param path:
    :return:
    """
    return endpoint + '/' + path


class Api(object):
    def __init__(self, endpoint=None, token=None):
        """
        :param token:
        """
        assert isinstance(token, str), "Token is not a string"
        assert endpoint is not None and endpoint is not "", "No endpoint has been provided"
        assert token is not None and token is not "", "No token has been provided"

        self.endpoint = endpoint
        self.token = token
        self.headers = self._get_auth_header()
        self.http_check_states = {
            200: True,
            404: False,
        }
        self.http_actionable_states = {
            201: True,
            204: True,
        }

    def _get_auth_header(self) -> dict:
        """
        :return:
        """
        return {
            'Content-Type': 'application/json',
            'User-Agent': 'Certbot DNS Isset',
            'Authorization': 'Bearer {0}'.format(self.token)
        }

    def to_dict(self, response: requests.Response) -> dict:
        """
        :param response:
        :return:
        """
        return response.json()

    def get(self, path: str, params: dict) -> requests.Response:
        """
        :param path:
        :param params:
        :return:
        """
        print("Calling GET on " + url(self.endpoint, path) + " with params: " + str(params))
        return requests.get(
            url=url(self.endpoint, path),
            params=params,
            headers=self.headers,
            timeout=TIMEOUT,
        )

    def exists(self, response: requests.Response) -> bool:
        """
        :param response:
        :return:
        """
        return self.http_check_states.get(response.status_code, False)

    def create(self, path: str, data: dict) -> bool:
        """
        :param path:
        :param data:
        :return:
        """
        print("Calling POST on " + url(self.endpoint, path) + " with params: " + str(data))
        return self.http_actionable_states.get(
            requests.post(
                url=url(self.endpoint, path),
                json=data,
                headers=self.headers,
                timeout=TIMEOUT,
            ).status_code,
            False
        )

    def delete(self, path: str, id: int) -> bool:
        """
        :param id:
        :param path:
        :return:
        """
        print("Calling DELETE on " + url(self.endpoint, path) + "/" + str(id))

        return self.http_actionable_states.get(
            requests.delete(
                url=url(self.endpoint, path) + "/" + str(id),
                headers=self.headers,
                timeout=TIMEOUT,
            ).status_code, False)
