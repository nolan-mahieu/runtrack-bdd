import mysql.connector


config = {
    'user': 'root',
    'password': 'Azerty01',
    'host': 'localhost',
    'database': 'LaPlateforme',
}


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


query = "SELECT * FROM etudiants;"
cursor.execute(query)


print("Liste des étudiants :")
for (id, nom, prenom, age, email) in cursor:
    print(f"{id} - {nom} {prenom} - {age} ans - {email}")


cursor.close()
cnx.close()