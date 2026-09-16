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

#I ain't green enough

# 2. Uzraksti klasi Prece ar konstruktoru un divām metodēm — bez ieskatīšanās vecajā kodā.
# class Prece:
#     def __init__(self, nosaukums, cena, kategorija):
#         self.nosaukums = nosaukums
#         self.cena = cena
#         self.kategorija = kategorija

#     def info(self):
#         return f"\"{self.nosaukums}\" ir prece kategorijā \"{self.kategorija}\", kura maksā {self.cena} eiro."

#     def akcija(self, procenti):
#         return round(self.cena * (1-(procenti/100)), 2)


# bpk = Prece("Burvīgais piena kartupelis", 5.7, "piena produkti")
# ssbb = Prece("Slavenā, slapjā beisbola bumba", 110.37, "sports")
# mva = Prece("Maize: vienmēr akcijā!", 10, "maize un kondetorejas produkti")

# print(bpk.info(), f"Tagad tā maksā {bpk.akcija(20)} eiro ar 20% atlaidi!")
# print(ssbb.info())
# print(mva.info(), f"Tagad tā maksā {mva.akcija(80)} eiro ar 80% atlaidi!")
#alt+shift+↓ = copy downwards


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
class Lidojums:
    def __init__(self, numurs, galamerkis, _rezervetas_vietas=0, vietu_skaits=100):
        self.numurs = numurs
        self.galamerkis = galamerkis
        self.vietu_skaits = vietu_skaits
        self._rezervetas_vietas = _rezervetas_vietas
        self._aizpildijums = (self.rezervetas_vietas/self.vietu_skaits)*100

    @property
    def aizpildijums(self):
        return self._aizpildijums
    
    @property
    def rezervetas_vietas(self):
        return self._rezervetas_vietas
    @rezervetas_vietas.setter
    def rezervetas_vietas(self, rezervets):
        if rezervets > self.vietu_skaits:
            raise ValueError("Rezerveto vietu skaits nevar būt lielāks par vietu skaitu.")
        else:
            self._rezervetas_vietas = rezervets
    @property
    def numurs(self):
        return self.numurs
    @numurs.setter
    def numurs(self, num):
        if num <= 0:
            raise ValueError("Numurs nevar būt mazāks par 1.")
    def rezervet(self, skaits):
        self.rezervetas_vietas += skaits

    def atcelt(self, skaits):
        self.rezervetas_vietas -= skaits

    def brivas_vietas(self):
        return self.vietu_skaits - self.rezervetas_vietas
    
    
    @classmethod
    def no_rindas(cls, rinda):
        """Izveido objektu no CSV rindas: BT101,Riga,180"""
        lauki = rinda.strip().split(",")
        return cls(lauki[0], lauki[1], int(lauki[2]))

    @classmethod
    def tuksa(cls):
        """Izveido tukšu lidojumu ar noklusējuma vērtībām."""
        return cls("---", "nav noteikts")

# lid = Lidojums(1, "France", 10, 40)
# print(lid.aizpildijums)

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
        return "pārvietojas"

class Automasina(Transportlidzeklis):
    def __init__(self, marka, gads, tips):
        super().__init__(marka, gads)
        self.tips = tips

    def parvietojas(self):
        return "brauc pa ceļu"

class Velosipeds(Transportlidzeklis):
    def parvietojas(self):
        return "brauc ar kājām"

class Unicikls(Transportlidzeklis):
    def __init__(self, marka, gads, tophats=1):
        super().__init__(marka, gads)
        self.tophats = tophats

    def parvietojas(self):
        return "brauc izsmalcināti"



# 25. Katrai apakšklasei pievieno savu metodi un pārrakstītu virsklases metodi.




# 26. Izveido objektu sarakstu ar dažādu apakšklašu objektiem un apstaigā to ar ciklu.
# deer = Automasina("Burguntruck", 2023, "benzīns")
# mick = Unicikls("One", 1816, 180)
# divi = Velosipeds("Twowheezer", 2)
# da = Transportlidzeklis("Okarun", 16)

# list = [deer, divi, mick, da]

# for l in list:
#     print(l.apraksts() + ", ar to " + l.parvietojas())



# 27. ★ Izveido trīs līmeņu hierarhiju un pieraksti, kāpēc tā parasti ir slikta ideja.





# ----------------------------------------------------------
# 12-008 · Polimorfisms
# ----------------------------------------------------------

# 28. Izveido klases Kvadrats, Rinkis, Trijsturis, katrai ar metodi laukums().
# class Kvadrats:
#     def __init__(self, mala):
#         self.mala = mala

#     def laukums(self):
#         return (self.mala*self.mala)

# class Rinkis:
#     def __init__(self, r):
#         self.r = r

#     def laukums(self):
#         return (3.14159265359*(self.r**2))

