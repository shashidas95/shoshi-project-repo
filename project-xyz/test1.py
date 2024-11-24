import requests

# from https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28 
# /repos/{owner}/{repo}/pulls 
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details = response.json()
for i in range(len(details)):
 print(details[i]["user"]["login"])