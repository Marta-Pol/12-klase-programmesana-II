# Praktiskais darbs: bibliotēkas serveris

**Apjoms:** 4 × 40 minūtes · **Veids:** pie datora · **Rīki:** Python, Flask, `sqlite3`, `requests`
**Datubāze:** tava `biblioteka.db` no 12-033 (`uzdevumi.py`, 26. uzdevums)
**Starta fails:** [`serveris.py`](serveris.py) · **Pēc tam:** mājasdarbs
[`majasdarbs-serveris.md`](majasdarbs-serveris.md) — izpēte par to, ko šeit uzbūvēsi

**Mērķis:** izveidot tīmekļa serveri, kas apkalpo paša veidotu datubāzi, ir drošs pret
nederīgiem datiem, raksta žurnālu, ir pieejams citiem lokālajā tīklā un ir dokumentēts tā, lai
to var lietot cits.

| Stunda | Tēma | Stundas beigās strādā |
| --- | --- | --- |
| 1 | Pirmais serveris: GET, JSON, 404 | 4 maršruti, kas lasa datus no datubāzes |
| 2 | Parametri un validācija | meklēšana, lappušošana, 400 kļūdas, statistika |
| 3 | Datu pieņemšana un kļūdu apstrāde | POST maršruti, 201 / 400 / 404 / 409, droša 500 |
| 4 | Žurnāls, tīkls, dokumentācija | serveris tīklā, `serveris.log`, `SERVERIS.md` |

**Nodevums pēc 4. stundas:** `serveris.py`, `parbaude.py`, `SERVERIS.md` repozitorijā.

---

## Sagatavošanās (pirms 1. stundas vai tās pirmajās minūtēs)

```bash
pip install flask requests
```

1. Pārbaudi, ka mapē ir `biblioteka.db` ar datiem. Ja nav, palaid savu `izveidot_biblioteku()`
   no `uzdevumi.py`.
2. Nokopē [`serveris.py`](serveris.py) savā mapē blakus `biblioteka.db`.
3. Palaid `python3 serveris.py` un atver `http://127.0.0.1:5001/`.

> **Kāpēc 5001, nevis 5000?** Uz macOS ports 5000 bieži ir aizņemts. Ja gribi to redzēt,
> pamēģini `port=5000` un pieraksti kļūdas paziņojumu. Kas to aizņem, noskaidrosi mājasdarbā.
>
> **Ja tava shēma atšķiras** no klases parauga (piemēram, nav tabulas `autori`), pielāgo
> vaicājumus savai shēmai. Maršrutiem un atbilžu formai jāpaliek tādai, kā aprakstīts.

**Kā testēt.** `GET` pieprasījumus var atvērt pārlūkā. `POST` pieprasījumus no adrešu joslas
nosūtīt nevar, tāpēc tos testē ar failu `parbaude.py` (to sāksi 3. stundā):

```python
import requests

URL = "http://127.0.0.1:5001"

def paradit(atbilde):
    print(atbilde.status_code, atbilde.request.method, atbilde.url)
    print("   ", atbilde.json())

paradit(requests.get(f"{URL}/api/gramatas/1"))
paradit(requests.post(f"{URL}/api/lasitaji", json={"vards": "Jānis", "uzvards": "Kļava",
                                                  "epasts": "janis@skola.lv"}))
```

Serverim jāstrādā **vienā** terminālī, `parbaude.py` palaid **otrā**.

---

## 1. stunda · Pirmais serveris

**Gaita**
- 5' — atkārtojums no 11. klases: klients, serveris, maršruts, JSON. Ko nozīmē
  `127.0.0.1:5001` — kura daļa ir adrese, kura ports?
- 10' — demo: `serveris.py` palaišana, `row_factory`, `jsonify`, maršruts ar `<int:id>`
- 22' — uzdevumi
- 3' — commit

**Statusa kodi, kas būs vajadzīgi visās četrās stundās**

| Kods | Nozīme | Kad mūsu serverī |
| --- | --- | --- |
| 200 | OK | dati atgriezti |
| 201 | Created | izveidots jauns ieraksts |
| 400 | Bad Request | klients atsūtīja nederīgus datus |
| 404 | Not Found | tāda ieraksta vai adreses nav |
| 405 | Method Not Allowed | adrese ir, bet ne ar šo metodi |
| 409 | Conflict | dati ir derīgi, bet konfliktē ar esošajiem (dubults e-pasts, jau izsniegts) |
| 500 | Internal Server Error | kļūda servera kodā — vaina nav klientam |

