# -*- coding: utf-8 -*-=
"""
Certbot DNS Isset
"""

import zope.interface
from certbot import interfaces
from certbot.plugins import dns_common

from certbot_dns_isset.domain import Domain
from certbot_dns_isset.record import Record

DEFAULT_TTL: int = 60


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """
    Isset DNS Authenticator for dns-01 challenge
    """

    description = "Isset B.V. Authenticator plugin"

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):
        """
        :param add:
        :return:
        """
        super(Authenticator, cls).add_parser_arguments(add)
        add('credentials', help='Isset API credentials INI file.')

    def more_info(self):
        return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using ' + \
               'the Isset API.'

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'Isset credentials INI file',
            {
                'endpoint': 'API endpoint',
                'token': 'API JWT token (without Bearer part)',
            }
        )

    def _perform(self, domain, validation_name, validation):
        """
        :param domain:
        :param validation_name:
        :param validation:
        :return:
        """
        self._get_isset_dns_client().add_txt_record(domain, validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        """
        :param domain:
        :param validation_name:
        :param validation:
        :return:
        """
        self._get_isset_dns_client().remove_txt_record(domain, validation_name, validation)

    def _get_isset_dns_client(self):
        """
        :return:
        """
        return _IssetDnsClient(
            self.credentials.conf('endpoint'),
            self.credentials.conf('token')
        )


class _IssetDnsClient(object):
    """
    Handles Isset DNS API communication
    """

    def __init__(self, endpoint=None, token=None):
        """
        :param token:
        """
        self.ttl = DEFAULT_TTL
        self.endpoint = endpoint
        self.token = token

        assert self.endpoint is not None, "No endpoint has been provided"
        assert self.token is not None, "No token has been provided"

    def add_txt_record(self, domain: str, record_name: str, record_content: str):
        """
        :param record_name:
        :param domain:
        :param record_content:
        :return:
        """
        Record(
            endpoint=self.endpoint,
            token=self.token,
            domain=Domain(
                name=domain,
                endpoint=self.endpoint,
                token=self.token
            ),
            dns_type="TXT",
            name=record_name,
            content=record_content,
            ttl=DEFAULT_TTL
        ).persist()

    def remove_txt_record(self, domain: str, record_name: str, record_content: str):
        """
        :param record_content:
        :param domain:
        :param record_name:
        :return:
        """
        Record(
            endpoint=self.endpoint,
            token=self.token,
            domain=Domain(
                name=domain,
                endpoint=self.endpoint,
                token=self.token
            ),
            dns_type="TXT",
            name=record_name,
            content=record_content,
            ttl=DEFAULT_TTL
        ).desist()
