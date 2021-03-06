import pg8000
from os import environ
username = environ.get('PGUSER', 'jan')
password = environ.get('PGPASSWORD', 'nonofyourbussiness')
host = environ.get('PGHOST', 'localhost')
port = environ.get('PGPORT', '5433')
database = environ.get('PGDATABASE', "jan")


conn = pg8000.dbapi.connect(username, password=password, host=host, port=port, database=database)
cursor = conn.cursor()
cursor.execute("SELECT * from p1_measurements")
results = cursor.fetchall()
for row in results:
    print(row)