import requests
from datetime import datetime

url = input()
#url = "https://www.youtube.com/watch?v=GtL1huin9EE"

with requests.get(url) as response:

    html = response.text

    if response.headers.get("Server") is not None:
        print("\nWeb Server: " + response.headers.get("Server"))
    else:
        print("\nWeb Server: No web server found")

    print("\nCookies: ")
    for cookie in response.cookies:
        if cookie.expires is not None:
            print("\tName: " + cookie.name)
            print("\tExpiration date: " + str(datetime.fromtimestamp(int(cookie.expires))))
        else:
            print("\tName: " + cookie.name)
            print("\tExpiration date: No expiration date found")
