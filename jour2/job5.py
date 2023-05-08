import mysql.connector

config = {
    'user': 'root',
    'password': 'Azerty01',
    'host': 'localhost',
    'database': 'LaPlateforme',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)

result = cursor.fetchone()
total_superficie = result[0]

print(f"La superficie de La Plateforme est de {total_superficie} m2")

cursor.close()
cnx.close()