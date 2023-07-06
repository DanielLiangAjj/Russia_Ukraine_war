import mysql.connector


def create_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
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
