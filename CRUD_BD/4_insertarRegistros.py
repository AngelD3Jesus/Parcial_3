from conexionBD import *
try:
    micursor=conexion.cursor()
    nombre=input("Ingrese el nombre:")
    direccion=input("Ingrese su direccion:")
    tel=input("Ingrese el numero de telefono:")
    
    # sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Angel', 'Col primero de mayo', '6181234567')"
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL,%s,%s,%s)"
    valores=(nombre,direccion,tel)

    micursor.execute(sql,valores)
except:
    print("OCURRIO UN ERROR")
#SIRVE PARA FINALIZAR DE MANERA EXITOSA LA EJECUCION DEL SQL
conexion.commit()

print("Registro Insertado correctamente")