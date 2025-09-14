from eventos import data_base_connection, close_connection
from database.models import Evento, Participantes
import sqlite3

# Opção 1: Inserindo dados com parâmetros dinâmicos usando '?'  
def insert_event_option_1(name, date, location, description=None) -> None:
    connection, cursor = data_base_connection()
    if not connection or not cursor:
        return
    
    try:
        cursor.execute(
            '''
            INSERT INTO events (name, date, location, description)
            VALUES (?, ?, ?, ?) 
            ''', # inserindo dados dinamicamente com o caracter '?'
            (name, date, location, description)
        )
        connection.commit()
        print("Evento inserido com sucesso!")
        
    except sqlite3.DatabaseError as err: #type:ignore
        print("Erro ao inserir evento: ", err)
        
    finally:
        if cursor: #type:ignore
            cursor.close() #type:ignore
        close_connection(connection)
        
# Opção 2: Inserindo dados com parâmetros nomeados usando ':param'
def insert_event_option_2(name, date, location, description=None) -> None:
    connection, cursor = data_base_connection()
    if not connection or not cursor:
        return
    
    try:
        cursor.execute(
            '''
            INSERT INTO events (name, date, location, description)
            VALUES (:name, :date, :location, :description)
            ''', # inserindo dados dinamicamente com o caracter ':param'
            {
                "name": name,
                "date": date,
                "location": location,
                "description": description
            }
        )
        connection.commit()
        print("Evento inserido com sucesso!")
        
    except sqlite3.DatabaseError as err: #type:ignore
        print("Erro ao inserir evento: ", err)
        
    finally:
        if cursor: #type:ignore
            cursor.close() #type:ignore
        close_connection(connection)
        
if __name__ == "__main__":
    python_conf = Evento(
        name="Python Conference 2024",
        date="2024-05-15",
        location="São Paulo, Brasil",
        description="Uma conferência sobre as últimas novidades em Python."
    )
    
    catalyst_league = Evento(
        name="Runescape Catalyst League",
        date="2025-09-15",
        location="Online",
        description="Uma liga competitiva de Runescape."
    )
    
    insert_event_option_1(
        name=python_conf.name,
        date=python_conf.date,
        location=python_conf.location,
        description=python_conf.description
    )
    insert_event_option_2(
        name=catalyst_league.name,
        date=catalyst_league.date,
        location=catalyst_league.location,
        description=catalyst_league.description
    )