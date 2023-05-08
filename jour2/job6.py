import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Azerty01",
  database="LaPlateforme"
)

# Récupération de la somme des capacités
mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(capacite) FROM salles")
result = mycursor.fetchone()

# Affichage du résultat dans la console
print("Somme des capacités des salles:", result[0])
