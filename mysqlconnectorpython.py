class mysqlConPython ():
    import pymysql
    db = pymysql.connect('localhost','root','123456','gitdb')
    cursor = db.cursor()
    # cursor.execute('SELECT VERSION()') #查询数据库信息
    # data = cursor.fetchone()
    # print("Database version: %s" % data)
    # db.close()

    # sql = "INSERT INTO Users(username,passwd,lv) VALUES ('%s','%s','%d')" % ('XCup','123456',10) # 增加数据
    #
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except:
    #     db.rollback()
    #     print("error:mother fucker")
    # db.close()

    sql = "SELECT * FROM Users" #查询数据
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            username = row[0]
            passwd = row[1]
            lv = row[2]
            print("username=%s,passwd=%s,lv=%d" % (username,passwd,lv))
    except:
        print("error:unable to fetch data")
    db.close()

    # sql = "DELETE FROM Users" #删除数据
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except:
    #     db.rollback()
    # db.close()

# import mysql.connector #廖雪峰 mysql python 链接
# conn=mysql.connector.connect(user='root',password='123456',database='gitdb')
# cursor = conn.cursor()
# cursor.execute('insert into users (username,passwd,lv) values (%s,%s,%d)',['XCup','123456',10])