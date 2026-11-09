import sqlite3
from pathlib import Path

MAPE = Path(__file__).parent
con = sqlite3.connect(MAPE / "skola.db", isolation_level=None)
con.execute("PRAGMA foreign_keys = ON")

def radit(sql, parametri=()):
    cur = con.execute(sql, parametri)
    rindas = cur.fetchall()
    kolonnas = [k[0] for k in cur.description]

    platumi = [len(k) for k in kolonnas]
    for rinda in rindas:
        for i, elem in enumerate(rinda):
            platumi[i] = max(platumi[i], len(str(elem)))

    for i, k in enumerate(kolonnas):
        print(f"{k:<{platumi[i]}}", end="  ")
    print()
    for rinda in rindas:
        for i, elem in enumerate(rinda):
            print(f"{str(elem):<{platumi[i]}}", end="  ")
        print()
    print(f"Rindu skaits: {len(rindas)}")

radit("""CREATE TABLE Lasitaji (
            id int PRIMARY KEY,
            vards varchar(255) NOT NULL,
            uzvards varchar(255) NOT NULL,
            email varchar(255) UNIQUE
            );
        CREATE TABLE Autori (
            id int PRIMARY KEY,
            vards varchar(255) NOT NULL,
            uzvards varchar(255) NOT NULL
            );
        CREATE TABLE Gramatas (
            id int PRIMARY KEY,
            nosaukums varchar(255) NOT NULL,
            FOREIGN KEY (autors),
            lpp int NOT NULL,
            izdosanas_gads int NOT NULL
            );
        CREATE TABLE Eksemplari (
            id int PRIMARY KEY,
            FOREIGN KEY (gramata_id)
            );
        CREATE TABLE Izsniegumi (
            id int PRIMARY KEY,
            FOREIGN KEY (eksemplars_id),
            FOREIGN KEY (lasitajs_id),
            izsniegsanas_datums date NOT NULL DEFAULT CURDATE(),
            atgriesanas_datums date CHECK (izsniegsanas_datums <= atgriesanas_datums)
            );
        )""")