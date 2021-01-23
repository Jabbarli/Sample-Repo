import sys
import requests

print(sys.executable)
print(sys.version)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


r = requests.get("https://www.google.ca/")
print(r.status_code)
