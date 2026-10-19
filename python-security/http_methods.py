import requests

url = "http://192.168.56.104"

# Test GET
get_response = requests.get(url, timeout=10)

print("\nGET Request")
print("Status:", get_response.status_code)
print("Response body length:", len(get_response.content))

# Test HEAD
head_response = requests.head(url, timeout=10)

print("\nHEAD Request")
print("Status:", head_response.status_code)
print("Response body length:", len(head_response.content))