**Uzdevumi**

1. Palaid serveri un atver `/`. Nomaini ziņas tekstu, saglabā failu un atjauno lapu. Serveri
   nepārstartēji — kāpēc izmaiņa tomēr ir redzama? Atbildi komentārā.

2. **`GET /api/gramatas`** — visas grāmatas, sakārtotas pēc nosaukuma. Katrai grāmatai:
   `id`, `nosaukums`, `autors` (vārds un uzvārds vienā laukā), `gads` un `eksemplari`
   (eksemplāru skaits). Atbildes forma:
   ```json
   {"skaits": 6, "dati": [{"id": 6, "nosaukums": "Aka", "autors": "Regīna Ezera", "gads": 1972, "eksemplari": 1}, …]}
   ```
   *Padoms:* `JOIN autori`, `LEFT JOIN eksemplari`, `COUNT(e.id)`, `GROUP BY g.id`.
   Kāpēc `LEFT JOIN`, nevis `JOIN`?

3. **`GET /api/gramatas/<int:id>`** — viena grāmata ar sarakstu `eksemplari`. Katram
   eksemplāram ir `id`, `svitrkods` un `pieejams` (`true` / `false`). Ja grāmatas nav, atbilde ir
   `{"kluda": "Grāmata nav atrasta"}` ar statusa kodu **404**.
   *Padoms:* eksemplārs nav pieejams, ja tam ir izsniegums ar `atgriezts IS NULL`.
   Neaizmirsti: `?`, nevis f-string.

4. Atver `/api/gramatas/abc` un `/api/gramatas/-1`. Ko atgriež serveris un kāpēc? Pieraksti
   komentārā, ko šeit izdara `<int:id>` tavā vietā.

5. **`GET /api/lasitaji`** — tikai `id`, `vards`, `uzvards`, sakārtoti pēc uzvārda. Komentārā
   pamato, kāpēc šajā sarakstā **neatgriežam** e-pastu un telefonu, lai gan tie datubāzē ir.

6. ★ **`GET /api/autori/<int:id>/gramatas`** — visas autora grāmatas. Ja autora nav — 404.
   Ja autors ir, bet viņam nav grāmatu — tukšs saraksts un 200. Kāpēc šie gadījumi atšķiras?

**Stundas beigās:** visi četri maršruti atgriež JSON no datubāzes; neesošs `id` dod 404 ar
JSON kļūdu, nevis HTML lapu. **Commit.**

---

## 2. stunda · Parametri un validācija

**Gaita**
- 5' — kas notiek, ja kods dara `int(request.args["limit"])` un kāds atsūta `?limit=abc`?
- 10' — demo: `request.args.get`, palīgfunkcija validācijai, 400 ar paskaidrojumu
- 22' — uzdevumi
- 3' — commit

**Uzdevumi**

7. Papildini `GET /api/gramatas` ar neobligātiem parametriem:
   - `?meklet=` — daļa no nosaukuma (`WHERE nosaukums LIKE '%' || ? || '%'`);
   - `?no=` un `?lidz=` — izdošanas gadu robežas.

   Pārbaudi `/api/gramatas?meklet=ē` un `/api/gramatas?no=1900&lidz=1950`.

8. Pievieno lappušošanu: `?limit=` (noklusējums 20, atļauts 1–100) un `?offset=` (noklusējums 0,
   ne mazāks par 0). Uzraksti palīgfunkciju:
   ```python
   def vesels_skaitlis(nosaukums, noklusejums, min_v=None, max_v=None):
       """Nolasa request.args[nosaukums]; ja nav — noklusējums.
       Ja nav vesels skaitlis vai ir ārpus robežām — raise ValueError("…saprotams teksts…")."""
   ```
   Maršrutā noķer `ValueError` un atgriez **400** ar tās tekstu. Atsevišķi pārbaudi, ka `no`
   nav lielāks par `lidz`.

9. Aizpildi tabulu `serveris.py` beigās komentārā. Katrai adresei vispirms uzraksti, ko
   **gaidi**, un tikai tad pārbaudi.

   | Adrese | Gaidītais kods | Faktiskais kods |
   | --- | --- | --- |
   | `/api/gramatas?limit=abc` | | |
   | `/api/gramatas?limit=0` | | |
   | `/api/gramatas?limit=1000` | | |
   | `/api/gramatas?offset=-1` | | |
   | `/api/gramatas?no=2000&lidz=1900` | | |
   | `/api/gramatas?meklet=zzz` | | |

