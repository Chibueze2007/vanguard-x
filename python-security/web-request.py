import requests
urls =["http://192.168.56.104","http://192.168.56.104:8180"]
apps = ["DVWA","phpMyAdmin","TWiki","Mutillidae"]
for url in urls:
    response = requests.get(url)
    print("URL:", url)
    print("Status Code:", response.status_code)
    for app in apps:
        if app in response.text:
            print(f"{app} detected in {url}")
