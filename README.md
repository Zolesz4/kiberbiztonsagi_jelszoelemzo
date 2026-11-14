# Kiberbiztonsági jelszóelemző

## Hallgató
Név: [Írd ide a teljes neved]
Monogram: ZD

## Feladat leírása
A program grafikus felületen megadott jelszavak alapvető biztonsági jellemzőit vizsgálja. Ellenőrzi a jelszó hosszát, a kis- és nagybetűk, számok és speciális karakterek meglétét, a karakterek változatosságát, valamint néhány gyakori vagy könnyen kitalálható mintát. Az eredmény pontszámként, szöveges besorolásként és javítási javaslatokként jelenik meg.

A program helyben végzi az elemzést. A beírt jelszót nem küldi el interneten keresztül, és nem menti fájlba vagy adatbázisba.

## Indítás
A projekt Python 3 környezetet igényel. Külső csomag telepítése nem szükséges.

A program indítása a projekt mappájából:

```bash
python main.py
```

A Tkinter grafikus felületnek telepítve kell lennie a Python környezetben.

## Modulok és függvények

### Tanult modul: tkinter
Az `app.py` modul a Tkinter könyvtárat használja grafikus felület létrehozására.
Felhasznált elemek: `Tk`, `StringVar`, `Entry`, `Label`, `Button`, `Checkbutton`, `Progressbar`, `Text`, `messagebox`.

### Bemutatandó modul: re
A `zd_sajat_modul.py` a reguláris kifejezések `re` modulját használja.
- `re.search()`: megvizsgálja, hogy a jelszó tartalmaz-e adott karaktert vagy mintát.
- `re.findall()`: listába gyűjti a kisbetűket, nagybetűket, számokat és speciális karaktereket.
- `re.sub()`: a számjegyeket `#` karakterre cseréli a gyakori számsorozat ellenőrzéséhez.

### Saját modul: zd_sajat_modul.py
- Saját függvény: `zd_jelszo_elemzes()`
- Saját osztály: `ZDBiztonsagiElemzo`
- Osztálymetódusok: `zd_eredmeny_elerheto()`, `zd_pontszam_lekerese()`, `zd_besorolas_lekerese()`

## Osztályok
- `ZDJelszoElemzoApp`: a grafikus alkalmazás felületét és eseménykezelését valósítja meg.
- `ZDBiztonsagiElemzo`: az elemzés eredményének tárolására és lekérdezésére szolgáló saját osztály.

## Eseménykezelés
- Az Elemzés gomb elindítja a jelszóvizsgálatot.
- Az Enter billentyű lenyomása szintén elindítja az elemzést.
- A Jelszó megjelenítése jelölőnégyzet váltja a jelszó láthatóságát.
- A Törlés gomb alaphelyzetbe állítja a felületet.
- A Kilépés gomb bezárja az alkalmazást.

## Fájlstruktúra
- `main.py` – a program indítása
- `app.py` – grafikus felület és eseménykezelés
- `zd_sajat_modul.py` – saját modul, függvény és osztály
- `README.md` – a projekt leírása
