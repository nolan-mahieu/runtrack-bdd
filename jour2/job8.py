import sqlite3

class ZooDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        self.cursor.execute("INSERT INTO animaux (nom, race, id_cage, date_naissance, pays_origine) VALUES (?, ?, ?, ?, ?)",
                            (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()

    def create_cage(self, superficie, capacite_max):
        self.cursor.execute("INSERT INTO cages (superficie, capacite_max) VALUES (?, ?)",
                            (superficie, capacite_max))
        self.conn.commit()

    def delete_animal(self, id):
        self.cursor.execute("DELETE FROM animaux WHERE id=?", (id,))
        self.conn.commit()

    def delete_cage(self, id):
        self.cursor.execute("DELETE FROM cages WHERE id=?", (id,))
        self.conn.commit()

    def update_animal(self, id, nom, race, id_cage, date_naissance, pays_origine):
        self.cursor.execute("UPDATE animaux SET nom=?, race=?, id_cage=?, date_naissance=?, pays_origine=? WHERE id=?",
                            (nom, race, id_cage, date_naissance, pays_origine, id))
        self.conn.commit()

    def update_cage(self, id, superficie, capacite_max):
        self.cursor.execute("UPDATE cages SET superficie=?, capacite_max=? WHERE id=?",
                            (superficie, capacite_max, id))
        self.conn.commit()

    def get_animaux(self):
        self.cursor.execute("SELECT * FROM animaux")
        return self.cursor.fetchall()

    def get_cages(self):
        self.cursor.execute("SELECT * FROM cages")
        return self.cursor.fetchall()

    def get_animaux_in_cage(self, id_cage):
        self.cursor.execute("SELECT * FROM animaux WHERE id_cage=?", (id_cage,))
        return self.cursor.fetchall()

    def get_superficie_totale(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cages")
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

def main():
    zoo_db = ZooDB("zoo.db")

    while True:
        print("Menu:")
        print("1. Ajouter un animal")
        print("2. Ajouter une cage")
        print("3. Supprimer un animal")
        print("4. Supprimer une cage")
        print("5. Modifier un animal")
        print("6. Modifier une cage")
        print("7. Afficher les animaux")
        print("8. Afficher les animaux dans une cage")
        print("9. Calculer la superficie totale des cages")
        print("0. Quitter")
        choix = int(input("Entrez le numéro de votre choix: "))

        if choix == 1:
            nom = input("Entrez le nom de l'animal: ")
            race = input("Entrez la race de l'animal: ")
            id_cage = int(input("Entrez l'ID de la cage: "))
            date_naissance = input("Entrez la date de naissance (YYYY-MM-DD): ")
            pays_origine = input("Entrez le pays d'origine: ")
            zoo_db.create_animal(nom, race, id_cage, date_naissance, pays_origine)

        elif choix == 2:
            superficie = float(input("Entrez la superficie de la cage: "))
            capacite_max = int(input("Entrez la capacité maximale de la cage: "))
            zoo_db.create_cage(superficie, capacite_max)

        elif choix == 3:
            id_animal = int(input("Entrez l'ID de l'animal à supprimer: "))
            zoo_db.delete_animal(id_animal)

        elif choix == 4:
            id_cage = int(input("Entrez l'ID de la cage à supprimer: "))
            zoo_db.delete_cage(id_cage)

        elif choix == 5:
            id_animal = int(input("Entrez l'ID de l'animal à modifier: "))
            nom = input("Entrez le nouveau nom de l'animal: ")
            race = input("Entrez la nouvelle race de l'animal: ")
            id_cage = int(input("Entrez le nouvel ID de la cage: "))
            date_naissance = input("Entrez la nouvelle date de naissance (YYYY-MM-DD): ")
            pays_origine = input("Entrez le nouveau pays d'origine: ")
            zoo_db.update_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)

        elif choix == 6:
            id_cage = int(input("Entrez l'ID de la cage à modifier: "))
            superficie = float(input("Entrez la nouvelle superficie de la cage: "))
            capacite_max = int(input("Entrez la nouvelle capacité maximale de la cage: "))
            zoo_db.update_cage(id_cage, superficie, capacite_max)

        elif choix == 7:
            animaux = zoo_db.get_animaux()
            for animal in animaux:
                print(animal)

        elif choix == 8:
            id_cage = int(input("Entrez l'ID de la cage: "))
            animaux = zoo_db.get_animaux_in_cage(id_cage)
            for animal in animaux:
                print(animal)

        elif choix == 9:
            superficie_totale = zoo_db.get_superficie_totale()
            print(f"La superficie totale de toutes les cages est de {superficie_totale}")

        elif choix == 0:
            zoo_db.close()
            break

if __name__ == "__main__":
    main()