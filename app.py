import tkinter as tk
from tkinter import ttk, messagebox

from zd_sajat_modul import ZDBiztonsagiElemzo, zd_jelszo_elemzes


class ZDJelszoElemzoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kiberbiztonsági jelszóelemző")
        self.root.geometry("760x620")
        self.root.minsize(680, 560)
        self.root.configure(bg="#eef2f7")

        self.elemzo = ZDBiztonsagiElemzo()
        self.jelszo_lathato = tk.BooleanVar(value=False)
        self.jelszo = tk.StringVar()

        self.stilus = ttk.Style()
        self.stilus.theme_use("clam")
        self.stilus.configure("TFrame", background="#eef2f7")
        self.stilus.configure("TLabel", background="#eef2f7", font=("Arial", 10))
        self.stilus.configure("Cim.TLabel", font=("Arial", 19, "bold"), foreground="#17324d")
        self.stilus.configure("Alcim.TLabel", font=("Arial", 11), foreground="#526579")
        self.stilus.configure("TButton", font=("Arial", 10, "bold"), padding=8)
        self.stilus.configure("TCheckbutton", background="#eef2f7", font=("Arial", 9))
        self.stilus.configure("Eredmeny.TLabel", font=("Arial", 12, "bold"), foreground="#17324d")

        self._felulet_letrehozasa()

    def _felulet_letrehozasa(self):
        fo = ttk.Frame(self.root, padding=24)
        fo.pack(fill="both", expand=True)

        ttk.Label(fo, text="Kiberbiztonsági jelszóelemző", style="Cim.TLabel").pack(anchor="w")
        ttk.Label(
            fo,
            text="Helyi ellenőrzés: a megadott jelszó nem kerül elküldésre vagy elmentésre.",
            style="Alcim.TLabel"
        ).pack(anchor="w", pady=(5, 20))

        ttk.Label(fo, text="Vizsgálandó jelszó").pack(anchor="w")
        beviteli_sor = ttk.Frame(fo)
        beviteli_sor.pack(fill="x", pady=(6, 4))

        self.jelszo_mezo = ttk.Entry(
            beviteli_sor,
            textvariable=self.jelszo,
            show="*",
            font=("Arial", 12)
        )
        self.jelszo_mezo.pack(side="left", fill="x", expand=True, ipady=7)
        self.jelszo_mezo.bind("<Return>", self._enter_esemeny)

        ttk.Checkbutton(
            fo,
            text="Jelszó megjelenítése",
            variable=self.jelszo_lathato,
            command=self._lathatosag_valtoztatasa
        ).pack(anchor="w", pady=(2, 12))

        gomb_sor = ttk.Frame(fo)
        gomb_sor.pack(fill="x", pady=(0, 18))

        ttk.Button(gomb_sor, text="Elemzés", command=self._elemzes_esemeny).pack(side="left")
        ttk.Button(gomb_sor, text="Törlés", command=self._torles_esemeny).pack(side="left", padx=8)
        ttk.Button(gomb_sor, text="Kilépés", command=self.root.destroy).pack(side="right")

        ttk.Separator(fo).pack(fill="x", pady=8)

        ttk.Label(fo, text="Értékelés", style="Eredmeny.TLabel").pack(anchor="w", pady=(8, 6))
        self.erosseg_cimke = ttk.Label(fo, text="Még nincs elemzés", style="Eredmeny.TLabel")
        self.erosseg_cimke.pack(anchor="w")

        self.pontszam_cimke = ttk.Label(fo, text="Pontszám: –")
        self.pontszam_cimke.pack(anchor="w", pady=(4, 8))

        self.mertek = ttk.Progressbar(fo, maximum=100, mode="determinate")
        self.mertek.pack(fill="x", pady=(0, 14))

        ttk.Label(fo, text="Ellenőrzési szempontok", style="Eredmeny.TLabel").pack(anchor="w", pady=(4, 6))
        self.ellenorzesek = ttk.Frame(fo)
        self.ellenorzesek.pack(fill="x")

        self.reszletek = {}
        for kulcs, felirat in [
            ("hossz", "Legalább 12 karakter"),
            ("kisbetu", "Tartalmaz kisbetűt"),
            ("nagybetu", "Tartalmaz nagybetűt"),
            ("szam", "Tartalmaz számot"),
            ("kulonleges", "Tartalmaz speciális karaktert"),
            ("valtozatossag", "Nem ismétlődő, változatos karakterhasználat"),
            ("gyakori", "Nem szerepel az egyszerű vagy gyakori minták között")
        ]:
            cimke = ttk.Label(self.ellenorzesek, text="○  " + felirat)
            cimke.pack(anchor="w", pady=2)
            self.reszletek[kulcs] = (cimke, felirat)

        ttk.Label(fo, text="Javaslatok", style="Eredmeny.TLabel").pack(anchor="w", pady=(16, 6))
        self.javaslatok = tk.Text(
            fo,
            height=5,
            wrap="word",
            font=("Arial", 10),
            relief="flat",
            bg="#ffffff",
            fg="#263746",
            padx=10,
            pady=8
        )
        self.javaslatok.pack(fill="both", expand=True)
        self.javaslatok.insert("1.0", "Az elemzéshez írj be egy jelszót, majd kattints az Elemzés gombra.")
        self.javaslatok.configure(state="disabled")

    def _lathatosag_valtoztatasa(self):
        self.jelszo_mezo.configure(show="" if self.jelszo_lathato.get() else "*")

    def _enter_esemeny(self, esemeny):
        self._elemzes_esemeny()

    def _elemzes_esemeny(self):
        beirt_jelszo = self.jelszo.get()
        if not beirt_jelszo:
            messagebox.showwarning("Hiányzó adat", "Adj meg egy jelszót az elemzéshez!")
            self.jelszo_mezo.focus_set()
            return

        eredmeny = zd_jelszo_elemzes(beirt_jelszo)
        self.elemzo.legutobbi_eredmeny = eredmeny

        self.erosseg_cimke.configure(text="Besorolás: " + eredmeny["szint"])
        self.pontszam_cimke.configure(text=f"Pontszám: {eredmeny['pontszam']} / 100")
        self.mertek["value"] = eredmeny["pontszam"]

        for kulcs, (cimke, felirat) in self.reszletek.items():
            jel = "✓" if eredmeny["ellenorzesek"][kulcs] else "✗"
            cimke.configure(text=f"{jel}  {felirat}")

        self.javaslatok.configure(state="normal")
        self.javaslatok.delete("1.0", "end")
        for javaslat in eredmeny["javaslatok"]:
            self.javaslatok.insert("end", "• " + javaslat + "\n")
        if not eredmeny["javaslatok"]:
            self.javaslatok.insert("end", "A vizsgált szempontok alapján nem találtam további javítandó elemet.")
        self.javaslatok.configure(state="disabled")

    def _torles_esemeny(self):
        self.jelszo.set("")
        self.erosseg_cimke.configure(text="Még nincs elemzés")
        self.pontszam_cimke.configure(text="Pontszám: –")
        self.mertek["value"] = 0
        for cimke, felirat in self.reszletek.values():
            cimke.configure(text="○  " + felirat)
        self.javaslatok.configure(state="normal")
        self.javaslatok.delete("1.0", "end")
        self.javaslatok.insert("1.0", "Az elemzéshez írj be egy jelszót, majd kattints az Elemzés gombra.")
        self.javaslatok.configure(state="disabled")
        self.jelszo_mezo.focus_set()
