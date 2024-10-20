
import requests

query_string = input("Enter the query string: ")
url = f"https://lccn.loc.gov/?q={query_string}" 
response = requests.get(url)
print(response.text)