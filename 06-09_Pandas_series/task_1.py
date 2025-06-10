import pandas as pd
import numpy as np

class SerijosAnalize:
    def __init__(self, data):
        self.s = pd.Series(data)

    def serijos_dydis_tipas(self):  
        print(self.s)

    def penktas_elementas_is_serijos(self):
        print(self.s[4]) # iprasti naudoti iloc

    def visi_isskyrus_pirma_paskutini(self):
        print(self.s[1:-1])

    def sk_didesnis_nei_ivestas(self, skaicius):
        rezultatas = self.s[self.s > skaicius]
        # print(f"Skaičiai didesni nei {skaicius}:\n{rezultatas.dropna()}")  
        print(rezultatas)
        return rezultatas
        # print(f"Skaičiai didesni nei {ivestas}:\n{rezultatas.dropna().tolist()}") 
        '''combo wombo dropna ir tolist del svaraus listo
        dropna pasalina NaN (grazina False), tolist grazina python sarasa, del patogumo. '''

    def serijos_suma(self):
        suma = self.s.sum()
        print(suma)

    def serijos_vidurkis(self):
        vidurkis = self.s.mean()
        print(f"{vidurkis:.2f}")

    def apply_funkcija_is_2(self):
        a = self.s.apply(lambda x: x *2)
        print(a)


analize = SerijosAnalize([0, 10, 20, 30, np.nan, 50, 60, 70, np.nan, 90, 100])
# analize.serijos_dydis_tipas()
# analize.penktas_elementas_is_serijos()
# analize.visi_isskyrus_pirma_paskutini()
# analize.sk_didesnis_nei_ivestas(60)
# analize.serijos_suma()
# analize.serijos_vidurkis()
# analize.apply_funkcija_is_2()

class ZodziuSerija:
    def __init__(self, data):
        self.s = pd.Series(data)
    
    def pasalinimas_none(self):
        a = self.s.dropna()
        print (a)
    
    def reiksmiu_didziosios_raides(self):
        a = self.s.str.upper().dropna()
        print(a)

    def zodziu_pasikartojimas(self):
        a = self.s.value_counts()
        print(a)

    def reiksmes_mazejancia_tvarka(self):
        a = self.s.sort_values(ascending=False).dropna()
        print(a)

    
z_analize = ZodziuSerija(["Liūtis", "Audra", np.nan, "Liūtis", None, "Škvalas", "Cunamis", None, "Saulėta", "Cunamis"])
# z_analize.pasalinimas_none()
# z_analize.reiksmiu_didziosios_raides()
# z_analize.zodziu_pasikartojimas()
z_analize.reiksmes_mazejancia_tvarka()