import re


def zd_jelszo_elemzes(jelszo):
    kisbetuk = re.findall(r"[a-záéíóöőúüű]", jelszo)
    nagybetuk = re.findall(r"[A-ZÁÉÍÓÖŐÚÜŰ]", jelszo)
    szamok = re.findall(r"\d", jelszo)
    specialis_karakterek = re.findall(r"[^A-Za-z0-9áéíóöőúüűÁÉÍÓÖŐÚÜŰ]", jelszo)
    szamok_helyettesitve = re.sub(r"\d", "#", jelszo)

    ellenorzesek = {
        "hossz": len(jelszo) >= 12,
        "kisbetu": len(kisbetuk) > 0,
        "nagybetu": len(nagybetuk) > 0,
        "szam": len(szamok) > 0,
        "kulonleges": len(specialis_karakterek) > 0,
        "valtozatossag": len(set(jelszo)) >= min(8, len(jelszo)),
        "gyakori": not bool(re.search(r"(?i)(password|jelszo|qwerty|123456|admin)", jelszo))
    }

    if szamok_helyettesitve == "######":
        ellenorzesek["gyakori"] = False

    pontszam = sum(ellenorzesek.values()) * 100 // len(ellenorzesek)

    if pontszam <= 28:
        szint = "Gyenge"
    elif pontszam <= 57:
        szint = "Közepes"
    elif pontszam <= 85:
        szint = "Erős"
    else:
        szint = "Nagyon erős"

    javaslatok = []
    if not ellenorzesek["hossz"]:
        javaslatok.append("Használj legalább 12 karakter hosszú jelszót.")
    if not ellenorzesek["kisbetu"]:
        javaslatok.append("Tegyél bele legalább egy kisbetűt.")
    if not ellenorzesek["nagybetu"]:
        javaslatok.append("Tegyél bele legalább egy nagybetűt.")
    if not ellenorzesek["szam"]:
        javaslatok.append("Tegyél bele legalább egy számot.")
    if not ellenorzesek["kulonleges"]:
        javaslatok.append("Használj speciális karaktert is, például !, ?, # vagy %.")
    if not ellenorzesek["valtozatossag"]:
        javaslatok.append("Kerüld a karakterek túlzott ismétlését.")
    if not ellenorzesek["gyakori"]:
        javaslatok.append("Kerüld a gyakori szavakat és könnyen kitalálható számsorokat.")

    return {
        "pontszam": pontszam,
        "szint": szint,
        "ellenorzesek": ellenorzesek,
        "javaslatok": javaslatok
    }


class ZDBiztonsagiElemzo:
    def __init__(self):
        self.legutobbi_eredmeny = None

    def zd_eredmeny_elerheto(self):
        return self.legutobbi_eredmeny is not None

    def zd_pontszam_lekerese(self):
        if self.legutobbi_eredmeny is None:
            return 0
        return self.legutobbi_eredmeny["pontszam"]

    def zd_besorolas_lekerese(self):
        if self.legutobbi_eredmeny is None:
            return "Nincs elemzés"
        return self.legutobbi_eredmeny["szint"]
