import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LRbuiltin
from sklearn.model_selection import train_test_split

class LinearnaRegresija:

    def __init__(self, podaci, x, y):
        self.podaci = podaci
        self.x = self.podaci[x]
        self.y = self.podaci[y]

    def prikaz_grafa(self, boja = 'g', naslov = 'Inicijalni prikaz'):
        plt.scatter(x = self.x, y = self.y, color = boja)
        plt.title(naslov)
        plt.show()
        return

    def podjela_seta(self, omjer_testa : float = 0.2, slučajno_stanje : int = 50):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size = omjer_testa, random_state = slučajno_stanje)
        return

    def prikaz_procesa(self, tr_naslov = 'Uzorak treniranja', te_naslov = 'Uzorak testiranja', tr_boja = 'r', te_boja = 'g'):
        plt.scatter(self.x_train, self.y_train, label = tr_naslov, color = tr_boja, alpha=.3)
        plt.scatter(self.x_test, self.y_test, label = te_naslov, color = te_boja, alpha=.3)
        plt.legend()
        plt.title('Proces treniranja i testiranja modela', fontweight = 'bold')
        plt.show()

    def prikaz_linearne_regresije(self):
        self.LR = LRbuiltin()
        self.LR.fit(self.x_train.values.reshape(-1,1), self.y_train.values)
        predviđanje = self.LR.predict(self.x_test.values.reshape(-1,1))
        plt.plot(self.x_test, predviđanje, label = 'Linearna regresija',)
        plt.scatter(self.x_test, self.y_test, label = 'Vrijednosti', color = 'darkkhaki', alpha = 0.5)
        plt.legend()
        plt.title('Linearna regresija', fontweight = 'bold')
        plt.show()

    def procjena_varijable(self, vrijednost, prikaz = True):
        self.vrijednost = vrijednost
        procjena = self.LR.predict(np.array([[vrijednost]]))[0]
        if prikaz == True:
            return print(f'Odgovarajuća vrijednost za {vrijednost} je {procjena}.')
        else:
            return procjena

    def preciznost_modela(self, prikaz = True):
        preciznost = self.LR.score(self.x_test.values.reshape(-1,1), self.y_test.values)
        if prikaz == True:
            return print(f'Uspješnost modela iznosi {preciznost}.')
        else:
            return preciznost
    
    def formula(self, prikaz = True):
        reformat_coef = float(self.LR.coef_)
        if prikaz == True:
            return print(f'Formula modela je y = {self.vrijednost} * {reformat_coef} + {self.LR.intercept_}')
        else:
            return f'Formula modela je y = {self.vrijednost} * {reformat_coef} + {self.LR.intercept_}'
