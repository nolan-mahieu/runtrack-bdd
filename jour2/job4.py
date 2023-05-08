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

query = "SELECT nom, capacite FROM salles"
cursor.execute(query)

print("Noms et capacités des salles:")
for (nom, capacite) in cursor:
    print(f"{nom}: {capacite} personnes")

cursor.close()
cnx.close()