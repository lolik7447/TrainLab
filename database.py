import psycopg2
from sshtunnel import SSHTunnelForwarder
from database_connection import bd


def change_text_in_database_by_front_id(front_id_bd, text_to_change):
    try:
        with SSHTunnelForwarder(
                (f"{bd.bd_ip}", 22),
                ssh_username=f"{bd.ssh_username}",
                ssh_private_key=f"{bd.ssh_private_key}",
                remote_bind_address=(f"{bd.remote_bind_address}", 25060)) as server:

            server.start()

            params = {
                'database': f"{bd.database}",
                'user': f"{bd.user}",
                'password': f"{bd.password}",
                'host': f"{bd.host}",
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"update frontend_data SET text='{text_to_change}'"
                         f" WHERE front_id='{front_id_bd}';")
            conn.commit()
            conn.close()
            return True

    except:
        print("Connection Failed")


def take_text_from_database_by_front_id(front_id_bd):
    try:
        with SSHTunnelForwarder(
                (f"{bd.bd_ip}", 22),
                ssh_username=f"{bd.ssh_username}",
                ssh_private_key=f"{bd.ssh_private_key}",
                remote_bind_address=(f"{bd.remote_bind_address}", 25060)) as server:

            server.start()
            print('Server connected via SSH')

            params = {
                'database': f"{bd.database}",
                'user': f"{bd.user}",
                'password': f"{bd.password}",
                'host': f"{bd.host}",
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"SELECT text FROM frontend_data WHERE front_id='{front_id}';")
            conn.commit()
            first_text = curs.fetchall()[0][0]
            print(first_text)
            curs.execute(f"update frontend_data SET text='{text}' WHERE front_id='{front_id}';")
            conn.commit()
            curs.execute("SELECT text FROM frontend_data WHERE front_id='1.1';")
            conn.commit()
            second_text = curs.fetchall()[0][0]
            print(second_text)
            curs.execute(f"update frontend_data SET text='{first_text}' WHERE front_id='{front_id}';")
            conn.commit()
            conn.close()
            return second_text

    except:
        print("Connection Failed")