#pip install "snowflake-connector-python[pandas]"
import snowflake.connector
class connect_to_snowflake:
    def create_conn():
         conn = snowflake.connector.connect(
         user='PRASHANT150792', ##USER NAME THAT YOU SET DURING SIGNUP
         password='Pr@shant15792', ##USER PASSWORD
         account='CC07134.ap-southeast-1', ##ACCOUNT ID- CAN BE EXTRACTED FROM ACCOUNT URL
         warehouse = 'tiny_warehouse_mg',
         database = 'testdb_mg',
         schema = 'testschema_mg',
         ROLE= 'ACCOUNTADMIN')
         return conn