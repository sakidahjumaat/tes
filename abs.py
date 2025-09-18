import requests

url = "https://sedut.my"

headers = {
  'User-Agent': "OTT Navigator/1.7.3.2 (Linux;Android 14; en; 7jg7i0)",
  'Accept-Encoding': "gzip"
}

response = requests.get(url, headers=headers)

print(response.text)
