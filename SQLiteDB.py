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
              "MD5 text, " \
              "SHA1 text, " \
              "mCV text, " \
              "Count text, " \
              "ProdID text)"
        cursor.execute(sql)

    def insert_sqlite(self, fname, fpath, md5, sha1, mcv, cnt, pid):
        con = sqlite3.connect(self.path)
        con.text_factory = str()
        cursor = con.cursor()

        cursor.execute("INSERT INTO richdrs VALUES(?,?,?,?,?,?,?)",
                       (str(unicode(fname).encode('utf8')), str(unicode(fpath).encode('utf8')), md5, sha1, str(mcv), str(cnt), str(pid)))
        con.commit()
        con.close()