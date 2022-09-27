import ibm_db

hostname="ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid="wml88404"
pwd="ijU9BXVkMdpwN5bL"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="31321"
protocol="TCPIP"
cert="certificate.crt"

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
    print("Connected to data base")
except:
    print("Unable to connect",ibm_db.conn_errormsg())
