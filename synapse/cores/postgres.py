from . import sqlite as s_c_sqlite

istable = '''
   SELECT 1
   FROM   information_schema.tables 
   WHERE    table_name = %s
'''

class Cortex(s_c_sqlite.Cortex):

    dbvar = '%s'

    def _initDataBase(self, dbinfo):
        import psycopg2
        db = psycopg2.connect(**dbinfo)
        c = db.cursor()
        c.execute('SET enable_seqscan=false')
        c.close()
        return db

    def _initCorQueries(self):
        s_c_sqlite.Cortex._initCorQueries(self)
        self._q_istable = istable

    def _initDbInfo(self, link):
        return {
            'host':link[1].get('host'),
            'user':link[1].get('user'),
            'port':link[1].get('port'),
            'passwd':link[1].get('passwd'),
            'database':link[1].get('path')[1:],
        }

