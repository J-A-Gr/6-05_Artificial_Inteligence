**PART 1**

✔ Sukurkite 1D masyvą iš sąrašo [1, 2, 3, 4, 5].
✔ Sukurkite 2D masyvą 3x3 dydžio su nuliais.

✔ Sukurkite 2D masyvą iš [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
✔ Gaukite elementą esantį antrame stulpelyje pirmoje eilutėje.
✔ Išpjaukite (slice) pirmas dvi eilutes ir antrą bei trečią stulpelį.

✔ Sukurkite du 1D masyvus: [1, 2, 3] ir [4, 5, 6].
✔ Atlikite sudėties, atimties, daugybos ir dalybos operacijas.
✔ Apskaičiuokite sumą, vidurkį, maksimumą ir minimumą.

✔ Sukurkite masyvą su reikšmėmis [0, π/2, π].
✔ Apskaičiuokite sin, cos, tan kiekvienai reikšmei.
✔ Apskaičiuokite eksponentes ir natūralius logaritmus kiekvienai reikšmei.

✔ Sukurkite 3x3 masyvą su atsitiktinėmis reikšmėmis tarp 0 ir 1.
✔ Padidinkite kiekvieną reikšmę masyve dvigubai.

**PART 2**

**Užduotis yra sukurti atsitiktinius orų duomenis naudojant numpy ir apskaičiuoti įvairias metrikas:**

✔ Sugeneruokite miesto orų temperatūras vieniems metams (pvz 2024-01-01: -15, 2024-01-02: -17 ir tt) Rekomenduojama generuoti kiekvieną mėnesį atskirai
✔Įterpkite anomalijų pvz sausį temperatūra pasiekia +10 laipsnių arba staiga pakinta nuo -15 iki -35) Suskaičiuokite mėnesio vidutines temperatūras
✔ Naudodami NumPy suraskite šias anomalijas, galite naudoti įvairias technikas (rekomendacija naudoti standartinį nuokrypi)

**Advanced (neturintiems ką veikti)**
Pamėginkite atvaizduoti visų metų temperatūra naudodami matplotlib, anomalijas paryškinkite kita spalva.

✔ **3 skaidrė**

Sukurkite NumPymasyvą, kuriame saugomi komandos žaidėjų rezultatai (pvz., surinktų taškų kiekis kiekviename rungtynių etape).
•Naudokite operacijas, kad suskaičiuotumėte bendrą komandos rezultatą, vidurkį bei surastumėte geriausią žaidėją.

•Galite išplėsti užduotį – vizualizuokite rezultatus su „matplotlib“.

_Patarimai:_
•Naudokite np.array() duomenų struktūros sukūrimui.
•Apskaičiuokite vidurkį su np.mean(), sumą su np.sum(), o geriausią rezultatą su np.max() arba np.argmax().

✔ **4 skaidrė**

Naudodami np.arange(), sukurkite masyvą, kuriame būtų skaičiai nuo 0 iki 9.
Iš šio masyvo išrinkite pirmuosius 5 skaičius ir paskutinius 3 skaičius naudodami slicing.
_Patarimai:_
np.arange(10) sukurs masyvą nuo 0 iki 9.
Slicingsintaksė: array[:5] pirmiesiems 5 elementams, array[-3:] paskutiniams 3.

**5 skaidrė**

Sukurkite vienmačio masyvą, kuriame saugomos skirtingų prekių kainos (pvz., [3.50, 7.99, 2.99, 12.50, 5.00]).
Apskaičiuokite bendrą kainų sumą ir vidutinę prekių kainą.
Papildomai, apskaičiuokite, kiek kiekvienos prekės kaina padidės, jei prie jos pridėsime 10% mokesčio.

_Patarimai:_
Bendram sumos apskaičiavimui – np.sum().
Vidurkiui – np.mean().
Elementų padidinimui: naudokite aritmetines operacijas (pvz., prices\* 1.10).
