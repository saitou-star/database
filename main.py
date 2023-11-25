import dao

# 下部２行を使うと、dao.pyのdao.insert_one(user)関数が実行され、SQLにuserの情報が新規登録される
user = {"name":"リック", "score":85}  # ディクショナリ（左がキー、右が値）
dao.insert_one(user)  # dao.pyの関数呼び出し（登録）


# 下の２行でデータをリスト形式で中身は各データがタプルで取得。したい時に使う。
result = dao.find_all()
print(result)  # 全件取得
print(result[0]["name"])  # resultの0番目の名前データを取得。取りたい部分を指定して取得する方法.
# リスト型で取得されるので、添え字指定で指示できる



