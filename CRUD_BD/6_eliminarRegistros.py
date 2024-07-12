from conexionBD import *
try:
    miCursor=conexion.cursor()

    sql="delete from clientes4 where id=3"
    miCursor.execute(sql)

    conexion.commit()
except:
    print("Ocurrio un error, por favor Verifique ...")
else:
    print("Registro eliminado exitosamenete")
