import requests


with open('L.txt', 'r+') as ip_file:
    stored_ip = ip_file.read()
    new_ip = requests.get('https://ipinfo.io/json').json()['ip']

    if new_ip == stored_ip:
        print(stored_ip)
    else:
        ip_file.seek(0)
        ip_file.truncate(0)
        ip_file.write(new_ip)