10. **`GET /api/izsniegti`** — eksemplāri, kas pašlaik ir pie lasītājiem: `svitrkods`,
    `nosaukums`, `lasitajs`, `izsniegts` un `dienas` (cik dienas pie lasītāja). Sakārto tā, lai
    ilgāk turētie ir augšā.
    *Padoms:* `julianday('now') - julianday(izsniegts)`. Līdzīgs vaicājums bija 29. uzdevumā.

11. **`GET /api/statistika`** — viens JSON objekts ar datubāzes kopsavilkumu:
    ```json
    {"gramatas": 6, "eksemplari": 7, "lasitaji": 5, "pasreiz_izsniegti": 4,
     "populararaka": {"nosaukums": "…", "reizes": 2}}
    ```

12. ★ **SQL injekcija darbībā.** Pagaidām pievieno apzināti ievainojamu maršrutu:
    ```python
    @app.get("/api/nedrosi")
    def nedrosi():
        nos = request.args.get("nosaukums", "")
        return jsonify(vaicajums(f"SELECT id, nosaukums FROM gramatas WHERE nosaukums = '{nos}'"))
    ```
    Pārlūkā izmēģini `?nosaukums=Aka`, tad `?nosaukums=' OR '1'='1`, tad
    `?nosaukums=' UNION SELECT id, epasts FROM lasitaji --`. Komentārā pieraksti, ko ieguvi un
    kāpēc tas izdevās. Pārraksti vaicājumu ar `?`, pārbaudi abus uzbrukumus vēlreiz, un tad
    **izdzēs** maršrutu.

**Stundas beigās:** neviena adrese ar nederīgu parametru neizraisa 500; katra 400 atbilde
pasaka, kurš parametrs ir nepareizs un kāpēc. **Commit.**

---

## 3. stunda · Datu pieņemšana un kļūdu apstrāde

**Gaita**
- 5' — `GET` pret `POST`; kāpēc jauns ieraksts dod 201, nevis 200
- 10' — demo: `request.get_json(silent=True)`, `IntegrityError` → 409, `parbaude.py`
- 22' — uzdevumi
- 3' — commit

**Uzdevumi**

13. **`POST /api/lasitaji`** — reģistrē jaunu lasītāju no JSON
    `{"vards", "uzvards", "epasts", "telefons"}`. Validācija:
    - `vards`, `uzvards`, `epasts` — obligāti, teksts, ne tukšs, ne garāks par 100 simboliem;
    - `epasts` satur `@`;
    - `telefons` — var nebūt; ja ir, tad tieši 8 cipari;
    - ja nav atsūtīts JSON objekts — 400.

    Ja kļūdas ir, atgriez **visas uzreiz**:
    `{"kluda": "Nederīgi dati", "detalas": ["'vards' ir obligāts teksts", …]}` ar 400.
    Ja e-pasts jau ir datubāzē — **409**. Lai to noteiktu, noķer `sqlite3.IntegrityError` no
    `UNIQUE` ierobežojuma, nevis pārbaudi ar atsevišķu `SELECT` pirms tam. Kāpēc tā ir
    drošāk? Atbildi komentārā.
    Ja izdodas — **201** un jaunā lasītāja `id`.

14. **`POST /api/izsniegumi`** — izsniedz eksemplāru: `{"eksemplars_id": 2, "lasitajs_id": 3}`.
    | Gadījums | Kods |
    | --- | --- |
    | ID nav veseli skaitļi vai trūkst | 400 |
    | eksemplārs vai lasītājs neeksistē | 404 |
    | eksemplārs jau ir pie kāda (ir izsniegums ar `atgriezts IS NULL`) | 409 |
    | izdevās | 201 |

15. **`POST /api/izsniegumi/<int:id>/atgriezt`** — iestata `atgriezts = CURRENT_DATE`.
    Neesošs izsniegums — 404, jau atgriezts — 409, izdevās — 200. Ar `GET /api/gramatas/<id>`
    pārbaudi, ka eksemplārs atkal ir `pieejams: true`.

16. **Kļūdu apstrādātāji.** Pievieno `@app.errorhandler(404)`, `(405)` un `(500)`, kas visi
    atgriež JSON formā `{"kluda": "…"}`. Pārbaudi tā:
    - atver `/nekas` un nosūti `requests.delete(f"{URL}/api/gramatas")`;
    - izveido pagaidu maršrutu `/api/salauzts` ar drukas kļūdu tabulas nosaukumā (`gramataas`).
      Atver to ar `debug=True` un pēc tam ar `debug=False`. Komentārā pieraksti, ko klients redz
      katrā gadījumā un kur tagad var atrast īsto kļūdas tekstu. Ar `debug=True` pārlūkā
      parādās interaktīvais atkļūdotājs — pieraksti, ko tas piedāvā darīt. Kāpēc tas ir
      bīstami, noskaidrosi mājasdarbā. Pēc tam maršrutu izdzēs.

