"""Mesmo login de laboratório, com consulta parametrizada (SQL Injection mitigado)."""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users (username TEXT, password TEXT)")
db.execute("INSERT INTO users VALUES ('admin', 'senha-de-teste')")


def login(username, password):
    # CORRIGIDO: os valores vão como parâmetros, nunca como parte do SQL
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return db.execute(query, (username, password)).fetchone() is not None


if __name__ == "__main__":
    print(login(input("Usuário: "), input("Senha: ")))
