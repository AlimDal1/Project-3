import requests
import pandas as pd

def fetch_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    return pd.DataFrame(data)
