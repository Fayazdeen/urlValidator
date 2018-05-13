import os
import pymysql

rds_host  = os.environ['RDS_HOST']
name = os.environ['USER_NAME']
password = os.environ['PASSWORD']
db_name =os.environ['DB_NAME']
port = int(os.environ['PORT'])
global conne
global category

def checkIfMaliciuos(category,hostname,URL_QS,conne):
    URL_QS_final= '/'+URL_QS
    print (category)
    if category == 'URL_based':
        cur=conne.cursor()
        print("hostname",hostname,"URL_QS_final",URL_QS_final)
        cur.execute("select * from HOSTNAME_Based_URLS where Host_Name=%s and Category =%s and QS_And_QP = %s",(str(hostname),str('Malicious'),str(URL_QS_final)))
        row = cur.fetchone()
        print(row)
        if row is None:
            return "The URL is safe to access"
        else:
            return "WARNING!!!The URL is NOT SAFE! Contains malicious content"
    elif category == 'IP_based':
        cur=conne.cursor()
        sql_query= "select Category from IP_Based_Hosts where Host_IP LIKE '%" + hostname[0:9] + "%'"
        print (sql_query)
        cur.execute(sql_query)
        row = cur.fetchone()
        if row is None:
            return "The URL is safe to access"
        else:
            Message =  "WARNING!!!The URL is NOT SAFE! Contains malicious content: As its WHOIS Content belongs to: " + row[0]
            return Message


def lambda_handler(event,context):
    try:
        conne = pymysql.connect(rds_host, user=name,passwd=password, db=db_name, connect_timeout=5)
    except Exception as e :
        return "SQL Connection Failed" + str(e.args[0])
    category=''
    QS=str(event["headers"]["original_path_and_qs"]).replace(", ","/")
    URL_QS=str(QS).replace("[","")
    URL_QS_final=URL_QS.replace("]","")
    hostname= str(event["params"]["hostname_and_port"])
    hostname_dot=hostname.split('.')
    print("Host",hostname_dot)
    try:
        if int(hostname_dot[0]):
            category ='IP_based'
    except Exception as message:
        print("Message",message)
        if str(message.args[0]).startswith("invalid literal for int() with base 10:"):
            category = 'URL_based' 
            
    malicious=checkIfMaliciuos(category,hostname,URL_QS_final,conne)
    Full_URL= hostname + '/' + URL_QS_final
    Respone={
        'URL':Full_URL,
        'Message': malicious
    }
    return Respone
    