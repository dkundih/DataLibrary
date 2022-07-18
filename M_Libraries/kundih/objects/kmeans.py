from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import pandas as pd
import random

class KSrednjeVrijednosti:

    def __init__(self, datoteka, broj_klastera, koordinate):
        self.datoteka = pd.DataFrame(datoteka)
        self.originalna_datoteka = pd.DataFrame(datoteka)
        self.koordinate = koordinate
        self.broj_klastera = broj_klastera # Maksimalno 20.

    def podesi_omjer(self,):
        omjer = MinMaxScaler()
        for col in self.koordinate:
            omjer.fit(self.datoteka[[col]])
            self.datoteka[col] = omjer.transform(self.datoteka[[col]])
        
        return self.datoteka

    def kreiraj_klastere(self,):
        self.ksv = KMeans(n_clusters = self.broj_klastera)
        self.dodjela_klastera = self.ksv.fit_predict(self.datoteka[self.koordinate]) # ispitati
        self.datoteka['Klaster'] = self.dodjela_klastera
        
    def prikaz_datoteke(self):
        return self.datoteka

    def prikaz_centroida(self):
        return self.ksv.cluster_centers_

    def prikaz_grafa(self,):
        x = self.koordinate[0]
        y = self.koordinate[1]
        boje = ['r', 'g', 'b', 'c', 'y', 'k', 'brown', 'wheat', 'maroon', 'grey', 'steelblue', 'peru', 'indigo', 'pink', 'darkkhaki', 'deeppink', 'chocolate', 'rosybrown', 'gold', 'tan']
        brojac = 0
        for i in range(self.broj_klastera):
            klaster = self.datoteka[self.datoteka['Klaster'] == brojac]
            tmp_boja = random.choice(boje)
            plt.scatter(klaster[x], klaster[y], color = tmp_boja)
            boje.remove(tmp_boja)
            brojac += 1
        plt.scatter(self.ksv.cluster_centers_[:, 0], self.ksv.cluster_centers_[:, 1], color = 'm', marker = '*', label = 'centroid')
        plt.title(f'{self.broj_klastera} klastera', fontweight = 'bold')
        plt.legend()
        plt.show()

    def prikaz_promjene(self, raspon = range(1,10)):
        self.inercija = []
        self.raspon = raspon
        for k in self.raspon:
            self.tmp_ksv = KMeans(n_clusters = k)
            self.tmp_ksv.fit(self.originalna_datoteka[self.koordinate])
            self.inercija.append(self.tmp_ksv.inertia_)

        plt.title('Prikaz stupnja optimizacije po vrijednosti', fontweight = 'bold')
        plt.xlabel('Broj K-vrijednosti')
        plt.ylabel('Razina odstupanja')
        plt.plot(self.raspon, self.inercija)
        plt.show()
