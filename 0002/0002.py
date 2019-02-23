# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import random
import string
import mysql.connector


forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        # print(Re)
        yield Re


def save_code():
    connect = mysql.connector.connect(user='****', password='******', database='test1')
    # print('It works!')
    cursor = connect.cursor()

    codes = generate_code(200, 10)

    for code in codes:
        cursor.execute("INSERT INTO code (code) VALUES(%s)", params=[code])

    connect.commit()
    cursor.close()


if __name__ == '__main__':
    save_code()
