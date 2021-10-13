from .models import *
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re, os

def parse_date(d):
    f = d.split(' ') # mm/ss/yyyy hh/mm/ss 'am'
    fecha_real = datetime.strptime(f[0] + ' ' + f[1], "%m/%d/%Y %H:%M")
    if(f[2] == "pm"): fecha_real -= timedelta(hours=12)
    return fecha_real
    
regex_url = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
strip_web = lambda x : re.sub(regex_url, '', str(x))
get_letters = lambda x : re.sub(r'[^A-Za-zÁ-Úá-ú]', ' ', str(x)).lower().translate(str.maketrans('áéíóúü','aeiouu'))
trim_spaces = lambda x : re.sub(r'\s\s+', ' ', x)
get_decimal = lambda x : float(re.sub(r'[^0-9.]', '', str(x))) / 100 if x is not None else x
get_number = lambda x : round(int(re.sub(r'[^0-9]', '', str(x)))) if x is not None else x
get_float  = lambda x : float(re.sub(r'[^0-9.]', '', str(x))) if x is not None else x


def cleanListeningInsights(data):
    df = pd.read_csv(data, low_memory = False)
    df['Date'] = df['Date'].map(parse_date)
    df['Message'] = df['Message'].map(strip_web)
    df['Message'] = df['Message'].map(get_letters)
    df['Message'] = df['Message'].map(trim_spaces)
    df['Network'] = df['Network'].map(str.lower)
    df = df.fillna(np.nan).replace([np.nan], [None])
    return df


def cleanPostPerformance(data):
    df = pd.read_csv(data, low_memory = False)
    df = df.fillna(np.nan).replace([np.nan], [None]) # Primer None: para poder procesar los datos
    df['Date'] = df['Date'].map(parse_date) 
    df['Network'] = df['Network'].map(str.lower)
    df['Post Type'] = df['Post Type'].map(str.lower)
    df['Content Type'] = df['Content Type'].map(str.lower)
    df['Post'] = df['Post'].map(strip_web)
    df['Post'] = df['Post'].map(get_letters)
    df['Post'] = df['Post'].map(trim_spaces)
    df['Engagement Rate (per Impression)'] = df['Engagement Rate (per Impression)'].map(get_decimal)
    df['Impressions'] = df['Impressions'].map(get_number)
    df['Organic Impressions'] = df['Organic Impressions'].map(get_number)
    df['Paid Impressions'] = df['Paid Impressions'].map(get_number)
    df['Reach'] = df['Reach'].map(get_number)
    df['Organic Reach'] = df['Organic Reach'].map(get_number)
    df['Paid Reach'] = df['Paid Reach'].map(get_number)
    df['Engagements'] = df['Engagements'].map(get_number)
    df['Reactions'] = df['Reactions'].map(get_number)
    df['Likes'] = df['Likes'].map(get_number)
    df['Love Reactions'] = df['Love Reactions'].map(get_number)
    df['Haha Reactions'] = df['Haha Reactions'].map(get_number)
    df['Wow Reactions'] = df['Wow Reactions'].map(get_number)
    df['Sad Reactions'] = df['Sad Reactions'].map(get_number)
    df['Angry Reactions'] = df['Angry Reactions'].map(get_number)
    df['Comments'] = df['Comments'].map(get_number)
    df['Shares'] = df['Shares'].map(get_number)
    df['Saves'] = df['Saves'].map(get_number)
    df['Post Link Clicks'] = df['Post Link Clicks'].map(get_number)
    df['Other Post Clicks'] = df['Other Post Clicks'].map(get_number)
    df['Post Clicks (All)'] = df['Post Clicks (All)'].map(get_number)
    df['Negative Feedback'] = df['Negative Feedback'].map(get_float)
    df['Video Views'] = df['Video Views'].map(get_number)
    df['Organic Video Views'] = df['Organic Video Views'].map(get_number)
    df['Paid Video Views'] = df['Paid Video Views'].map(get_number)
    df['Partial Video Views'] = df['Partial Video Views'].map(get_number)
    df['Organic Partial Video Views'] = df['Organic Partial Video Views'].map(get_number)
    df['Paid Partial Video Views'] = df['Paid Partial Video Views'].map(get_number)
    df['Full Video Views'] = df['Full Video Views'].map(get_number)
    df['Organic Full Video Views'] = df['Organic Full Video Views'].map(get_number)
    df['Paid Full Video Views'] = df['Paid Full Video Views'].map(get_number)
    df = df.fillna(np.nan).replace([np.nan], [None]) # segundo None: Para asegurarse de que no haya NaN
    return df

