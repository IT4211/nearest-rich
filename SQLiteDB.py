import sqlite3

class sqlite_db:

    def __init__(self, path):
        self.path = path

    def create_sqlite(self):
        con = sqlite3.connect(self.path)  # database create
        con.text_factory = str()
        cursor = con.cursor()

        sql = "CREATE TABLE IF NOT EXISTS richdrs(" \
              "Filename text, " \
              "Filepath text, " \
              "Hash(MD5) text, " \
              "Hash(SHA1) text, " \
              "mCV text, " \
              "Count int, " \
              "ProdID text)"
        cursor.execute(sql)

    def ins_sqlite(self, fname, fpath, md5, sha1, compids):
        con = sqlite3.connect(self.path)
        con.text_factory = str()
        cursor = con.cursor()

        mCV = compids['mcv']
        Count = compids['cnt']
        ProdID = compids['pid']

        cursor.execute("INSERT INTO richdrs VALUES(?, ?, ?, ?, ?, ?, ?)",
                       (fname, fpath, md5, sha1, mCV, Count, ProdID))
        con.commit()
        con.close()