import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    for item in soup.find_all("h2"):
        data.append({"title": item.text})

    return pd.DataFrame(data)
