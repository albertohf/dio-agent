"""Login de LABORATÓRIO, propositalmente vulnerável a SQL Injection.

Use só localmente, para o agente analisar. Não publique como aplicação real.
"""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users (username TEXT, password TEXT)")
db.execute("INSERT INTO users VALUES ('admin', 'senha-de-teste')")


def login(username, password):
    # VULNERÁVEL: a entrada da pessoa é concatenada direto no SQL
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return db.execute(query).fetchone() is not None


if __name__ == "__main__":
    print(login(input("Usuário: "), input("Senha: ")))
