# ==========================================================
# 01. OBJEKTORIENTĒTĀ PROGRAMMĒŠANA UN ĀRĒJĀS BIBLIOTĒKAS — DARBA FAILS
# ==========================================================
# Šeit raksti savus risinājumus.
# Teorija, piemēri un atgādne: teorija.py
# Uzdevumu numuri iet cauri visam blokam.
# ==========================================================


# ----------------------------------------------------------
# 12-001 · Kursa ievads un OOP atkārtojums
# ----------------------------------------------------------

# 1. Izlasi [kurss/eksamens.md](../kurss/eksamens.md) un pieraksti, kura eksāmena daļa tev
#    šķiet grūtākā un kāpēc.

# 4. daļa

# 2. Uzraksti klasi Prece ar konstruktoru un divām metodēm — bez ieskatīšanās vecajā kodā.

from sqlite3 import Date
from traceback import StackSummary


class Prece:
    def __init__(self, nosaukums, cena, kategorija): # init -> initialize
        self.nosaukums = nosaukums
        self.cena = cena
        self.kategorija = kategorija

    def info(self):
        return f"Preces nosaukums: {self.nosaukums}, cena: {self.cena}, kategorija: {self.kategorija}"

    def akcija(self, procenti):
        return self.cena - self.cena * (procenti / 100)

# tomats = Prece("Tomāti", 3, "dārzeņi")
# print(tomats.info())
# print(tomats.akcija(30))

# 3. ★ Pieraksti, ko tu no 11. klases OOP nesaproti līdz galam. To risināsim šajā blokā.

# ----------------------------------------------------------
# 12-002 · Klase, objekts, konstruktors
# ----------------------------------------------------------

# 4. Izveido klasi Rezervacija ar konstruktoru (vards, datums, vietu_skaits) un metodi
#    apraksts().



# 5. Izveido trīs objektus un izvadi to aprakstus.




# 6. Pievieno metodi mainitvietas(jaunsskaits), kas neļauj skaitu padarīt negatīvu.




# 7. ★ Pievieno metodi, kas atgriež True, ja rezervācija ir šodienai.





# ----------------------------------------------------------
# 12-003 · Vairāki konstruktori
# ----------------------------------------------------------

# 8. Pievieno Rezervacija konstruktoram noklusējuma vērtību vietu skaitam.




# 9. Izveido @classmethod no_rindas(rinda), kas izveido objektu no CSV rindas.




# 10. Izveido @classmethod tuksa(), kas izveido objektu ar noklusējuma vērtībām.




# 11. Pārbaudi visus trīs izveides veidus vienā programmā.




# 12. ★ Pieraksti, ar ko šī pieeja atšķiras no vairākiem konstruktoriem C# valodā. _Norāde:
#    eksāmenā var būt jautājums par konstruktoriem vispārīgi, ne tikai Python._





# ----------------------------------------------------------
# 12-004 · Iekapsulēšana
# ----------------------------------------------------------

# 13. Pārraksti klasi Konts tā, lai atlikumu var lasīt, bet ne tieši mainīt.




# 14. Pievieno property un setter, kas neļauj negatīvu vērtību.




# 15. Pārbaudi, kas notiek, mēģinot piešķirt nederīgu vērtību.




# 16. ★ Uzraksti klasi, kurā viens atribūts tiek aprēķināts no citiem un tāpēc ir tikai lasāms.





# ----------------------------------------------------------
# 12-005 · Sprints: klase ar validāciju
# ----------------------------------------------------------

# 17. Izstrādā klasi Lidojums ar atribūtiem numurs, galamerkis, vietu_skaits,
#    rezervetas_vietas. Visai validācijai jābūt klasē: numurs nedrīkst būt tukšs, vietu
#    skaitam jābūt pozitīvam, rezervēto vietu skaits nedrīkst pārsniegt kopējo.




# 18. Pievieno metodes rezervet(skaits), atcelt(skaits) un brivas_vietas().




