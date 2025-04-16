import psycopg2

def conectar():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5433",
            options="-c client_encoding=UTF8"
        )
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco de dados:")
        print(repr(e))
        return None