17. ★ **`POST /api/izsniegumi/vairaki`** —
    `{"lasitajs_id": 2, "eksemplari": [2, 5]}` izsniedz vairākus eksemplārus **visus vai
    nevienu** (`BEGIN` / `COMMIT` / `ROLLBACK`, kā kinoteātra biļetēm 35. uzdevumā). Pārbaudi:
    viens eksemplārs brīvs, otrs jau izsniegts → atbilde 409, un brīvais eksemplārs **joprojām
    ir pieejams**.

**`parbaude.py`** — šīs stundas beigās tajā jābūt vismaz vienam veiksmīgam un vienam
neveiksmīgam pieprasījumam katram `POST` maršrutam.

**Stundas beigās:** nevienā kļūdas atbildē nav SQL, *traceback* vai faila ceļa; katrs
kļūdas gadījums atgriež pareizo kodu. **Commit.**

---

## 4. stunda · Žurnāls, tīkls, dokumentācija

**Gaita**
- 5' — eksperiments: pāris mēģina atvērt tavu serveri pēc tava IP. Kāpēc neizdodas?
- 10' — demo: `logging`, `@app.before_request`, `@app.after_request`, `g`
- 22' — uzdevumi
- 3' — commit un nodošana

**Uzdevumi**

18. **Žurnalēšana.** Katrs pieprasījums tiek pierakstīts failā `serveris.log` vienā rindā:
    ```
    2026-11-26 10:14:03 192.168.1.37 GET /api/gramatas?limit=5 200 3ms
    ```
    *Padomi:* `logging.basicConfig(filename=…, level=logging.INFO, format="%(asctime)s %(message)s")`;
    `@app.before_request` saglabā sākuma laiku `g.sakums = time.perf_counter()`;
    `@app.after_request` saņem `atbilde`, pieraksta rindu un atgriež `atbilde`. Klienta IP ir
    `request.remote_addr`.
    Žurnālā **nedrīkst** nonākt pieprasījuma saturs (e-pasti, telefoni). Atver `serveris.log` un
    pārbaudi, kur nonāca 16. uzdevuma 500 kļūdas *traceback*.

19. **Serveris tīklā.** Noskaidro sava datora IP adresi lokālajā tīklā (`ipconfig` / `ifconfig`).
    - a) Serveris vēl darbojas ar `app.run(port=5001, …)`. Pāris atver
      `http://<tava IP>:5001/api/statistika` no sava datora. Pieraksti, ko viņš redz.
    - b) Nomaini uz `app.run(host="0.0.0.0", port=5001, debug=False)` un mēģiniet vēlreiz.
    - c) Komentārā vienā teikumā: kas mainījās?

    Atrodi `serveris.log` rindu ar pāra IP adresi — tas ir pierādījums, ko ieliksi `SERVERIS.md`.
    *Ja neizdodas:* pārbaudi ugunsmūri un to, vai abi esat vienā tīklā. Skolas Wi-Fi var
    bloķēt ierīču savstarpējo saziņu (klientu izolācija) — tad lietojiet telefona karstvietu.

20. **Pāra «uzbrukums», 10 minūtes.** Pāris ar savu `parbaude.py` mēģina panākt, ka tavs serveris
    atgriež 500, izpauž e-pastus vai pieņem acīmredzami nederīgus datus. Pieraksti katru
    mēģinājumu:

    | Pieprasījums | Gaidīju | Saņēmu | Izlabots? |
    | --- | --- | --- | --- |
    | | | | |

    Izlabo vismaz vienu atrasto problēmu. Ja pārim neizdevās atrast nevienu, pieraksti trīs
    viņa mēģinājumus un to, kura tava koda rinda viņu apturēja.

21. **`SERVERIS.md`** — dokumentācija, pēc kuras cits skolēns var tavu serveri palaist un lietot:
    - **palaišana no nulles:** kas jāinstalē, kā izveidot datubāzi, kā palaist, kādā adresē
      atvērt;
    - **maršrutu tabula:** metode, adrese, parametri vai JSON ķermenis, veiksmīgas atbildes
      piemērs, iespējamie kļūdu kodi;
    - **žurnāls:** trīs rindas no `serveris.log`, tostarp pāra pieprasījums no 19. uzdevuma;
    - **drošība:** kas izdarīts (parametrizēti vaicājumi, validācija, droša 500, `debug=False`) un
      kas **apzināti nav** izdarīts (piemēram, nav pieteikšanās, nav HTTPS).

