import sqlite3

try:
    import os
    os.makedirs("./database", exist_ok=True)

    # Conexão com o banco de dados SQLite
    connection = sqlite3.connect("./database/database.db")

    # Criação de um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Criando a primeira tabela [users]
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            email TEXT NOT NULL UNIQUE,
            cpf TEXT NOT NULL UNIQUE,
            birth_date DATE NOT NULL,
            glasses BOOLEAN NOT NULL
        )
        '''
    )

    # Criando a tabela [Vehicles]
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS vehicles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            model TEXT NOT NULL,
            brand TEXT NOT NULL,
            year INTEGER NOT NULL,
            color TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        '''
    )

    # Criando a tabela [Brands]
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS brands(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            acronym TEXT NOT NULL UNIQUE
        )
        '''
    )
    
    # Salvando (commit) as mudanças
    connection.commit()
    print("Tabelas criadas com sucesso!")
    
except sqlite3.Error as e:
    print("Erro ao criar tabelas:", e)
    
finally:
    if connection: #type:ignore
        cursor.close() #type:ignore
        connection.close()