# 19. Uzraksti vismaz sešus pārbaudes gadījumus, tostarp trīs nederīgus, un pieraksti
#    rezultātus komentārā.




# 20. ★ Pievieno property, kas atgriež aizpildījumu procentos.





# ----------------------------------------------------------
# 12-006 · Sprints: refleksija
# ----------------------------------------------------------

# 21. Pieraksti piezimes.md, kura validācija bija visgrūtākā un kāpēc.




# 22. Salīdzini savu risinājumu ar klasesbiedra risinājumu repozitorijā un pieraksti vienu
#    lietu, ko viņš izdarīja labāk.




# 23. ★ Pārraksti vienu savas klases metodi tā, lai tā būtu īsāka vai skaidrāka.





# ----------------------------------------------------------
# 12-007 · Mantošana
# ----------------------------------------------------------

# 24. Izveido virsklasi Transportlidzeklis un apakšklases Automasina un Velosipeds.

class Transportlidzeklis:
    def __init__(self, marka, gads):
        self.marka = marka
        self.gads = gads

    def apraksts(self):
        return f"{self.marka} ({self.gads})"

    def parvietojas(self):
        return "parvietojas"


class Automasina(Transportlidzeklis):
    def __init__(self, marka, gads, degviela):
        super().__init__(marka, gads)      # virsklases konstruktors
        self.degviela = degviela

    def parvietojas(self):                 # pārraksta virsklases metodi
        return "brauc pa celu"


class Velosipeds(Transportlidzeklis):
    def parvietojas(self):
        return "brauc ar kajam"

# 25. Katrai apakšklasei pievieno savu metodi un pārrakstītu virsklases metodi.




# 26. Izveido objektu sarakstu ar dažādu apakšklašu objektiem un apstaigā to ar ciklu.

# a = Transportlidzeklis("Bolt Skūteris", "2025")
# b = Automasina("Porsche", "2000", "dīzelis")
# c = Velosipeds("Cube", "2018")

# saraksts = [a, b, c]

# for t in saraksts:
#     print(t.parvietojas())

# 27. ★ Izveido trīs līmeņu hierarhiju un pieraksti, kāpēc tā parasti ir slikta ideja.



# ----------------------------------------------------------
# 12-008 · Polimorfisms
# ----------------------------------------------------------

# 28. Izveido klases Kvadrats, Rinkis, Trijsturis, katrai ar metodi laukums().

class Kvadrats:
    def __init__(self, mala):
        self.a = mala

    def laukums(self):
        return self.a ** 2

class Rinkis:
    def __init__(self, radiuss):
        self.r = radiuss

    def laukums(self):
        return round(3.14159265 * self.r ** 2, 2)

class Trijsturis:
    def __init__(self, pamats, augstums):
        self.a = pamats
        self.h = augstums

    def laukums(self):
        return round((self.a * self.h) / 2, 2)

# 29. Uzraksti funkciju, kas saņem figūru sarakstu un atgriež kopējo laukumu.

def laukumu_summa(saraksts):
    summa = 0

    for figura in saraksts:
        summa += figura.laukums()

    return summa

kv = Kvadrats(4)
tr = Trijsturis(7, 3)
ri = Rinkis(6)

sar = [kv, tr, ri]
print(laukumu_summa(sar))

# 30. Papildini programmu ar jaunu figūru, nemainot funkciju.


# 31. Pieraksti, kāpēc 30. uzdevumā funkcija nebija jāmaina — tā ir polimorfisma jēga.


# 32. ★ Uzraksti funkciju, kas darbojas ar jebkuru objektu, kuram ir metode apraksts(),
#    neatkarīgi no klases.


# ----------------------------------------------------------
# 12-009 · Abstrakcija
# ----------------------------------------------------------

# 33. Pārveido Figura par abstraktu klasi ar abstraktu metodi laukums().
from abc import ABC, abstractmethod

