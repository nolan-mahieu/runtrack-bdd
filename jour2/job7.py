import sqlite3

class EmployeDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(self, nom, prenom, salaire, id_service):
        self.cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (?, ?, ?, ?)",
                            (nom, prenom, salaire, id_service))
        self.conn.commit()

    def read(self, id):
        self.cursor.execute("SELECT * FROM employes WHERE id=?", (id,))
        return self.cursor.fetchone()

    def update(self, id, nom, prenom, salaire, id_service):
        self.cursor.execute("UPDATE employes SET nom=?, prenom=?, salaire=?, id_service=? WHERE id=?",
                            (nom, prenom, salaire, id_service, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM employes WHERE id=?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

