import requests

url = "http://192.168.56.104"

try:
    response = requests.get(url, timeout=10)

    print("Target:", url)
    print("Status Code:", response.status_code)

    # Inspect cookies received in the response
    cookies = response.cookies

    if not cookies:
        print("\nNo cookies were set by this response.")

    else:
        print("\nCookie Security Analysis:")

        for cookie in cookies:
            print("\nCookie Name:", cookie.name)

            print("HttpOnly:", cookie.has_nonstandard_attr("HttpOnly"))
            print("Secure:", cookie.secure)

            same_site = cookie.get_nonstandard_attr("SameSite")
            print("SameSite:", same_site or "Not specified")

except requests.RequestException as e:
    print("Request failed:", e)

