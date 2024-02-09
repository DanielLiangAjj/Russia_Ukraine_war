import mysql.connector


def create_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1",
        database="Russian_Ukraine_war",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )

    return mydb


def save_article(mycursor, title, link):
    sql = "SELECT * FROM articles WHERE link = %s"
    val = (link,)
    mycursor.execute(sql, val)

    result = mycursor.fetchall()

    if not result:
        sql = "INSERT INTO articles (title, link) VALUES (%s, %s)"
        val = (title, link)
        mycursor.execute(sql, val)

def pull_article(mycursor, id):
    sql = "SELECT * FROM articles WHERE id = %s AND category = %s"
    val = (id, 'news')
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    return result

def dataset_length(mycursor):
    sql = "SELECT COUNT(*) FROM articles"
    mycursor.execute(sql)
    return mycursor.fetchall()

def update_russia_score(mycursor, id, score):
    sql = "UPDATE articles SET Russia_score = %s WHERE id = %s"
    val = (score, id)
    mycursor.execute(sql, val)

def update_ukraine_score(mycursor, id, score):
    sql = "UPDATE articles SET Ukraine_score = %s WHERE id = %s"
    val = (score, id)
    mycursor.execute(sql, val)

def update_article_content(mycursor, id, content):
    sql = "UPDATE articles SET content = %s WHERE id = %s"
    val = (content, id)
    mycursor.execute(sql, val)