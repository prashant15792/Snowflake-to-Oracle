#pip install oracledb
import oracledb
class ORA_CONNECTION:
    def con_obj(pi_user, pi_password, pi_tns):
        con = oracledb.connect(user="scott", password="tiger",  dsn="localhost/orclpdbpm")
        return con