class Figura(ABC): # Abstract Base Class
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    @abstractmethod
    def laukums(self):
        """Katrai figūrai savs aprēķins."""

    def apraksts(self):
        return f"{self.nosaukums}: {self.laukums():.2f}"


# 34. Pārbaudi, kas notiek, mēģinot izveidot abstraktās klases objektu.

# fig = Figura() # nestrādā

# 35. Pārbaudi, kas notiek, ja apakšklase abstrakto metodi nerealizē.

class Kvadrats(Figura):
    def __init__(self, mala):
        super().__init__("kvadrats")
        self.mala = mala

# k = Kvadrats(9)

# 36. ★ Pieraksti, ar ko abstrakcija atšķiras no iekapsulēšanas. Eksāmenā šie jēdzieni ir
#    jāatšķir.

# ----------------------------------------------------------
# 12-010 · Praktikums: četri principi
# ----------------------------------------------------------

# 37. Izstrādā bibliotēkas sistēmas klases: abstrakta Vienums ar apakšklasēm Gramata,
#    Zurnals, DVD. Katrai sava apraksts() un izsniegsanas_termins().
from datetime import datetime, timedelta

class Vienums(ABC):
    def __init__(self, nosaukums, _izsniegts=0):
        self.nosaukums = nosaukums
        self.sanemts = datetime.now()
        self.izsniegts = _izsniegts

    @property
    def izsniegts(self):
        return self._izsniegts

    @izsniegts.setter
    def izsniegts(self, value):
        if value < 0:
            raise ValueError("Izsniegto vienumu skaits nevar būt negatīvs.")
        self._izsniegts = value
    @abstractmethod
    def apraksts(self):
        """Katrai mantojošai klasei būs atšķirīgi aprakstošie dati"""

    def izsniegsanas_termins(self):
        return self.sanemts + timedelta(days=14)

class Gramata(Vienums):
    def __init__(self, nosaukums, autors, lpp):
        super().__init__(nosaukums)
        self.autors = autors
        self.lpp = lpp

    def apraksts(self):
        return f"{self.nosaukums} ({self.autors}, {self.lpp} lpp.)"

class DVD(Vienums):
    def __init__(self, nosaukums, gads, rezisors):
        super().__init__(nosaukums)
        self.gads = gads
        self.rezisors = rezisors

    def apraksts(self):
        return f"{self.rezisors} - {self.nosaukums} ({self.gads})"

    def izsniegsanas_termins(self):
        return self.sanemts + timedelta(days=5)

class Zurnals(Vienums):
    def __init__(self, nosaukums, periods, gads):
        super().__init__(nosaukums)
        self.periods = periods
        self.gads = gads

    def apraksts(self):
        return f"{self.nosaukums} ({self.gads}. gada {self.periods})"

g = Gramata("Uguns un nakts", "Rainis", 132)
m = DVD("The Odyssey", 2026, "C. Nolan")
z = Zurnals("Pie galda!", "jūlijs-augusts", 2026)


# 38. Uzraksti funkciju, kas apstaigā vienumu sarakstu un izvada visu aprakstus.


for vienums in [g, m, z]:
    print(vienums.apraksts())


# 39. ★ Pievieno iekapsulētu skaitītāju, cik reižu vienums izsniegts. 
#       Izstrādāt funkcionalitāti, kas seko līdzi isniegšanai un saņemšanai.



# ----------------------------------------------------------
# 12-011 · Sprints: klašu hierarhija
# ----------------------------------------------------------

# 40. Dotajam aprakstam «skolas inventāra uzskaite» izprojektē klašu hierarhiju: kas ir
#    virsklase, kas apakšklases, kas abstrakts.

class Inventars(ABC):
    def __init__(self, nosaukums, iegades_gads, _skaits=0):
        self.nosaukums = nosaukums
        self.iegades_gads = iegades_gads
        self._skaits = _skaits

    @property
    def skaits(self):
        return self._skaits

    @skaits.setter
    def skaits(self, value):
        if value < 0:
            raise ValueError("Skaits nevar būt negatīvs.")
        self._skaits = value
    
    @abstractmethod
    def apraksts(self):
        """Katrai mantojošai klasei būs atšķirīgi aprakstošie dati"""

