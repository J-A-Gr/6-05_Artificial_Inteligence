Supaprastintas Titanikas:

Išmeskite visus stulpelius, kurie yra nereikalingi. iš titaniko duomenų rinkinio:
sns.load_dataset("titanic")

Sutvarkykite duomenis, kad tiktų logistinei regresijai. Svarbu nepalikti pasikartojančio target stulpekio, pvz yra IsAlive (kurio reikšmės yra identiškos Survived, šitą privaloma išmesti). Atlikite ant jo treniravimą ir pamėginkite gauti kuo aukštesnius accuracy rezultatus su testavimo duomenimis. Nepamirškite visų žingsnių, tokių, kaip duomenų sutvarkymas, logistinė regresija negali dirbti su tekstiniais duomenimis, dėl to reikės arba išmesti arba paversti į skaičius (pvz Male/Female -> 0/1. Nerekomenduojama versti į skaičius, jeigu yra daugiau nei dvi reikšmės pvz uostas S/Q/C neturėtų virsti į 0/1/2, šiandienai juos geriau tiesiog išmesti, o kitą dieną išmoksite, kaip susitvarkyti).
