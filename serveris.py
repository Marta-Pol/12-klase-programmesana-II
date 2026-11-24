# ==========================================================
# 02. bloks — BIBLIOTĒKAS SERVERIS (praktiskais darbs, 4 stundas)
# ==========================================================
# Uzdevumi: praktiskais-serveris.md
# Datubāze: tava biblioteka.db no 12-033 (uzdevumi.py, 26. uzdevums)
#
# Palaišana:   python3 serveris.py
# Pārbaude:    pārlūkā atver http://127.0.0.1:5001/
# Apturēšana:  Ctrl+C terminālī

import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

MAPE = Path(__file__).parent
DB = MAPE / "biblioteka.db"

app = Flask(__name__)
app.json.ensure_ascii = False   # lai JSON rāda "Nāves ēnā", nevis "Nāves ēnā"


# ----------------------------------------------------------
# Palīgfunkcijas — tās jau ir gatavas
# ----------------------------------------------------------

def db():
    """Jauns savienojums katram pieprasījumam."""
    con = sqlite3.connect(DB, isolation_level=None)
    con.row_factory = sqlite3.Row             # rindas var pārvērst par dict
    con.execute("PRAGMA foreign_keys = ON")
    return con


def vaicajums(sql, parametri=()):
    """Izpilda SELECT un atgriež sarakstu ar vārdnīcām — tieši tas, ko var ielikt jsonify."""
    con = db()
    try:
        return [dict(rinda) for rinda in con.execute(sql, parametri)]
    finally:
        con.close()


def kluda(teksts, kods):
    """Vienmēr viena un tā pati kļūdas atbildes forma: {"kluda": "..."}."""
    return jsonify({"kluda": teksts}), kods


# ----------------------------------------------------------
# Maršruti
# ----------------------------------------------------------

@app.get("/")
def sakums():
    return jsonify({"zina": "Bibliotēkas serveris strādā, bet mani Drifters drīz noķers </3"}) #ziņa redzama, jo serveris atpazīst izmaiņas un pats reloadoja


# 1. stunda — 2.–6. uzdevums
# GET /api/gramatas
# GET /api/gramatas/<int:id>
# GET /api/lasitaji
# ★ GET /api/autori/<int:id>/gramatas
@app.get("/api/gramatas")
def gramatas():
    meklet = request.args.get("meklet")
    if meklet:
        result = vaicajums("""SELECT gramatas.id, nosaukums, CONCAT(autori.vards, ' ', autori.uzvards) AS autors, COUNT(eksemplari.id) AS eksemplari FROM gramatas
                            JOIN autori ON gramatas.autors_id = autori.id 
                            LEFT JOIN eksemplari ON eksemplari.gramata_id = gramatas.id 
                            WHERE gramatas.nosaukums LIKE '%' || ? || '%'
                            GROUP BY gramatas.id;""", (meklet, ))
    else:
        result = vaicajums("""SELECT gramatas.id, nosaukums, CONCAT(autori.vards, ' ', autori.uzvards) AS autors, COUNT(eksemplari.id) AS eksemplari FROM gramatas
                                    JOIN autori ON gramatas.autors_id = autori.id 
                                    LEFT JOIN eksemplari ON eksemplari.gramata_id = gramatas.id 
                                    GROUP BY gramatas.id;""")
    print(result)
    return jsonify({"skaits": len(result), "dati": result})

@app.get("/api/gramatas/<int:id>")
def gramatasArId(id):
    result = vaicajums("""SELECT gramatas.id, nosaukums, CONCAT(autori.vards, ' ', autori.uzvards) AS autors, COUNT(eksemplari.id) AS eksemplari, izdosanas_gads AS gads FROM gramatas
                            JOIN autori ON gramatas.autors_id = autori.id 
                            LEFT JOIN eksemplari ON eksemplari.gramata_id = gramatas.id
                            WHERE gramatas.id = ?
                            GROUP BY gramatas.id;""", (id, ))
    if len(result) == 0:
        return jsonify({"kluda" : "Drifteris tevi noķers"}), 400
    return jsonify({"dati": result})

@app.get("/api/lasitaji")
def lasitaji():
    result = vaicajums("""SELECT id, vards, uzvards FROM Lasitaji;""")
    return jsonify({"skaits": len(result), "dati": result})

# 2. stunda — 7.–12. uzdevums
# GET /api/gramatas?meklet=&no=&lidz=&limit=&offset=
# GET /api/izsniegti
# GET /api/statistika


# 3. stunda — 13.–17. uzdevums
# POST /api/lasitaji
# POST /api/izsniegumi
# POST /api/izsniegumi/<int:id>/atgriezt
# kļūdu apstrādātāji 404, 405, 500
# ★ POST /api/izsniegumi/vairaki


# 4. stunda — 18.–22. uzdevums
# žurnalēšana: @app.before_request un @app.after_request


if __name__ == "__main__":
    # 4. stundā: debug=False un host="0.0.0.0" (19. uzdevums)
    app.run(port=5001, debug=True)