# class Trijsturis:
#     def __init__(self, pamats, augstums):
#         self.pamats = pamats
#         self.augstums = augstums

#     def laukums(self):
#         return (self.pamats * self.augstums)/2
        
# class Oktagons:
#     def __init__(self, mala):
#         self.mala = mala

#     def laukums(self):
#         return 2*(1+(2**0.5))*(self.mala**2)


# 29. Uzraksti funkciju, kas saņem figūru sarakstu un atgriež kopējo laukumu.
# sq = Kvadrats(5)
# cir = Rinkis(6)
# tri = Trijsturis(6, 5)
# hajime = Oktagons(7)

# def kopejs_s(figuras):
#     # return sum(figura.laukums() for figura in figuras)
#     sum = 0
#     for f in figuras:
#         sum += f.laukums()
#     return sum

# shaps = [sq, cir, tri, hajime]
# print(kopejs_s(shaps))
# 30. Papildini programmu ar jaunu figūru, nemainot funkciju.




# 31. Pieraksti, kāpēc 30. uzdevumā funkcija nebija jāmaina — tā ir polimorfisma jēga.




# 32. ★ Uzraksti funkciju, kas darbojas ar jebkuru objektu, kuram ir metode apraksts(),
#    neatkarīgi no klases.

def turbo(obj):
    if "Okarun" in obj.apraksts():
        return True
    else:
        return False



# ----------------------------------------------------------
# 12-009 · Abstrakcija
# ----------------------------------------------------------

# 33. Pārveido Figura par abstraktu klasi ar abstraktu metodi laukums().

from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    @abstractmethod
    def laukums(self):
        """Katram savs laukuma aprēķins"""

    def apraksts(self):
        return f"{self.nosaukums}: {self.laukums():.2f}"

class Kvadrats(Figura):
    def __init__(self, mala):
        super().__init__("kvadrats")
        self.mala = mala

    def laukums(self):
        return (self.mala*self.mala)

class Rinkis(Figura):
    def __init__(self, r):
        super().__init__("riņķis")
        self.r = r

    def laukums(self):
        return (3.14159265359*(self.r**2))

# square = Kvadrats(5)
# aple = Rinkis(6)
# print(f"{square.apraksts()}\n{aple.apraksts()}")

# 34. Pārbaudi, kas notiek, mēģinot izveidot abstraktās klases objektu.

# fig = Figura("johg") # DON'T WORK!!!!!



# 35. Pārbaudi, kas notiek, ja apakšklase abstrakto metodi nerealizē.

# uznāk error!!
# class Oktagons(Figura):
#     def __init__(self, mala):
#         super().__init__("hajime")
#         self.mala = mala

# ha = Oktagons(4)
#TypeError: Can't instantiate abstract class Oktagons with abstract method laukums


# 36. ★ Pieraksti, ar ko abstrakcija atšķiras no iekapsulēšanas. Eksāmenā šie jēdzieni ir
#    jāatšķir.

#abstrakcija ierobežo, kādām metodēm jābūt apakšklasēm, iekapsulēšanā tur datus un darbības kopā



# ----------------------------------------------------------
# 12-010 · Praktikums: četri principi
# ----------------------------------------------------------

# 37. Izstrādā bibliotēkas sistēmas klases: abstrakta Vienums ar apakšklasēm Gramata,
#    Zurnals, DVD. Katrai sava apraksts() un izsniegsanas_termins().
# from datetime import datetime, timedelta
# class Vienums(ABC):
#     def __init__(self, nosaukums, gads, _izsniegsanas_reizes = 0, izsniegsana = 0):
#         self.nosaukums = nosaukums
#         self.gads = gads
#         self.sanemts = datetime.now()
#         self._izsniegsana = izsniegsana
#         self._izsniegsanas_reizes = _izsniegsanas_reizes

#     @property
#     def izsniegsana(self):
#         return f"Vienums ir izsniegts {self._izsniegsana} reizes."

#     @izsniegsana.setter
#     def izsniegsana(self, reizes):
#         if reizes < 0:
#             raise ValueError("Vienums nevar būt izsniegts mazāk par nevienu reizi.")
#         self._izsniegsana = reizes
#         self.izsniegsanas_reizes += 1
#     @property
#     def izsniegsanas_reizes(self):
#         return self.izsniegsanas_reizes
#     @abstractmethod
#     def apraksts(self):
#         """apraksti pats omfg"""
    
#     def izsniegsanas_termins(self):
#         return (self.sanemts + timedelta(weeks=4))

       
# class Gramata(Vienums):
#     def __init__(self, nosaukums, gads, autors):
#         super().__init__(nosaukums, gads)
#         self.autors = autors

#     def apraksts(self):
#         return f"\"{self.nosaukums}\" ir {self.gads}. gada grāmata, kuru uzrakstīja {self.autors}."

