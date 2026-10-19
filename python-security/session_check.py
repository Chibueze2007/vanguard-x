import requests

url = "http://192.168.56.104"

# Create a session
session = requests.Session()

try:
    print("First Request")

    response1 = session.get(url, timeout=10)

    print("Status Code:", response1.status_code)
    print("Cookies Stored:", session.cookies.get_dict())

    print("\nSecond Request")

    response2 = session.get(url, timeout=10)

    print("Status Code:", response2.status_code)
    print("Cookies Stored:", session.cookies.get_dict())

except requests.RequestException as e:
    print("Request failed:", e)

finally:
    session.close()
