1. **Sukurkite DataFrame su bent 5 eilutėmis ir 3 stulpeliaiskur vienas iš stulpelių būtų temperatūra**

2. -- •Atspausdinkite antrą ir ketvirtą eilutę iš DataFrame
3. -- •Atspausdinkite visas eilutes,kuriose temperatūra yra neigiama
4. -- •Apskaičiuokite ir atspausdinkite bendrą temperatūrų sumą
5. -- •Pridėkite naują stulpelį "Vėjas" su atsitiktinėmis reikšmėmis
6. -- •Pridėkite stulpelį "Peršalimo Rizika" su reikšme "Taip" visoms eilutėms, kuriose temperatūra mažesnė nei 0.
7. -- •Pakeiskite "Vėjas" stulpelio reikšmes į didžiosiomis raidėmis parašytą "Silpnas", "Vidutinis" arba "Stiprus", priklausomai nuo reikšmės (mažiau nei 10, nuo 10 iki 20, daugiau nei 20) (hint use apply).
8. -- •Sugrupuokite duomenis pagal "Peršalimo Rizika" ir apskaičiuokite vidutinę temperatūrą kiekvienai grupei
9. -- •Surikiuokite Data Frame pagal "Temperatūra" stulpelį mažėjančia tvarka
10. -- •Sujunkite du DataFrame objektus (vieną su datomis ir temperatūromis, kitą su datomis ir vėjo stiprumu) pagal bendrą raktą ("Data") (gali būti indeksas, tuomet naudokite, join metodą, join yra, kaip merge tik su indeksu).

**Parsisiųskite duomenų rinkinį iš šios nuorodos https://www.kaggle.com/competitions/titanic/data?select=train.csv**

1. -- •Padėkite ji į savo projekto aplanką ar kitoje vietoje ir užkraukite jį kaip dataframe
2. -- •Sutvarkykite trūkstamas reikšmes savo nuožiūra (trūkstamas reikšmes rasti jau mokate) (turi nelikti nei vienos trūkstamos reikšmės).
3. •Sukurkite bendrą stulpelį susumavę brolius seseris ir tėvus, kad sužinotumėte šeimos dydį, senus stulpelius galite pašalinti (Parchir SibSp).
4. •Įsiaiškinkite, ar žmonės keliavo vieni ar ne (naujas stulpelis IsAlone).
5. •Sukurkite naują stulpelį, kuris sugrupuos asmenis pagal amžių į grupes ( <18 vaikas, < 65 suauges, > 65 senjoras)
6. •Suskaičiuokite vidutinį kiekvienos klasės keleivių amžių.
7. •Pamėginkite įsiaiškinti, ar bilieto kaina, turėjo įtakos išgyvenamumui.

**•Advanced** 8. Pažiūrėkite, kaip koreliuoja vieni stulpeliai su kitais (galite naudoti bibliotekas arba yra net df.corr())