class Kresls(Inventars):
    def __init__(self, nosaukums, iegades_gads, _skaits=0):
        super().__init__(nosaukums, iegades_gads, _skaits)

    def apraksts(self):
        return f"{self.nosaukums} ({self.iegades_gads}), katram skolēnam savs."

# 41. Realizē to kodā, izmantojot visus četrus OOP principus.




# 42. Uzraksti programmu, kas demonstrē katru principu, un komentārā norādi, kur tas ir.




# 43. ★ Uzzīmē klašu diagrammu un ieliec to repozitorijā.





# ----------------------------------------------------------
# 12-012 · Sprints: koda pārskatīšana
# ----------------------------------------------------------

# 44. Pārskati klasesbiedra 12-011 risinājumu un uzraksti trīs konkrētas piezīmes.




# 45. Atrodi vienu vietu, kur mantošana lietota tur, kur nevajadzēja, vai otrādi.




# 46. ★ Piedāvā konkrētu labojumu koda fragmenta veidā.





# ----------------------------------------------------------
# 12-013 · Standarta bibliotēka
# ----------------------------------------------------------

# 47. Ar collections.Counter saskaiti burtu biežumu un salīdzini ar savu ciklu.




# 48. Ar collections.defaultdict pārraksti grupēšanas uzdevumu.




# 49. Ar pathlib uzraksti programmu, kas uzskaita visas .py datnes katalogā.




# 50. Atrodi dokumentācijā vienu itertools funkciju un pieraksti tās lietojuma piemēru.




# 51. ★ Atrodi standarta bibliotēkas moduli, ko vari izmantot savā projektā, un pamato izvēli.





# ----------------------------------------------------------
# 12-014 · Ārējās bibliotēkas
# ----------------------------------------------------------

# 52. Uzstādi bibliotēku virtuālajā vidē un izveido requirements.txt.




# 53. Izvērtē trīs bibliotēkas pēc četriem kritērijiem un aizpildi salīdzinājuma tabulu.




# 54. Pieraksti, kādi riski rodas, pievienojot projektam svešu bibliotēku.




# 55. ★ Noskaidro, cik atkarību ievelk viena tava izvēlētā bibliotēka.





# ----------------------------------------------------------
# 12-015 · Grafiskā saskarne: pamati
# ----------------------------------------------------------

# 56. Izveido logu ar virsrakstu, vienu ievades lauku un pogu.




# 57. Pievieno otru lauku un sakārto elementus režģī.




# 58. Pievieno teksta lauku rezultāta izvadīšanai.




# 59. ★ Pievieno logam izvēlni ar diviem punktiem.





# ----------------------------------------------------------
# 12-016 · Grafiskā saskarne: notikumi
# ----------------------------------------------------------

# 60. Panāc, lai poga nolasa ievadi un izvada rezultātu logā.




# 61. Pievieno validāciju: nederīgas ievades gadījumā parādi paziņojumu, nevis avarē.




# 62. Savieno saskarni ar savu 12-002 klasi Rezervacija.




# 63. ★ Pievieno pogu, kas notīra visus laukus.





# ----------------------------------------------------------
# 12-017 · Sprints: saskarne un klase kopā
# ----------------------------------------------------------

# 64. Izveido grafisku saskarni savai 12-005 klasei Lidojums: rezervēšana, atcelšana,
#    brīvo vietu rādīšana.




# 65. Visai validācijai jāpaliek klasē; saskarne tikai rāda rezultātu.




# 66. ★ Pievieno sarakstu ar visiem lidojumiem un iespēju izvēlēties.





# ----------------------------------------------------------
# 12-018 · Sprints: refleksija un uzlabojumi
# ----------------------------------------------------------

