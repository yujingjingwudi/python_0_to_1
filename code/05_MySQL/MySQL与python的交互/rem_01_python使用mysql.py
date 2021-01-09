 from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='127.0.0.1',port=3306,user='root',password='19970806',database='jing_dong',charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def showMenu():
        print("1. 查看所有商品")
        print("2. 查看所有商品类别")
        print("3. 查看所有商品品牌")
        print("4. 增加一个新的商品品牌")
        return input("请输入你的选择")


    def run(self):
        while True:
            answ = self.showMenu()
            if answ == '1':
                self.showAll()
            if answ == '2':
                self.showCate()
            if answ == '3':
                self.showBland()
            if answ == '4':
                self.addNewBrand(input("请输入你要添加的品牌"))

    def showAll(self):
        sql = "select * from goods"
        self.execsql(sql)

    def showCate(self):
        sql = "select * from goods_cates"
        self.execsql(sql)

    def showBland(self):
        sql = "select * from goods_brands"
        self.execsql(sql)

    def addNewBrand(self,new_brand):
        sql = "insert into goods_brands (name) values ('%s')" % new_brand
        self.cursor.execute(sql)
        self.conn.commit()

    def execsql(self,sql):
        self.cursor.execute(sql)
        mes = self.cursor.fetchall()
        for i in mes:
            print(i)


def main():
    jd = JD()
    jd.run()



if __name__ == "__main__":
    main()