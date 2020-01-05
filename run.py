from urllib.request import urlopen
with urlopen("http://www.google.com") as response:
  response_content = response.read()

print(response_content)
