'''
1 - alcance, reproducciones de video, engagement, cantidad de seguidores, crecimiento.
2 - gráfico por red, uno con 3 redes.
3 - sentimiento de Hashtags, nube de palabras, porcentajes, tweets, volumen de tweets, datos demográficos.
4 - IG separar metricas por tipo de post
'''
from os import replace
import pyodbc
import pandas as pd
import datetime 
import json

server = 'localhost'
database = 'DB_T13'
user = 'sa'
passw = 'system'

connString = ''.join([
    'DRIVER={ODBC Driver 17 for SQL server}',
    ';SERVER=', server,
    ';DATABASE=', database,
    ';UID=', user,
    ';PWD=', passw
])


class Grafico_engagement_date():
    query = {
        'q1' : 
        """
            SELECT 
                p.id,
                p.post_date,
                p.post_message,
                p.engagements
            FROM Post p
            JOIN Network n  ON p.id_network = n.id
            WHERE 
                n.network_name = ?
                AND p.post_message NOT IN('none','')
            ORDER BY p.post_date;
        """
    }

    def get_data(self, network):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.query['q1'], network)
            result = cursor.fetchall()
            result = [list(x) for x in result]

            df = pd.DataFrame(result)
            df.columns = ['id', 'post_date', 'post_messsage', 'engagements']
            df['post_date'] = df['post_date'].map(lambda x : x.strftime("%Y/%m/%d %H:%M:%S"))
            #data = df.to_dict('records')
        
            df.to_csv('./media/grafoFacebook.csv', index=False)
            #df.to_csv('C:/Users/sebas/Downloads/grafoFacebook.csv', index=False)
        except Exception as e: print(e)
        finally:
            connection.close()
            #return data