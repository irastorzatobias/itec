import sqlite3 as sql
from sqlite3 import Error
# Apunte Tobias Irastorza, modificado para que funcione con la EFI. Original aparte.


# TIPOS DE DATOS SQLITE3
# text: se usa para almacenar cadenas de caracteres. Una cadena es una secuencia de caracteres. Se coloca entre comillas (simples); ejemplo: 'Hola', 'Juan Perez'. El tipo "text" define una cadena de longitud variable.
# integer: se usa para guardar valores numéricos enteros. Definimos campos de este tipo cuando queremos representar, por ejemplo, cantidades.
# real: se usa para almacenar valores numéricos con decimales. Se utiliza como separador el punto (.). Definimos campos de este tipo para precios, por ejemplo.
# blob: se usa para almacenar valores en formato binario (imágenes, archivos de sonido etc.)

def createDB(name):
    """ Recibe un nombre y crea la base de datos"""
    try:
        conn = sql.connect(f'{name}.db')
        conn.commit()
        conn.close()
        return (f'Conexion con base de datos establecida')
    except Error:
        return (Error)
        
        
def createTable(nameDb, table): # se podria agregar metodo fields
    """ Recibe el nombre de la base de datos y nombre de la tabla"""
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""CREATE TABLE {table} (
                name text NOT NULL UNIQUE,
                turn text NOT NULL,
                payment text NOT NULL
                )"""
        cursor.execute(instruccion)
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        return ('Tabla creada con exito')
    except:
        return ('Conexion con tabla establecida')



def insertRow(nameDb,table,nombre, turnos, pago):
    """ Inserta nombre y edad en nuestra base de datos que contiene personas"""
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""INSERT INTO {table}
                            VALUES ('{nombre}', '{turnos}','{pago}')"""
        cursor.execute(instruccion)
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        return (f'Se agrego {nombre} a la tabla')
    except:
        return ('Ya existe el alumno')
        


def readRows(nameDb, table):
    """ lee todos los datos de la BD """
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""SELECT * from {table}""" # seleccionar todos los datos de la tabla
        cursor.execute(instruccion)
        datos = cursor.fetchall() # obtengo todos los datos
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        return (datos)
    except Error:
        return 'Error BD'
        
def insertRows(nameDb, table, listPersonas):
    """ Inserta varios datos tras pasarle una tupla a la funcion """
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""INSERT INTO {table}
                        VALUES (?, ?)"""
        cursor.executemany(instruccion, listPersonas) # segundo parametro la lista de tuplas
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
    except Error:
        print(Error)


def readOrdered(nameDb, table, field):
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""SELECT * from {table} ORDER BY {field}""" # seleccionar todos los datos de la tabla y ordena por field
        cursor.execute(instruccion)
        datos = cursor.fetchall() # obtengo todos los datos
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        print(datos)
    except Error:
        print(Error)

def search(nameDb, table, condition):
    """ Busqueda de datos a partir de una condicion """
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""SELECT * from {table} WHERE {condition}""" # seleccionar todos los datos de la tabla y filtra
        cursor.execute(instruccion)
        datos = cursor.fetchall() # obtengo todos los datos
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        return datos
    except Error as er:
        print(Error)


def updateFields(nombreAnterior,nombreNuevo,turnos,pago):
    """ Update de todos los fields, se usa al agregar alumno o al modificar alumno"""
    conn = sql.connect('motus.db')
    cursor = conn.cursor()
    instruccion = f"""UPDATE alumnos SET 
                            name='{nombreNuevo}', turn='{turnos}', payment='{pago}' WHERE name = '{nombreAnterior}'"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()
    
def updateTurns(nombre,turnos):
    """ Update de los turnos"""
    conn = sql.connect('motus.db')
    cursor = conn.cursor()
    instruccion = f"""UPDATE alumnos SET turn='{turnos}' WHERE name = '{nombre}'"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()
    
def updatePay(nombre,pago):
    """ Update del pago"""
    conn = sql.connect('motus.db')
    cursor = conn.cursor()
    instruccion = f"""UPDATE alumnos SET payment='{pago}' WHERE name = '{nombre}'"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()
    

    



def deleteRow(condition):
    conn = sql.connect(f'motus.db')
    cursor = conn.cursor()
    instruccion = f"""DELETE FROM alumnos WHERE {condition}"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()

def deleteTable(name, table):
    conn = sql.connect(f'{name}.db')
    cursor = conn.cursor()
    instruccion = f"""DROP TABLE {table}"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()
    

def main():
    # createDB('test')
    # createTable('personas','humano')
    # insertRow('personas','humano','Tobias',21)
    # readRows('personas','humano')
    p = [
        ('Lautaro', 25),
        ('Patricia', 50),
        ('Marcelo', 55)
    ]
    # insertRows('personas', 'humano',p)
    # readRows('personas', 'humano')
    # readOrdered('personas','humano','age')
    # search('personas', 'humano',"name like 'T%'") # porcentaje para ver los nombres que empiezan por T
    # updateFields()
    # deleteItem('personas','humano',"name like 'T%'")
    # readRows('personas','humano')

    
    
    
    
if __name__ == '__main__':
    main()