# importing psycopg2 module as psy 
import psycopg2 as psy
from decouple import config

class DatabaseConnection:
    def connecting_database(self):
        try:
            self.connection = psy.connect(
                                user=config('DB_USER'),
                                password=config('DB_PASSWORD'),
                                host=config('DB_HOST'),  
                                port=config('DB_PORT'),       
                                database=config('DB_NAME')
                                )
            self.cursor = self.connection.cursor()
        

            
        except:
            print("Error while connecting to PostgreSQL")
        finally:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
