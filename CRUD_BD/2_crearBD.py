import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
    )
except:
    print(f"Ocurrio un error con el sistema porfavor verlifique")
else:
    #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    miCursor=conexion.cursor()

    sql='create database bd_python'
    #Ejecutar la consulta SQL
    miCursor.execute(sql)

    if miCursor:
        print("La BD se creo exitosamente")

    #Mostrar las BD que existen en el SGBD MySQL
    miCursor.execute("show databases")

    for x in miCursor:
        print(x)