from django.db import models
import pyodbc
# Create your models here.


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

class Network:
    queries = {
        'insert'        : 'INSERT INTO Network VALUES(?)',
        'read_all'      : 'SELECT * FROM Network',
        'read_by_name'  : 'SELECT * FROM Network n WHERE n.network_name = ?',
        'get_id'        : 'SELECT n.Id FROM Network n WHERE n.network_name = ?'
    }
    def get_id(self, network):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['get_id'], network)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_network.get_id) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_network.read_all) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def read(self, network):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_by_name'], network)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_network.read_by_name) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, network):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que la network no exista aún
            cursor.execute(self.queries['read_by_name'], network)
            exists = cursor.fetchone()

            if not exists:
                cursor.execute(self.queries['insert'], network)
                message = '(dao_network.insert) >>> network \"{0}\" insertada.'.format(network)
            else:
                message = '(dao_network.insert) >>> network \"{0}\" ya existe'.format(network)

        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()

        finally: 
            connection.autocommit = True
            connection.close()
            return message

class ContentType:
    queries = {
        'read_all'      : 'SELECT * FROM ContentType',
        'read_by_name'  : 'SELECT * FROM ContentType WHERE content_type = ?',
        'insert'        : 'INSERT INTO ContentType VALUES(?)',
        'get_id'        : 'SELECT c.id FROM ContentType c WHERE c.content_type = ? '
    }

    def get_id(self, content_type):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['get_id'], content_type)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_contentType.get_id) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_contentType.read_all) >>> No se encontraron valores.')

        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, content_type):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_name'], content_type)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_contentType.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, content_type):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_name'], content_type)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], content_type)
                message = '(dao_contentType.insert) >>> content_type \"{0}\" insertado.'.format(content_type)
            else:
                message = '(dao_contentType.insert) >>> content_type \"{0}\" ya existe.'.format(content_type)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Hashtag:
    queries = {
        'read_all'      : 'SELECT * FROM Hashtag',
        'read_by_name'  : 'SELECT * FROM Hashtag WHERE hashtag = ?',
        'insert'        : 'INSERT INTO Hashtag VALUES(?)'
    }

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_hashtag.read_all) >>> No se encontraron valores.')

        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, hashtag):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_name'], hashtag)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_hashtag.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, hashtag):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_name'], hashtag)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], hashtag)
                message = '(dao_hashtag.insert) >>> hashtag \"{0}\" insertado.'.format(hashtag)
            else:
                message = '(dao_hashtag.insert) >>> hashtag \"{0}\" ya existe.'.format(hashtag)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Entity:
    queries = {
        'read_all'      : 'SELECT * FROM Entity',
        'read_by_name'  : 'SELECT * FROM Entity WHERE ent_name = ?',
        'insert'        : 'INSERT INTO Entity VALUES(?)'
    }

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_entity.read_all) >>> No se encontraron valores.')

        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, entity):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_name'], entity)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_entity.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, entity):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_name'], entity)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], entity)
                message = '(dao_entity.insert) >>> entidad \"{0}\" insertada.'.format(entity)
            else:
                message = '(dao_entity.insert) >>> entidad \"{0}\" ya existe.'.format(entity)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Rating:
    queries = {
        'read_all'      : 'SELECT * FROM Rating',
        'read_by_date'  : 'SELECT * FROM Rating r WHERE r.rating_date = ?',
        'insert'        : 'INSERT INTO Rating VALUES(?,?)'
    }

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_rating.read_all) >>> No se encontraron valores.')
            result = [(x[0], str(x[1]), x[2]) for x in result]
        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, rating_date):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_date'], rating_date)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_rating.read_by_date) >>> No se encontraron valores')
            result = (result[0], str(result[1]), result[2])
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, rating_date, points):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_date'], rating_date)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], rating_date, points)
                message = '(dao_rating.insert) >>> rating \"{0} ~ {1}\" insertado.'.format(rating_date, points)
            else:
                message = '(dao_rating.insert) >>> rating \"{0} ~ {1}\" ya existe.'.format(rating_date, points)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Sentiment:
    queries = {
        'read_all'      : 'SELECT * FROM Sentiment',
        'read_by_name'  : 'SELECT * FROM Sentiment s WHERE sentiment = ?',
        'insert'        : 'INSERT INTO Sentiment VALUES(?)',
        'get_id'        : 'SELECT s.id FROM Sentiment s WHERE s.sentiment = ?'
    }

    def get_id(self, sentiment):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['get_id'], sentiment)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_sentiment.get_id) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_sentiment.read_all) >>> No se encontraron valores.')

        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, sentiment):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_name'], sentiment)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_sentiment.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, sentiment):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_name'], sentiment)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], sentiment)
                message = '(dao_sentiment.insert) >>> sentimento \"{0}\" insertado.'.format(sentiment)
            else:
                message = '(dao_sentiment.insert) >>> sentimento \"{0}\" ya existe.'.format(sentiment)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class UserProfile:
    queries = {
        'read_all'      : 'SELECT * FROM UserProfile',
        'read_by_name'  : 'SELECT * FROM UserProfile WHERE profile_name = ?',
        'insert'        : 'INSERT INTO UserProfile VALUES(?,?)',
        'get_id'        : 'SELECT u.id FROM UserProfile u WHERE u.profile_name = ? '
    }

    def get_id(self, usuario):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['get_id'], usuario)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_user_profile.get_id) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_userProfile.read_all) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, profile_name):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_name'], profile_name)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_userProfile.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, profile_name, followers):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            # Chequear que no exista aún
            cursor.execute(self.queries['read_by_name'], profile_name)
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(self.queries['insert'], profile_name, followers)
                message = '(dao_userProfile.insert) >>> usuario \"{0} ~ {1}\" insertado.'.format(profile_name, followers)
            else:
                message = '(dao_userProfile.insert) >>> usuario \"{0} ~ {1}\" ya existe.'.format(profile_name, followers)
        except pyodbc.DatabaseError:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Post:
    queries = {
        'read_all'      : 'SELECT * FROM Post',
        'read_by_id_message'  : 'SELECT * FROM Post WHERE id_message = ?',
        'insert'        : 'INSERT INTO Post VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    }



    def read_all(self):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()

            cursor.execute(self.queries['read_all'])
            result = cursor.fetchall()
            if not result: raise Exception('(dao_userProfile.read_all) >>> No se encontraron valores.')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result
            
    def read(self, id_message):
        try:
            result = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            
            cursor.execute(self.queries['read_by_id_message'], id_message)
            result = cursor.fetchone()
            if not result: raise Exception('(dao_Post.read_by_name) >>> No se encontraron valores')
        except Exception as e: print(e)
        finally:
            connection.close()
            return result

    def insert(self, data):
        try:
            message = None
            connection = pyodbc.connect(connString)
            cursor = connection.cursor()
            cursor.execute(self.queries['insert'], [d for d in data])
            message = '(dao_Post.insert) >>> Post \"{0}\" insertado.'.format(data[3])
            '''
            # Chequear que no exista aún
            exists = self.read(id_message)
            if not exists:
                cursor.execute(self.queries['insert'], data)
                message = '(dao_Post.insert) >>> Post \"{0}\" insertado.'.format(id_message)
            else:
                message = '(dao_Post.insert) >>> Post \"{0}\" ya existe.'.format(id_message)
            '''
        except pyodbc.DatabaseError as err:
            connection.rollback()
            message = err
        else:
            connection.commit()
        finally:
            connection.autocommit = True
            connection.close()
            return message

class Post_Hashtags:
    queries = {
        'insert' : 'INSERT INTO Post_Hashtags VALUES(?,?)', # id_post, id_hashtag
        'get_id_post' : 'SELECT p.id FROM Post p WHERE p.id_message = ?',
        'get_id_hashtag' : 'SELECT h.id FROM Hashtag h WHERE h.hashtag = ?' 

    }

    def insert(self, post, hashtag): 
        try:
            message = None
            conn = pyodbc.connect(connString)
            cur = conn.cursor()

            # Obtener el id del token 
            id_post = cur.execute(self.queries['get_id_post'], post).fetchone()
            id_hashtag = cur.execute(self.queries['get_id_hashtag'], hashtag).fetchone()
            id_post, id_hashtag = id_post[0], id_hashtag[0] # sacar el valor de dentro del cursor
            if id_post and id_hashtag:
                cur.execute(self.queries['insert'], id_post, id_hashtag)
                message = '(dao_post_hashtags.insert) >>> Registro \"{0} ~ {1}\" insertado.'.format(id_post, id_hashtag)
            else:
                message = '(dao_post_hashtags.insert) >>> Datos faltantes para la inserción. ({0}, {1})'.format(id_post, id_hashtag)
        except pyodbc.DatabaseError as err:
            conn.rollback() 
            message = err
        else:
            conn.commit()

        finally: 
            conn.autocommit = True
            conn.close()
            return message
