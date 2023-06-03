import netifaces
import requests

gateways = netifaces.gateways()

default_gateway: str = gateways['default'][2][0]
print(requests.get(f'http://{default_gateway}/').text)
print(default_gateway)
