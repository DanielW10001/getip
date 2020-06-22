import requests


class APIError(RuntimeError):
    pass


try:
    response_json = requests.get(
        'http://ip-api.com/json/?fields=status,query',
        proxies={'http': 'socks5://HOST:PORT'}).json()
    if response_json['status'] != 'success':
        raise APIError(f'status: {response_json["status"]}')
    ip = response_json['query']
except requests.exceptions.ConnectionError:
    pass
except requests.exceptions.HTTPError:
    pass
except ValueError:
    pass
except KeyError:
    pass
else:
    print(ip)
