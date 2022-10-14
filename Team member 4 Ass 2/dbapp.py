import ibm_db

hostname="98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
uid="cdc82006"
pwd="69BUnKXXpXkk0XMY"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30875"
protocol="TCPIP"
cert="Certificate.crt"

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
