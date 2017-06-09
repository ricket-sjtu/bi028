import requests

print requests.get("http://example.com").text[:65] + " ..."

print requests.get("https://www.googleapis.com/books/v1/volumes", params={"q":"machine learning"}).json()['items'][0]