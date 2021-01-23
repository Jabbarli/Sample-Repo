import requests

r = requests.get("https://www.google.ca/")
print(r.status_code)
print(r.ok)
