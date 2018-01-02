import psycopg2

class Model():
    def __init__(self):
        self.conn = psycopg2.connect("dbname='gplay' user='postgres' host='localhost' password='Matkhaula123'")

    def getAppId(self,first,last):
        query = ' LIMIT ' + str(first) + ' OFFSET ' + str(last)
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT app_id from apps" + query)
        except:
            print "I can't SELECT from apps"
        rows = cur.fetchall()
        listAppId = []
        for row in rows:
            listAppId.append(str(row[0]))
        return listAppId
