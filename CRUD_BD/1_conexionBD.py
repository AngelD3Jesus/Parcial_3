import mysql.connector

try:
#Conectar con la BD en Mysql
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
except Exception as e:
    # print(f"Error: {e}")
    # print(f"Tipo de excepcion: {type(e).__name__}")
    print(f"Ocurrio un error con el servidor ... Porfavor verifique ...")

else:
#verificar si la conexion fue exitosa
    if conexion.is_connected():
        print(f"exito")
    else:
        print(f"no exito... verifique")