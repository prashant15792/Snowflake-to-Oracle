import re
class create_ora_obj:
    def create_sql(tuple):
        sql = 'INSERT INTO STG_TAB_COLS(table_name, column_name, column_position, column_length, data_type) VALUES'+str(tuple)
        sql = re.sub('None', 'NULL', sql)
        return sql

