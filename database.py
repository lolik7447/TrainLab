import psycopg2
from sshtunnel import SSHTunnelForwarder
from sshtunnel import BaseSSHTunnelForwarderError
from decouple import config

host = config('HOST')
user = config('USER')
password = config('PASSWORD')
database = config('DATABASE')
bd_ip = config('BD_IP')
port = int(config('PORT'))
remote_bind_address = (host, port)
# ssh_port = 22
# ssh_username = config('SSH_USERNAME')
# ssh_private_key = config('SSH_PRIVATE_KEY')



def get_text_from_database_by_front_id(front_id_bd):
    try:
        # with SSHTunnelForwarder(
        #         (bd_ip, 22),
        #         ssh_username=ssh_username,
        #         ssh_private_key=ssh_private_key,
        #         remote_bind_address=remote_bind_address) as server:
        #
        #     server.start()

            params = {
                'database': database,
                'user': user,
                'password': password,
                'host': host,
                'port': port
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
        # with SSHTunnelForwarder(
        #         (bd_ip, 22),
        #         ssh_username=ssh_username,
        #         ssh_private_key=ssh_private_key,
        #         remote_bind_address=remote_bind_address) as server:
        #
        #     server.start()
            params = {
                'database': database,
                'user': user,
                'password': password,
                'host': host,
                'port': port
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


# Получаем текст по front_id
text_to_change = get_text_from_database_by_front_id("1.1")
# Изменяем текст в базе данных
change_text_in_database_by_front_id("1.1", "Новый текст")
