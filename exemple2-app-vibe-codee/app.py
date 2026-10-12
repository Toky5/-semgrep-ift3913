import sqlite3

API_KEY = "sk-proj-DEMO0FAKE0KEY0FOR0SEMGREP0IFT3913"


def chercher_utilisateur(db, nom):
    return db.execute(f"SELECT * FROM users WHERE nom = '{nom}'").fetchall()


def chercher_utilisateur_corrige(db, nom):
    return db.execute("SELECT * FROM users WHERE nom = ?", (nom,)).fetchall()


def supprimer_utilisateur(db, nom):
    db.execute(f"DELETE FROM users WHERE nom = '{nom}'")


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (nom TEXT)")
    db.executemany("INSERT INTO users VALUES (?)", [("alice",), ("bob",)])

    assert chercher_utilisateur(db, "alice") == [("alice",)]
    assert chercher_utilisateur_corrige(db, "' OR '1'='1") == []
    print("Tests normaux : OK")

    assert chercher_utilisateur(db, "' OR '1'='1") == [], "injection SQL : tous les utilisateurs sont renvoyés"
    print("Test d'injection : OK")
