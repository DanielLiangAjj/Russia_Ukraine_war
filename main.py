import time
import database
import news_scraper
import newsplease
from newsplease import NewsPlease
from newspaper import Article
from bs4 import BeautifulSoup
import requests

import os
import openai




def gpt_paraphrase(text):


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant with article paraphrasing."},
            {"role": "user", "content": "Please paraphrase the following news article: \n" + text},
        ]
    )

    print(response['choices'][0]['message']['content'])


# Load pre-trained model and tokenizer
# model = BertModel.from_pretrained('bert-base-uncased')
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')



def main():
    mydb = database.create_db_connection()
    mycursor = mydb.cursor()
    database_length = database.dataset_length(mycursor)[0][0]
    for i in range(8238, -1, -1): #201 #8198
        try:
            curr_article = database.pull_article(mycursor,i)
            print(curr_article)
            title = curr_article[0][1]
            link = curr_article[0][2]
            article = NewsPlease.from_url(link)
            print(title)
            print(article.maintext)
            database.update_article_content(mycursor, i, article.maintext)
            russia_score = int(input("The score for Russia: "))
            database.update_russia_score(mycursor, i, russia_score)
            ukraine_score = int(input("The score for Ukraine: "))
            database.update_ukraine_score(mycursor, i, ukraine_score)
            mydb.commit()
            print(f"Successfully Recorded, current article id: {i}")
        except:
            continue



if __name__ == '__main__':
    main()
    # mydb = database.create_db_connection()
    # mycursor = mydb.cursor()
    # curr_article = database.pull_article(mycursor, 1)
    # title = curr_article[0][1]
    # content = curr_article[0][3]
    # text = 'News title: ' + title + '\n'+ 'Content: ' + content
    # gpt_paraphrase(text)