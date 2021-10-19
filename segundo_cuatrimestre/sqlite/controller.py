import sqlite3 as sql

def createDB(name):
    """ Recibe un nombre y crea la base de datos"""
    try:
        conn = sql.connect(f'{name}.db')
        conn.commit()
        conn.close()
        print(f'La base de datos {name} fue creada con exito')
    except:
        print('La base de datos ya esta creada')
        
def createTable(nameDb, table): # se podria agregar metodo fields
    """ Recibe el nombre de la base de datos y nombre de la tabla"""
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""CREATE TABLE {table} (
            name text,
            age integer
            )"""
        cursor.execute(instruccion)
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        print('Tabla creada con exito')
    except:
        print('Error conexion BD o tabla ya existente')


def insertRow(nameDb,table,nombre, edad):
    """ Inserta nombre y edad en nuestra base de datos que contiene personas"""
    try:
        conn = sql.connect(f'{nameDb}.db')
        cursor = conn.cursor()
        instruccion = f"""INSERT INTO {table}
                        VALUES ('{nombre}', {edad})"""
        cursor.execute(instruccion)
        conn.commit() # realizar los cambios
        cursor.close()
        conn.close()
        print(f'Se agrego {nombre} a la tabla')
    except:
        print('Error conexion BD o datos ya existentes') 


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
        print(datos)
    except:
        print('Error conexion BD o tabla no existente') 
        
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
    except:
        print('Error conexion BD o datos ya existentes') 


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
    except:
        print('Error conexion BD o tabla no existente')  


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
        print(datos)
    except:
        print('Error conexion BD o tabla no existente')


def updateFields():
    """ Update de algun field """
    conn = sql.connect('personas.db')
    cursor = conn.cursor()
    instruccion = f"""UPDATE humano SET age=22 WHERE name like 'Tobias'"""
    cursor.execute(instruccion)
    conn.commit() # realizar los cambios
    conn.close()
    


def deleteItem(name, table, condition):
    conn = sql.connect(f'{name}.db')
    cursor = conn.cursor()
    instruccion = f"""DELETE FROM {table} WHERE {condition}"""
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
    insertRow('personas','humano','Tobias',21)
    readRows('personas','humano')
    
    
    
    
if __name__ == '__main__':
    main()