import requests
import time


def fetch_articles(page_number):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    parameters = {
        'fq': 'headline:("Russia" "Ukraine") OR body:("Ukraine" AND "Russian" AND "War")',
        "api-key": "YOUR_API_KEY",
        "begin_date": "20230518",
        "end_date": "20230704",
        "page": page_number
    }

    response = requests.get(url, params=parameters)

    data = response.json()

    return data["response"]["docs"]
