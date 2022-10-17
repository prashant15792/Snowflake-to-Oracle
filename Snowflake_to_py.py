#pip install "snowflake-connector-python[pandas]"
import snowflake.connector
from Oracle_Conn import ORA_CONNECTION as oc
snowflake.connector.paramstyle='qmark'
conn = snowflake.connector.connect(
    user='PRASHANT150792', ##USER NAME THAT YOU SET DURING SIGNUP
    password='Pr@shant15792', ##USER PASSWORD
    account='CC07134.ap-southeast-1', ##ACCOUNT ID- CAN BE EXTRACTED FROM ACCOUNT URL
    warehouse = 'tiny_warehouse_mg',
    database = 'testdb_mg',
    schema = 'testschema_mg',
    ROLE= 'ACCOUNTADMIN'
)
cur = conn.cursor()
cur_in = conn.cursor()
table_sql ='select table_name from information_schema.tables where table_schema=?'
cur.execute(table_sql, ['TESTSCHEMA_MG'])
for record in cur:
#   print(record)
   column_sql= 'select COLUMN_NAME, ORDINAL_POSITION, data_type, CHARACTER_MAXIMUM_LENGTH from information_schema.columns where table_name=?';
   cur_in.execute(column_sql, record)
   for rec in cur_in:
       print(record+rec)
ora_con_obj = oc.con_obj("scott","tiger","localhost/orclpdbpm")
sql = """select sysdate from dual"""
for r in ora_con_obj.cursor().execute(sql):
    print(r)