from conexionBD import *

try:
    miCursor=conexion.cursor()

    sql="create table clientes4(id int primary key auto_increment, nombre varchar(60), direccion varchar(120),tel varchar(10))"

    miCursor.execute(sql)

except:
    print(f"Ocurrio un problema, por favor verifique ...")
else:
    print("Se creo exitosamente")