import requests

url = "http://192.168.56.104"

methods = ["GET", "HEAD", "OPTIONS", "POST"]

for method in methods:
    print(f"\nTesting {method}...")

    try:
        response = requests.request(
            method,
            url,
            timeout=10
        )

        print("Status Code:", response.status_code)
        print("Response Body Length:", len(response.content))
        print("Allow Header:", response.headers.get("Allow", "Not provided"))

    except requests.RequestException as e:
        print(f"Request failed: {e}")