22. ★ **Pieprasījumu ierobežošana.** Ne vairāk kā 30 pieprasījumi minūtē no vienas IP adreses.
    Ja vairāk — **429** `{"kluda": "Pārāk daudz pieprasījumu"}`. Pārbaudi ar ciklu `parbaude.py`.
    *Padoms:* vārdnīca `{ip: [laiks, laiks, …]}` un `@app.before_request`.

**Stundas beigās:** serveris darbojas tīklā ar `debug=False`, raksta žurnālu, un `SERVERIS.md`
ir repozitorijā. **Commit un nodošana.**

---

## Gatavs, ja

- [ ] `GET` maršruti: `/api/gramatas` (ar meklēšanu un lappušošanu), `/api/gramatas/<id>`,
      `/api/lasitaji`, `/api/izsniegti`, `/api/statistika`.
- [ ] `POST` maršruti: `/api/lasitaji`, `/api/izsniegumi`, `/api/izsniegumi/<id>/atgriezt`.
- [ ] Visi vaicājumi lieto `?`, nevienā vaicājumā nav f-string vai `+`.
- [ ] Katrs kļūdas gadījums atgriež JSON un pareizo kodu: 400, 404, 405, 409, 500.
- [ ] Neviena atbilde neatklāj SQL, *traceback*, faila ceļu, e-pastus vai telefonus.
- [ ] `serveris.log` pieraksta katru pieprasījumu; tajā ir pieprasījums no cita datora.
- [ ] `debug=False`, kad serveris ir pieejams tīklā.
- [ ] `parbaude.py` testē katru `POST` maršrutu ar derīgiem un nederīgiem datiem.
- [ ] `SERVERIS.md` — palaišana, maršrutu tabula, žurnāla piemērs, drošība.

---

## Metodiskās piezīmes

- **Vispirms prakse, tad izpēte.** Skolēni vispirms pieredz to, ko mājasdarbs pēc tam liek
  izskaidrot: aizņemtu portu, `debug=True` atkļūdotāju, `127.0.0.1` pret `0.0.0.0`, žurnālu.
  Praktiskajā darbā šie punkti apzināti tikai novēroti un pierakstīti, bez skaidrojuma.
  Mājasdarbs lieto skolēna paša `serveris.py`, `serveris.log` un 16. un 19. uzdevuma
  pierakstus, tāpēc to izsniedz **pēc 4. stundas**. Nākamās stundas sākumā — trīs mutiski
  jautājumi no tā.
- **Secība salīdzinājumā ar plānu.** Šis darbs aptver 12-040, 12-041, 12-042 un daļu no 12-045
  (README 61.–63., 65.–71., 80.–82. uzdevums). 64. uzdevums (pieteikšanās ar jaucējvērtībām)
  apzināti atstāts 12-037. SQL injekcija 12. uzdevumā ir ★ «āķis» 12-039 stundai, ne tās
  aizstājējs. 17. uzdevums (transakcija) der arī kā ievads 12-034 transakcijām, ja tās vēl
  nav izietas.
- **Ports 5000 uz macOS** bieži ir aizņemts (AirPlay uztvērējs), tāpēc visur ir 5001.
- **`app.json.ensure_ascii = False`** jau ir starta failā — bez tā latviešu burti JSON
  atbildē parādās kā `ē`, un skolēni domā, ka kaut kas salūzis.
- **Pārlūks pats kodē** pēdiņas un atstarpes adresē, tāpēc 12. uzdevuma uzbrukumu var
  ievadīt tieši adrešu joslā.
- **Windows un `curl`.** Ar JSON pēdiņām PowerShell ir neērti, tāpēc `POST` pieprasījumus testē
  ar `requests` (`parbaude.py`), ne ar `curl`.
- **19. uzdevums var neizdoties skolas tīkla dēļ.** Pārbaudi iepriekš, vai divi datori kabinetā
  redz viens otru (`ping`). Ja nē — telefona karstvieta vai skolotāja maršrutētājs.
- **Datu atjaunošana.** Pēc 3. stundas testiem datubāzē sakrājas testa lasītāji un izsniegumi.
  `izveidot_biblioteku()` atjauno sākotnējo stāvokli.
