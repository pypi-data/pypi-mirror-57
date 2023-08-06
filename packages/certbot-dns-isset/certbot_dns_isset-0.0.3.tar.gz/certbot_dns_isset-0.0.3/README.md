# Isset Certbot plugin

## Running
```shell script
docker run --rm -it ubuntu
```

```shell script
apt update
apt install -y software-properties-common
add-apt-repository -y universe
add-apt-repository -y ppa:certbot/certbot
apt install -y certbot python3-pip
pip install -i https://test.pypi.org/simple/ certbot-dns-isset
```

Fill out isset.ini:
```shell script
certbot_dns_isset:dns_isset_endpoint="https://customer.isset.net/api"
certbot_dns_isset:dns_isset_token="nag_rich_for_token"
```

Fix credentials permissions:
```shell script
chmod 600 isset.ini
```

Dry-run
```shell script
certbot certonly --dry-run \
  -a certbot-dns-isset:dns-isset --certbot-dns-isset:dns-isset-credentials isset.ini \
  -m https@isset.nl --agree-tos \
  -d isset.cloud
```

Production (non-interactive)
```shell script
certbot certonly -n \
  -a certbot-dns-isset:dns-isset --certbot-dns-isset:dns-isset-credentials isset.ini \
  -m https@isset.nl --agree-tos \
  -d isset.cloud
```

# Releasing

1. Have `docker`
2. Have credentials for Test PyPi
3. `make all`
4. Fill out required prompted credentials
5. ???
6. PROFIT
