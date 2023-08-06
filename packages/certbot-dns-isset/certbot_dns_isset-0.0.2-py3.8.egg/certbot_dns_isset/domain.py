# -*- coding: utf-8 -*-=
"""
Domain object
"""

from requests import Response

from certbot_dns_isset.api import Api


class Domain(object):
    def __init__(self, name: str, endpoint=None, token=None):
        """
        :param name:
        """
        assert isinstance(name, str), "Domain name is not a string"
        assert name.count('.') == 1, 'Domain name is not a first level domain (like: google.com)'
        assert isinstance(endpoint, str), 'Endpoint is not a string'
        assert isinstance(token, str), 'Token is not a string'

        self.name = name
        self.api = Api(endpoint, token)
        self.path = "domain"

        assert self.exists(), "Domain is not recognised by API"

    def _get(self) -> Response:
        return self.api.get(
            self.path, {
                'name': self.name
            }
        )

    def to_dict(self):
        """
        :return:
        """
        return self.api.to_dict(
            self._get()
        )

    def exists(self):
        """
        :return:
        """
        return self.api.exists(
            self._get()
        )