# Listening insights
def cargarData(df, file_type):
    try:
        if file_type == 'listeningInsights':
            for row in df.itertuples():

                # Ingresar Network
                if (row[2] is not None): print(Network().insert(network = row[2]))
                # Ingresar Usuario
                if (row[7] and row[8] is not None): print(UserProfile().insert(profile_name = row[7], followers = row[8]))
                # Ingresar Sentimento
                if (row[11] is not None): print(Sentiment().insert(sentiment = row[11]))
            
                # Ingresar Post
                if (row[2] is not None):
                    id_network = Network().get_id(network = row[2])
                    id_network = id_network[0]
                else: id_network = None

                if (row[7] is not None):
                    id_user = UserProfile().get_id(usuario = row[7])
                    id_user = id_user[0]
                else: id_user = None

                if (row[11] is not None):
                    id_sentiment = Sentiment().get_id(sentiment= row[11])
                    id_sentiment = id_sentiment[0]
                else: id_sentiment = None

                print(Post().insert(
                    data = [
                        row[1], # Date
                        row[3], # Message
                        row[4], # Message URL
                        row[5], # Message ID
                        row[9], # Shares
                        row[10], # Likes
                        None, None, None, None,
                        None, None, None, None,
                        None, None, None, None,
                        None, None, None, None,
                        None, None, None, None,
                        None, None, None, None,
                        None, None, None, None,
                        None, None,
                        id_network,
                        id_user,
                        id_sentiment,
                        None
                    ]))
                # Ingresar Hashtags
                if (row[13] is not None):
                    hashtags = [h for h in str(row[13]).split(', ')]
                    for h in hashtags: print(Hashtag().insert(hashtag = h))
                # Ingresar Post_Hastags
                if (row[5] is not None):
                    for h in hashtags: print(Post_Hashtags().insert(post = row[5], hashtag = h))

        elif file_type == 'postPerformance':
            for row in df.itertuples():
                
                # Ingresar Content Type
                if (row[5] is not None): print(ContentType().insert(content_type = row[5]))
                # Ingresar Network
                if (row[3] is not None): print(Network().insert(network = row[3]))
                # Ingresar Usuario
                if (row[6] is not None): print(UserProfile().insert(profile_name = row[6], followers = None))


                # Ingresar Post
                if (row[3] is not None):
                    id_network = Network().get_id(network = row[3])
                    id_network = id_network[0]
                else: id_network = None

                if (row[6] is not None):
                    id_user = UserProfile().get_id(usuario = row[6])
                    id_user = id_user[0]
                else: id_user = None

                if (row[5] is not None):
                    id_content_type = ContentType().get_id(content_type = row[5])
                    id_content_type = id_content_type[0]
                else: id_content_type = None
                
                print(Post().insert(
                    data = [
                        row[1], # Date
                        row[9], # Message
                        None, # Message URL
                        row[2], # Message ID
                        row[28], # Shares
                        row[21], # Likes
                        row[4], # Post Type
                        row[11], # Impressions 
                        row[12], # Organic impressions 
                        row[13], # Paid Impressions
                        row[14], # Reach 
                        row[15], # Organic Reach 
                        row[16], # Paid Reach 
                        row[18], # Engagement_Rate
                        row[19], # Engagements 
                        row[20], # Reactions 
                        row[22], # Love Reactions 
                        row[23], # Haha reactions
                        row[24], # Wow Reactions
                        row[25], # Sad reactions
                        row[26], # Angry Reactions
                        row[27], # Comments
                        row[29], # Saves
                        row[30], # Post link clicks
                        row[31], # other post clicks
                        row[32], # post click all
                        row[34], # negative feedback
                        row[35], # video views
                        row[36], # organic video views
                        row[37], # paid video views
                        row[38], # partial video views
                        row[39], # organic partial video views
                        row[40], # paid partial video views
                        row[41], # full video views
                        row[42], # organic full video views
                        row[43], # paid full video views
                        id_network,
                        id_user,
                        None,
                        id_content_type
                    ]))

    except Exception as e: print(e)
    finally: print('Listo!')

# Post Performance


# Rating

# Entidades