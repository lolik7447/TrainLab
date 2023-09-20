import psycopg2
from sshtunnel import SSHTunnelForwarder
from sshtunnel import BaseSSHTunnelForwarderError



def change_text_in_database_by_front_id(front_id_bd, text_to_change):
    try:
        with SSHTunnelForwarder(
                (f"{bd_ip}", 22),
                ssh_username=f"{ssh_username}",
                ssh_private_key=f"{ssh_private_key}",
                remote_bind_address=(f"{remote_bind_address}", 25060)) as server:

            server.start()

            params = {
                'database': f"{database}",
                'user': f"{username}",
                'password': f"{password}",
                'host': f"{host}",
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"update frontend_data SET text='{text_to_change}'"
                         f" WHERE front_id='{front_id_bd}';")
            conn.commit()
            conn.close()
            return True


    except psycopg2.Error as e: print("PostgreSQL error:", e)
    except BaseSSHTunnelForwarderError as e: print("SSH tunnel error:", e)
    except Exception as e: print("An unexpected error occurred:", e)


def take_text_from_database_by_front_id(front_id_bd):
    try:
        with SSHTunnelForwarder(
                (f"{bd_ip}", 22),
                ssh_username=f"{ssh_username}",
                ssh_private_key=f"{ssh_private_key}",
                remote_bind_address=(f"{remote_bind_address}", 25060)) as server:

            server.start()
            print('Server connected via SSH')

            params = {
                'database': f"{database}",
                'user': f"{username}",
                'password': f"{password}",
                'host': f"{host}",
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
