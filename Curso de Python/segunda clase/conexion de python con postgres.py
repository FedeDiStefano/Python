import psycopg2

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres",
    port="5434"
)
connection.autocommit = True


def creartabla():
    cursor = connection.cursor()
    query = "create table usuario (nombre varchar (30), correo varchar (30), email varchar (30))"
    cursor.execute(query)
    cursor.close()


creartabla()
