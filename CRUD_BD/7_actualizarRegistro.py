from conexionBD import *
try:
    miCursor=conexion.cursor()

    sql="update clientes set direccion='Col. Nueva Vizcaya' where id=1"
    miCursor.execute(sql)

    conexion.commit()
except:
    print("Ocurrio un error, por favor Verifique ...")
else:
    print("Registro actualizado exitosamenete")