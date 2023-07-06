import time
import database
import news_scraper


def main():

    mydb = database.create_db_connection()
    mycursor = mydb.cursor()

    for i in range(55):
        articles = news_scraper.fetch_articles(i)
        for article in articles:
            title = article['headline']['main']
            link = article['web_url']
            print(f"Headline: {title}")
            print(f"Web URL: {link}\n")

            database.save_article(mycursor, title, link)
            mydb.commit()

        print(f"Current Page Number: {i}")
        time.sleep(12)


if __name__ == '__main__':
    main()
