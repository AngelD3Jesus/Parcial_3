import mysql.connector

try:
#Conectar con la BD en Mysql
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )

except:
    print("Ocurrio un error con el servidor, Porfavor verifique ...")

#verificar si la conexion fue exitosa
#if conexion.is_connected():
#    print(f"Exito")
#else:
#    print(f"No exito... verifique")