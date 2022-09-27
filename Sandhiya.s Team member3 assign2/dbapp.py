import ibm_db

hostname="2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="qpw86742"
pwd="eWUeXsk2L9k3Y6Hn"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="32328"
protocol="TCPIP"
cert="DigiCertGlobalRootCA.crt"

dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
    ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to data base")
except:
    print("unable to connect",ibm_db.conn_errormsg())
 
