import sqlite3

def data_base_connection():
    try:
        import os
        os.makedirs("./database", exist_ok=True)

        # Conexão com o banco de dados SQLite
        connection = sqlite3.connect("D:/faculdade/desenvolvimento_agil_com_python/python/database/database_eventos.db")

        # Criação de um cursor para executar comandos SQL
        cursor = connection.cursor()

        return connection, cursor

    except sqlite3.DatabaseError as err: #type:ignore
        print("Erro no banco de dados: ", err)
        return None, None
    
def close_connection(connection):    
    if connection: #type:ignore
        connection.close() #type:ignore
        print("Conexão com o banco de dados fechada.")
        
def create_tables():
    connection, cursor = data_base_connection()
    if not connection or not cursor:
        return
    
    try:
        # Criando a tabela [events]
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS events(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date DATE NOT NULL,
                location TEXT NOT NULL,
                description TEXT
            )
            '''
        )

        # Criando a tabela [attendees]
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS attendees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                registration_date DATE NOT NULL,
                FOREIGN KEY (event_id) REFERENCES events (id)
            )
            '''
        )

        # Salvando (commit) as mudanças
        connection.commit()
        print("Tabelas criadas com sucesso!")
        
    except sqlite3.DatabaseError as err: #type:ignore
        print("Erro no banco de dados: ", err)

    finally:
        if cursor: #type:ignore
            cursor.close() #type:ignore
        close_connection(connection)
        
if __name__ == "__main__":
    create_tables()