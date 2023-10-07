import psycopg2
from sshtunnel import SSHTunnelForwarder
from sshtunnel import BaseSSHTunnelForwarderError
import os

host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
database = os.environ['DATABASE']
bd_ip = os.environ['BD_IP']
ssh_port = int(os.environ['SSH_PORT'])
ssh_username = os.environ['SSH_USERNAME']
ssh_private_key = os.environ['SSH_PRIVATE_KEY']
remote_bind_address = (os.environ['HOST'], int(os.environ['PORT']))
port = int(os.environ['PORT'])


def get_text_from_database_by_front_id(front_id_bd):
    try:
        with SSHTunnelForwarder(
                (bd_ip, 22),
                ssh_username=ssh_username,
                ssh_private_key=ssh_private_key,
                remote_bind_address=remote_bind_address) as server:

            server.start()

            params = {
                'database': database,
                'user': user,
                'password': password,
                'host': host,
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"SELECT text FROM frontend_data WHERE front_id='{front_id_bd}';")
            conn.commit()
            text = curs.fetchall()[0][0]
            conn.close()
            return text

    except Exception as e:
        print("An error occurred:", e)


def change_text_in_database_by_front_id(front_id_bd, text_to_change):
    try:
        with SSHTunnelForwarder(
                (bd_ip, 22),
                ssh_username=ssh_username,
                ssh_private_key=ssh_private_key,
                remote_bind_address=remote_bind_address) as server:

            server.start()

            params = {
                'database': database,
                'user': user,
                'password': password,
                'host': host,
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"UPDATE frontend_data SET text='{text_to_change}' WHERE front_id='{front_id_bd}';")
            conn.commit()
            conn.close()
            return True

    except psycopg2.Error as e:
        print("PostgreSQL error:", e)
    except BaseSSHTunnelForwarderError as e:
        print("SSH tunnel error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


# Пример использования:
# Получаем текст по front_id
text_to_change = get_text_from_database_by_front_id("1.1")

# Изменяем текст в базе данных
change_text_in_database_by_front_id("1.1", "Новый текст")
