from Oracle_Conn import ORA_CONNECTION as oc
from Create_Ora_objects import create_ora_obj as coo
from Connec_to_snowflake import connect_to_snowflake as ccs
import re
ccs.paramstyle='qmark'
conn = ccs.create_conn()
cur = conn.cursor()
cur_in = conn.cursor()
table_sql ='select table_name from information_schema.tables where table_schema={0}'
query = table_sql.format('\'TESTSCHEMA_MG\'')
cur.execute(query)
ora_con_obj = oc.con_obj("scott","tiger","localhost/orclpdbpm")
ora_obj_cur = ora_con_obj.cursor();
for record in cur:
    table_name = re.sub('[^A-Z a-z 0-9]*','',str(record))
    column_sql= 'select COLUMN_NAME, ORDINAL_POSITION, CHARACTER_MAXIMUM_LENGTH,data_type from information_schema.columns where table_name=\'{}\'';
    cur_in.execute(column_sql.format(str(table_name)))
    for rec in cur_in:
        col_list = (table_name,)+rec
        create_sql = coo.create_sql(col_list)
        print(create_sql)
        ora_obj_cur.execute(create_sql)
        ora_obj_cur.execute('COMMIT')