import psycopg2
import os
import json

configs={
    'host':os.getenv('DB_HOST'),
    'database':os.getenv('DB_NAME'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD')
}


def make_table():
    conn=psycopg2.connect(**configs)
    cur=conn.cursor()
    query= """

    CREATE TABLE IF NOT EXISTS ka_series (
        id  BIGSERIAL  PRIMARY KEY,
        serie  VARCHAR(100)  NOT NULL  UNIQUE,
        seasons INTEGER  NOT NULL,
        released_date  DATE  NOT NULL,
        genre  VARCHAR(50)  NOT NULL,
        imdb_rating  FLOAT  NOT NULL       
    );
    """
    
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()



class Series:

    def __init__(self,**kwargs):
        self.serie = kwargs['serie']
        self.seasons = kwargs['seasons'] 
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre']
        self.imdb_rating = kwargs['imdb_rating']



    @staticmethod
    def series():
        conn=psycopg2.connect(**configs)
        cur=conn.cursor()
        query= "SELECT * FROM ka_series;"

        cur.execute(query)

        series = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()


        return series
    

    def select_by_id(id):
        conn=psycopg2.connect(**configs)
        cur=conn.cursor()
        query="SELECT * FROM ka_series WHERE id = %s"


        cur.execute(query,id)
        serie_id=cur.fetchall()
        conn.commit()
        cur.close()
        conn.close
        

        return serie_id
    

    def create_series(self):

        conn=psycopg2.connect(**configs)
        cur=conn.cursor()

        query = """
            INSERT INTO ka_series
                (serie,seasons,released_date,genre,imdb_rating)
            VALUES
                (%s,%s,%s,%s,%s)
            RETURNING *
        """


        query_values=tuple(self.__dict__.values())
        
        cur.execute(query, query_values)
        conn.commit()
        inserte_one = cur.fetchone()

        cur.close()
        conn.close()

        return inserte_one