# 67. Pārbaudi savu kodu: vai saskarnes failā ir aprēķini, kuriem tur nav vietas?




# 68. Pārcel tos uz klasi un pārbaudi, ka viss joprojām strādā.




# 69. ★ Pieraksti, kāpēc loģikas atdalīšana no saskarnes atvieglo testēšanu.





# ----------------------------------------------------------
# 12-019 · Datu glabāšana
# ----------------------------------------------------------

# 70. Pievieno savai klasei metodi uzvardnicu() un klases metodi novardnicas().




# 71. Saglabā objektu sarakstu JSON datnē un ielasi to atpakaļ.




# 72. Pievieno programmai automātisku saglabāšanu pēc katras izmaiņas.




# 73. ★ Apstrādā gadījumu, kad datne ir bojāta vai tukša.





# ----------------------------------------------------------
# 12-020 · Izņēmumi
# ----------------------------------------------------------

# 74. Pievieno savai klasei izņēmumu, ko tā met nederīgas darbības gadījumā.




# 75. Definē savu izņēmuma klasi, kas manto Exception.




# 76. Apstrādā to programmā un parādi lietotājam saprotamu paziņojumu.




# 77. ★ Pieraksti, kad labāk atgriezt False un kad — mest izņēmumu.





# ----------------------------------------------------------
# 12-021 · Jēdzieni un atkārtojums
# ----------------------------------------------------------

# 78. Burtnīcā: paskaidro katru no četriem principiem vienā teikumā un dod piemēru.




# 79. Burtnīcā: dotajam koda fragmentam nosaki, kurš princips tajā izmantots.




# 80. ★ Burtnīcā: uzraksti klases definīciju ar roku pēc dota apraksta.





# ----------------------------------------------------------
# 12-022 · SV1 uzdevuma izsniegšana
# ----------------------------------------------------------

# 81. Izlasi SV1 specifikāciju un uzraksti savu izpildes plānu.




# 82. Pieraksti, kura prasība tev šķiet grūtākā, un kā to risināsi.




# 83. ★ Izplāno savu klašu hierarhiju uz papīra pirms koda rakstīšanas.





# ----------------------------------------------------------
# 12-023 · Sprints: SV1 klašu modelis
# ----------------------------------------------------------

# 84. Realizē savu klašu hierarhiju ar konstruktoriem un validāciju.




# 85. Pārbaudi katru klasi atsevišķi, pirms taisi saskarni.




# 86. ★ Pievieno vismaz vienu abstraktu metodi vai property, ja specifikācija to pieļauj.





# ----------------------------------------------------------
# 12-024 · Sprints: datu glabāšana
# ----------------------------------------------------------

# 87. Pievieno metodes uzvardnicu() un novardnicas().




# 88. Realizē saglabāšanu un ielasīšanu; pārbaudi ar restartētu programmu.




# 89. Pieraksti piezimes.md, kur iestrēgi, lai nākamajā klātienes stundā to atrisinātu ātri.




# 90. ★ Apstrādā gadījumu, kad datne ir bojāta vai tukša.





# ----------------------------------------------------------
# 12-025 · SV1 izstrāde: saskarne
# ----------------------------------------------------------

# 91. Izveido saskarni ar visiem specifikācijā prasītajiem elementiem.




# 92. Panāc, lai visa validācija paliek klasēs, ne saskarnes funkcijās.




# 93. ★ Pievieno saskarnei ārējās bibliotēkas funkcionalitāti, ja specifikācija to prasa.





# ----------------------------------------------------------
# 12-026 · SV1 izstrāde: pabeigšana un pašpārbaude
# ----------------------------------------------------------

# 94. Aizpildi pašpārbaudes tabulu: katrai prasībai statuss un vieta kodā.




# 95. Notestē programmu ar nederīgiem datiem un pieraksti rezultātus.




# 96. ★ Sakārto kodu: nosaukumi, komentāri, liekā koda izmešana.