# class Zurnals(Vienums):
#     def __init__(self, nosaukums, gads, redaktors):
#         super().__init__(nosaukums, gads)
#         self.redaktors = redaktors

#     def apraksts(self):
#         return f"\"{self.nosaukums}\" ir žurnāls, kurš izdots {self.gads}. gadā. Tā redaktors/-e ir {self.redaktors}."

# class DVD(Vienums):
#     def __init__(self, nosaukums, gads, garums, rezisors):
#         super().__init__(nosaukums, gads)
#         self.garums = garums
#         self.rezisors = rezisors

#     def apraksts(self):
#         return f"\"{self.nosaukums}\" ir veidots {self.gads}. gadā, režisors - {self.rezisors}. DVD ir {self.garums}h garš."

# ca = Gramata("Old Possum's Book of Practical Cats", 1939, "T.S. Eliot")
# catsstage = DVD("CATS", 1998, 2, "David Mallet")
# zur = Zurnals("Cats - What ARE They????", 2026, "Varik")
# # 38. Uzraksti funkciju, kas apstaigā vienumu sarakstu un izvada visu aprakstus.
# vienumi = [ca, catsstage, zur]

# def desc(list):
#     for vien in vienumi:
#         print(vien.apraksts())

# desc(vienumi)

# print(ca.izsniegsanas_termins())

# 39. ★ Pievieno iekapsulētu skaitītāju, cik reižu vienums izsniegts.

# FV 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Maksajums(ABC):
    def __init__(self, vajag, dota):
        self.vajag = vajag
        self.dota = dota
        self.atlikums = vajag - dota

    @abstractmethod
    def komisija(self):
        """aprēķini pats..."""

class KartesMaksajums(Maksajums):
    def __init__(self, vajag, dota):
        super().__init__(vajag, dota)

    def komisija(self):
        return round(self.vajag * 0.015, 2)

class SkaidraNauda(Maksajums):
    def __init__(self, vajag, dota):
        super().__init__(vajag, dota)

    def komisija(self):
        return 0

def kopeja_komisija(maksajumi):
    kops = 0
    for maksajums in maksajumi:
        kops += maksajums.komisija()

    return kops

mak = KartesMaksajums(25.05, 30)
wue = SkaidraNauda(55.5, 100)
pur = [mak, wue]
print(kopeja_komisija(pur))

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
        """EVERY MAN FOR HIMSELF!!"""

class Kresls(Inventars):
    def __init__(self, nosaukums, iegades_gads, _legs, _skaits=0):
        super().__init__(nosaukums, iegades_gads, _skaits)
        self._legs =_legs

    def klase_vel(self, klases):
        needed = klases*31
        if needed > self._skaits:
            return needed - self._skaits
        else:
            return 0

    @property
    def legs(self):
        return self._skaits

    @legs.setter
    def legs(self, value):
        if value < 0:
            raise ValueError("Skaits nevar būt negatīvs.")
        self._legs = value

    def apraksts(self):
        return "Sēdi."
    
class Gramata(Inventars):
    def __init__(self, nosaukums, iegades_gads, _lpp, _skaits=0):
        super().__init__(nosaukums, iegades_gads, _skaits)
        self._lpp = _lpp

    def klase_vel(self, klases):
            needed = klases*95
            if needed > self._skaits + 5:
                return needed - self._skaits
            else:
                return 5
    @property
    def lpp(self):
        return self._lpp
    @property
    def skaits(self):
        return self._skaits
    @skaits.setter
    def skaits(self, sk):
        self._skaits = sk
    def apraksts(self):
        return "Lasi."

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
# from collections import Counter
# text = input("--> ")
# print(Counter(text))
# # letters = {}
# for t in text.lower():
#     if t in letters.keys():
#         letters[t] += 1
#     else:
#         letters[t] = 1

# print(letters)


# 48. Ar collections.defaultdict pārraksti grupēšanas uzdevumu.




# 49. Ar pathlib uzraksti programmu, kas uzskaita visas .py datnes katalogā.
from pathlib import Path
# for datne in Path("./01-oop-un-bibliotekas/uzdevumi.py").glob("*.py"):
#     print(datne.name, datne.stat().st_size)
ue = Path(".")
folders = []
# for dir in ue.iterdir():
    # d = dir
    # while d.is_dir() == True:
    #     for fil in d.iterdir():
    #         if fil.is_dir() == False:
    #             files.append(fil)
    #             break
    #         else: 
    #             folders.append(fil)
    #             d = fil
    #             break
    #     break
def getAllFiles(path):
    files = []
    for directory in path.iterdir():
        if directory.is_dir() and ".git" not in directory.stem:
            files += getAllFiles(directory)
        else:
            files.append(directory)
    return files

for  file in getAllFiles(ue):
    print(file)





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
