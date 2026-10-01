#c1
import requests

url = "https://api.github.com/users/RaffertyChen/repos"
response = requests.get(url)
print(response.status_code)

repos = response.json()

for repo in repos:
    print(repo["name"])