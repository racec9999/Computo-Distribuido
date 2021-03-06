"""
License Attribution-NonCommercial 4.0 International
Contact:
    César Arcos Gonzalez: racec9999@gmail.com
    Saul Armas Gamiño: luasikirfl@gmail.com
"""
import datetime
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
from datetime import datetime
import ntpath

def insertar(data_query):
    try:
        cnx=mysql.connector.connect(**config)
        cursor=cnx.cursor()
        query=("INSERT INTO tipo_cambio_tweets(date,tweet,dollar) VALUES(%s,%s,%s) ")
        cursor.execute(query,data_query)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("algo esta mal con tu usuario o contrasena")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == "__main__":

    with open(path+'/config/'+'db.json') as json_file:
        config=json.load(json_file)
    
    for filename in glob.glob(path+"*.json"):
        print(filename)
        real_file = ntpath.basename(filename)  #filename[18:]
        with open(filename,'r') as f:
            datos=json.load(f)
        date= datos['date']
        tweets=datos['tweet']
        dolar=datos['dollar']
        data_query=(date,tweets,dolar)
        insertar(data_query)
    
