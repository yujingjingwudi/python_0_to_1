from pymysql import connect

print(__name__)

def main():
    conn = connect(host='127.0.0.1', port=3306, user='root', password='19970806', database='jing_dong', charset='utf8')
    cursor = conn.cursor()
    print("nihao")

    for i in range(100000):
        sql = "insert into test_index values ('haha-%d')" % i
        cursor.execute(sql)

    conn.commit()
    print("已经提交")
    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()
