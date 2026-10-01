#c3
import requests

url = "https://api.github.com/users/octocat/repos"
page = 1 
total = 0

while True:
    params = {"per_page":3,"page":page}
    response = requests.get(url, params=params)
    repos = response.json()

    if len(repos) == 0:
        break

    print("Page",page)
    for repo in repos:
        print(repo["name"])

    total = total + len(repos)
    page = page + 1

print("Total repos:", total)