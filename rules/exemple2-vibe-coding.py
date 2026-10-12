import os
import sqlite3

# ruleid: cle-api-dans-le-code
API_KEY = "sk-proj-DEMO0FAKE0KEY0FOR0SEMGREP0TESTS0000"
# ok: cle-api-dans-le-code
API_KEY_OK = os.environ["OPENAI_API_KEY"]


def chercher(db, nom):
    # ruleid: injection-sql-fstring
    db.execute(f"SELECT * FROM users WHERE nom = '{nom}'")
    # ok: injection-sql-fstring
    db.execute("SELECT * FROM users WHERE nom = ?", (nom,))
