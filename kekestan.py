import requests
login = input()
password = input()
r = requests.get('https://api.github.com/user', auth=(login, password))
print(r.status_code)
print(r.json())