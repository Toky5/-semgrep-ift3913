import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users (nom TEXT, age INTEGER)")


def recherche_directe():
    nom = input("Nom : ")
    return db.execute(f"SELECT * FROM users WHERE nom = '{nom}'").fetchall()


def recherche_en_deux_etapes():
    nom = input("Nom : ")
    requete = f"SELECT * FROM users WHERE nom = '{nom}'"
    return db.execute(requete).fetchall()


def recherche_par_age():
    age = int(input("Âge : "))
    return db.execute(f"SELECT * FROM users WHERE age = {age}").fetchall()


def recherche_parametree():
    nom = input("Nom : ")
    return db.execute("SELECT * FROM users WHERE nom = ?", (nom,)).fetchall()
