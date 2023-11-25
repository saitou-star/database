import pymysql.cursors


# データベースに接続
def connect():

    connection = pymysql.connect(
        host="localhost", # MNMPの時はlocalhost
        user="root",      # user,password はMANPは初期設定はroot
        password="root",  # 上と同じ
        database="pybase",  # SQLに作ったファイル名、データを取りたいファイル名
        cursorclass=pymysql.cursors.DictCursor  # どういう形式で受け取るかを指定
    )
    return connection



# SELECT文でレコード全件取得
def find_all():
    result = None
    with connect() as con:
        with con.cursor() as cursor:  # ここと上の２行は定型文,conの中にはconnect()の戻り値が入る
            sql = "SELECT * FROM ranking"  # 取得時に数値の高い順などの条件付けれる。rankingの後にORDER BY score DESC
            cursor.execute(sql)  # execute関数でレコードを１行ずつ取得
            result = cursor.fetchall()  # 上の１行ずつ取得したデータを複数行でリスト形式で処理
    return result  # 定義にNoneが入っているため、数値が無ければNoneが入る



def insert_one(user):
    with connect() as con:
        with con.cursor() as cursor:  # 定型文
            sql = "INSERT INTO ranking(name,score) VALUES(%s,%s)" # %sはフォーマット関数（仮置き）＝後から数値を入れる
            cursor.execute(sql,(user["name"],user["score"]))  # 第２引数の（）はタプル、このデータ（def部分でもらった引数）をSQLに実行して、という内容
            # 上記のexecute関数（指定した関数などを実行する）で第一引数のsql(一個上の)の中身を実行する。
        
        con.commit()  # データ変更を行ったら定型的に、コミットメソッドを使い、変更を承認する（必ず）



