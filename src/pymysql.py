import MySQLdb
import pandas as pd

##　MySQLへの接続を行う関数
def getConnect():
    conn = MySQLdb.connect(
        host = '192.168.33.10',
        user = 'natsu',
        database = 'test',
        charset = 'utf8'
    )
    return conn

## データをMySQLへ追加する関数
# input : dataset -> タプル型の一組のデータセット
def updataDB(conn, dataset):
    # dataset [type:tuple]
    c = conn.cursor()
    conn.commit()

    # MySQLのテーブルの名前
    table = 'backcountry_db'
    # 重複を確認するために用いる項目
    column = 'productNumber'
    # productNumberの値
    target = dataset[2]

    # 重複を確認するコマンド (productNumberの値が重複しているか確認)
    cmd_match = "SELECT * FROM %s WHERE %s LIKE '%s'" %(table, column, target)
    #print(cmd_match)
    flag = c.execute(cmd_match)
    res = c.fetchall()

    # 重複がなかった場合はflag = 0
    # 重複がなかった場合は新規でデータを追加
    # 重複があった場合はstockの値だけ更新（それ以外の項目は変化なし）
    if(flag == 0):
        cmd_insert = "insert into backcountry_db values ('%s', '%s', '%s', '%s', '%s')" %(dataset)
        #print(cmd_insert)
        c.execute(cmd_insert)
        print("New Data [INSERT]\n")
    else:
        cmd_update = "update %s set stock = '%s' where productNumber = '%s'" %(table, dataset[-1], target)
        #print(cmd_update)
        c.execute(cmd_update)
        print("Existing [UPDATE]\n")

    conn.commit()
    return conn

if __name__ == '__main__':
    conn = getConnect()

    # TestData [id, name, productNumber, price, stock]
    # 日本語は未対応なので英数字のみ
    datas = [
        (1, 'murakami', '#6145', '1000yen', '2'),
        (2, 'kamimoto', '#6146', '1200yen', '0'),
        (3, 'midoriya', '#6147', '1500yen', '2'),
        (4, 'uraraka', '#6148', '2000yen', '0'),
        (5, 'kinoshita', '#6149', '2400yen', '0'),
        (6, 'yamashita', '#6150', '1800yen', '5')
    ]

    for d in datas:
        print(d)
        conn = updataDB(conn, d)

    conn.close()
