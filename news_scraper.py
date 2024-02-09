import requests
import time


# for i in range(55):
#     articles = news_scraper.fetch_articles(i)
#     for article in articles:
#         title = article['headline']['main']
#         link = article['web_url']
#         print(f"Headline: {title}")
#         print(f"Web URL: {link}\n")
#
#         database.save_article(mycursor, title, link)
#         mydb.commit()
#
#     print(f"Current Page Number: {i}")
#     time.sleep(12)
def fetch_articles(page_number):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    parameters = {
        'fq': 'headline:("Russia" "Ukraine") OR body:("Ukraine" AND "Russian" AND "War")',
        "api-key": "kiKKTKAOIaHxQdKfY8rtgrxTx0BRdXcO",
        "begin_date": "20230518",
        "end_date": "20230704",
        "page": page_number
    }

    response = requests.get(url, params=parameters)

    data = response.json()

    return data["response"]["docs"]
