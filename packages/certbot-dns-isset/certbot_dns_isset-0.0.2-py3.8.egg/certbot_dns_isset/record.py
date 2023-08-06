# -*- coding: utf-8 -*-=
"""
Domain object
"""

from requests import Response

from certbot_dns_isset.api import Api
from certbot_dns_isset.domain import Domain


class Record(object):
    allowed_dns_types = [
        'A',
        'AAAA',
        'ALIAS',
        'CNAME',
        'MX',
        'NS',
        'PTR',
        'SOA',
        'SRV',
        'TXT'
    ]

    def __init__(self, endpoint: str, token: str, domain: Domain, name: str, dns_type: str, content: str, ttl: int):
        """
        :param domain:
        :param dns_type:
        :param content:
        :param ttl:
        """
        assert isinstance(endpoint, str), 'Endpoint is not a string'
        assert isinstance(token, str), 'Token is not a string'
        assert isinstance(domain, Domain), 'Domain instance not provided'
        assert isinstance(name, str), 'Name type is not a string'
        assert isinstance(dns_type, str), 'DNS type is not a string'
        assert dns_type in self.allowed_dns_types, 'DNS type is not allowed'
        assert isinstance(content, str), 'Content is not a string'
        assert isinstance(ttl, int), 'TTL is not an integer'

        self.domain = domain
        self.name = name
        self.dns_type = dns_type
        self.content = content
        self.ttl = ttl
        self.api = Api(endpoint, token)
        self.path = 'dnsRecord'

    def _get(self) -> Response:
        """
        :return:
        """
        return self.api.get(
            self.path, {
                'name': self.name,
                'type': self.dns_type,
                'content': self.content
            }
        )

    def exists(self) -> bool:
        """
        :return:
        """
        return self.api.exists(
            self._get()
        )

    def persist(self) -> bool:
        """
        :return:
        """
        return self.api.create(
            path=self.path,
            data={
                'powerDnsDomain': self.domain.to_dict().get('id'),
                'type': self.dns_type,
                'content': self.content,
                'ttl': self.ttl,
                'name': self.name,
            }
        )

    def desist(self) -> bool:
        """
        :return:
        """
        # First obtain record to get ID before deletion
        record = self.api.to_dict(
            self._get()
        )

        assert isinstance(record, dict), 'Returned record is no dictionary'
        assert record, 'Returned record is empty'

        return self.api.delete(
            self.path,
            record.get('id')
        )
