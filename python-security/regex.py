import requests
import re
urls = ["http://192.168.56.104", 
        "http://192.168.56.104:8180"]
security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]
get_response = requests.get(urls,timeout = 10)
print("\nGET REQUEST")
print("Status:", get_response.status_code)
print("Response body length: ",len(get_response.content))
# Test HEAD
head_response = requests.head(url, timeout=10)

print("\nHEAD Request")
print("Status:", head_response.status_code)
print("Response body length:", len(head_response.content))
for url in urls:
    try:
        response = requests.get(url,timeout=10)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        continue
    print("Status Code:", response.status_code)
    print("Web Server:",response.headers.get("Server","Not disclosed"))
    print("ALl Response Headers: ", response.headers)
    result = re.search(r'<title>(.*?)</title>', response.text,re.IGNORECASE)
    if result:
        print("Page Title:", result.group(1))
    else:
        print("Page Title: Not found")
    print("\nSecurity Headers:")
    for header in security_headers:
        if header in response.headers:
            print(f"[PRESENT] {header}: {response.headers[header]}")
        else:
            print(f"[MISSING] {header}")
