import os
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

print(response)
