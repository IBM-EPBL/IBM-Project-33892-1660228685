import ibm_db

hostname="824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="cqs76416"
pwd="gJOvhu4Jy0eEmfOo"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30119"
protocol="TCPIP"
cert="certificate,crt"

dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5}"
    ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to data base")
except:
    print("unable to connect",ibm_db.conn_errormsg())

    
