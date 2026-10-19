
import requests

url = "http://192.168.56.104"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    print("\nCookies received:")

    if response.cookies:
        for cookie in response.cookies:
            print("Cookie Name:", cookie.name)
            print("Cookie Value:", cookie.value)
    else:
        print("No cookies were set in this response.")

    print("\nSet-Cookie Header:")
    print(response.headers.get("Set-Cookie", "Not provided"))

except requests.RequestException as e:
    print("Request failed:", e)
