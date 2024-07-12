from conexionBD import *

try:
    miCursor=conexion.cursor()

    sql="select * from clientes"
    miCursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecucion de la linea anterior exexute para posteriormente mostrar con ciclo 
    resultado=miCursor.fetchall()
except:
    print("Ocurrio un error, por favor Verifique ...")
else:
    for x in resultado:
        print(x)

    