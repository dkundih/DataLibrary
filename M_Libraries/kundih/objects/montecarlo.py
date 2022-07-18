# coloring.
from colorama import Fore, init
import numpy as np

init()

# type hints and annotations.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# package.
class MonteCarlo:

    '''

    (OBJECT INFO)
    -------------

    eg. MonteCarlo = vandal.MonteCarlo()

    vandal.MonteCarlo - main class that stores the simulation data.

        * takes 5 additional arguments.
            list_of_values - pandas dataframe of values.
            time_seq - desired time sequence.
            num_sims - desired number of simulation iterations.
            ref_col (default: ref_col = 0) - column index of the dictionary values.
            ref_row (default: ref_row = 0) - row index on which the starting point of the simulation is created.
        * Requirements:
            data stored as dictionary of key, value pair | list | numpy array | pandas DataFrame.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.MonteCarlo.function()

        .execute() - executes a Monte Carlo simulation on a defined data set.
            * takes 1 additional argument.
                filtered (defualt: filtered = True) - filters the print option and leaves just the return object.

        .graph() - plots the Monte Carlo simulation on a graph.
            * takes 5 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True).
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.

        .get_risk() - calculates the risk of value decrease over time.
            * takes 1 additional argument.
                risk_sims (default: risk_sims = 5000) - number of simulations to perform the risk percantage.

        .get_stats() - shows the statistics of the Monte Carlo simulation.
            * takes no additional arguments.

        .get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.
            * takes no additional arguments.

        .hist() - plots the histogram of Monte Carlo simulation.
            * takes 7 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), set_bins = None, perform_block = True, method = 'b').
            If method = 'e' is chosen, no customization arguments apply.
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.
                method - default method is Basic histogram and it's performed by automation. In order to plot Empirical rule histogram add method = 'e' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.
                set_bins - sets the amount of bins of the histogram. (default: set_bins = self.time_seq)
            * automatically executes the .get_stats() function in order to get standard deviation for the Empirical rule plotting.

    MCapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.MCapp is an executable function that runs the Command Line Interface of the vandal MonteCarlo module.
        print(help(vandal.MCapp)) in order to see available features.
        
    '''

    # metadata of the used library.
    from vandal.misc._meta import (
        __author__,
        __copyright__,
        __credits__,
        __license__,
        __version__,
        __documentation__,
        __contact__,
        __donate__,
        __APPversion__,
    )

    def __init__(
        self, 
        lista_vrijednosti : NumberVectorAlike = None, 
        period : IntegerType = None, 
        broj_simulacija : IntegerType = None,
        referentni_stupac : IntegerType = 0, 
        referentni_redak : IntegerType = 0,
        ) -> ReturnType:

        '''
        * initial launch.
        '''

        self.list_of_values = lista_vrijednosti
        self.time_seq = period
        self.num_sims = broj_simulacija
        self.ref_col = referentni_stupac
        self.ref_row = referentni_redak

        return 

    def __str__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    def __repr__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    def izračunaj(
        self,
        filter : BooleanType = True,
        ) -> NumberArrayAlike:

        '''
        * executes a Monte Carlo simulation on a defined data set.

        - filtered (True/False) - filters the data setup print and warnings.
        # DEFAULT: MonteCarlo.execute(filtered : BooleanType = True.)
        '''

        if filter == False:
            print(Fore.GREEN + f'Monte Carlo simulacija postavljena za {self.num_sims} simulacija u periodu od {self.time_seq} vremenskih jedinica.' + Fore.RESET)
            print(Fore.RED + 'OPREZ: Prihvatljivi su podaci s razumnom standardnom devijacijom zbog izbjegavanja mogućeg eksponencijalnog rasta.' + Fore.RESET)
        
        from vandal.hub.toolkit import random_value
        import pandas as pd

        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.

        try:
            self.list_of_values = pd.DataFrame(self.list_of_values)
            self.list_of_values = self.list_of_values.iloc[:, self.ref_col]
        except:
            raise KeyError('Impossible to reach a defined key, value pair. Data types supported: dictionary, list, numpy array, pandas DataFrame. Make sure to set index row_col on an existing field. Must be of type: int.')

        today_value = self.list_of_values.iloc[self.ref_col]
        data = pd.DataFrame()
        loading = 0

        for num_sim in range(self.num_sims):
            rand_change = self.list_of_values.pct_change().std()
            count = 0
            index_array = []
            index_array += [today_value + (today_value * np.random.normal(0, rand_change))]

            for num_day in range(self.time_seq):
                rand_change = self.list_of_values.pct_change().std()
                if count == self.time_seq:
                    break
                index_array += [index_array[count] + (today_value * np.random.normal(0, rand_change))]
                count += 1
                
            loading += 1
            print(end = '\r')
            print(loading, 'iteracija od', self.num_sims, 'izvršeno do sada', end = '')

            data[num_sim] = index_array
        print(end = '\r')
        print(Fore.GREEN + 'Monte Carlo simulacija postavljena i spremna za iscrtavanje.' + Fore.RESET)
        self.results = data

        return data

    def prikaži_promjenu(
        self,
        ) -> NumberArrayAlike:

        '''
        * shows the percentage of Monte Carlo simulation value change for every iteration.
        '''

        return self.results.pct_change()

    def izračunaj_rizik(
        self, 
        simulacije : IntegerType = 5000,
        ) -> NumberType:

        '''
        * calculates the risk of negative values occuring.

        - risk_sims - number of simulations to run risk evaluation on.
        # DEFAULT: MonteCarlo.get_risk(risk_sims : IntegerType = 5000.)
        '''

        import random
        import pandas as pd

        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.

        today_value = self.list_of_values.iloc[self.ref_row]
        percent_change = self.list_of_values.pct_change()
        data = pd.DataFrame()
        smaller = []

        for num_sim in range(simulacije):
            random_change = random.choice(percent_change)
            index_array = []
            index_array += [today_value * (1 + (random_change))]
            data[num_sim] = index_array

            for sim in data[num_sim]:
                if sim < today_value:
                    smaller += [sim]
        NRisk = len(smaller) / num_sim * 100
        assert (NRisk < 100), '\nTime sequence and/or number of iterations are too low for the proper risk calculation.'

        return print('Rizik za ovu opciju je', str(round(NRisk, 2)) + '%.')

    def prikaži_graf(
        self, 
        naslov : StringType = 'Monte Carlo simulacija', 
        x_naslov : StringType = 'X axis', 
        y_naslov : StringType = 'Y axis', 
        plot_size : TupleType = (25,10), 
        perform_block : BooleanType = True,
        ) -> GraphType:

        '''
        * plots the Monte Carlo simulation on a graph.

        - graph title - sets a graph title.
        - x_title - sets an x axis title.
        - y_title - sets and y axis title.
        - plot_size - sets a size of graph in a tuple (eg. (x,y).)
        - perform_block (True/False) - customizable wheel to disable block in some IDEs.
        # DEFAULT: MonteCarlo.graph(graph_title : StringType = 'Monte Carlo simulation', x_title : StringType = 'X axis', y_title : StringType = 'Y axis', plot_size : TupleType = (25,10), perform_block : BooleanType = True.)
        '''

        print(Fore.GREEN + '\nZapočelo je iscrtavanje MonteCarlo simulacije na grafu.' + Fore.RESET)
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('diplomski rad (c) David Kundih, 2022', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(naslov, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_naslov, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_naslov, fontsize = 18, weight = 'semibold')
        plt.show(block = perform_block)
        print(Fore.GREEN + 'Iscrtavanje Monte Carlo simulacije izvršeno.' + Fore.RESET)

        return

    def prikaži_statistiku(
        self,
        ) -> AnyArrayAlike:

        '''
        * shows the statistics of the Monte Carlo simulation.
        '''
        
        import numpy as np
        import pandas as pd

        mean_value = np.mean(self.results.loc[self.time_seq])
        mean_value = round((mean_value),2)
        standard_deviation = round(np.std(self.results.loc[self.time_seq]),2)
        standard_deviation = round((standard_deviation),2)
        maximum_value = np.max(self.results.loc[self.time_seq])
        maximum_value = round((maximum_value),2)
        minimum_value = np.min(self.results.loc[self.time_seq])
        minimum_value = round((minimum_value),2)
        self.standard_deviation = standard_deviation
        self.mean_value = mean_value

        stats = {
            'Srednja vrijednost' : mean_value, 
            'Standardna devijacija' : standard_deviation, 
            'Maximalna vrijednost' : maximum_value, 
            'Minimalna vrijednost' : minimum_value,
            }

        stats = pd.DataFrame(stats, index = ['Statistika'])
        stats = stats.transpose()

        return stats 

    def prikaži_histogram(
        self, 
        naslov : StringType = 'Histogram vrijednosti', 
        x_naslov : StringType = 'X axis', 
        y_naslov : StringType = 'Y axis', 
        plot_size : TupleType = (25,10), 
        perform_block : BooleanType = True,
        set_bins : IntegerType = None,
        **method : StringType,
        ) -> GraphType:

        '''
        * plots the histogram of Monte Carlo simulation.

        - graph title - sets a graph title.
        - x_title - sets an x axis title.
        - y_title - sets and y axis title.
        - plot_size - sets a size of graph in a tuple (eg. (x,y).)
        - perform_block (True/False) - customizable wheel to disable block in some IDEs.
        - set_bins - sets amount of histogram bins.
        - **method ('e' - empirical, 'b' - basic)- method of a histogram.
        # DEFAULT: MonteCarlo.hist(graph_title : StringType = 'Histogram of value frequencies', x_title : StringType = 'X axis', y_title : StringType = 'Y axis', plot_size : TupleType = (25,10), perform_block : BooleanType = True,set_bins : IntegerType = None, **method : StringType.)
        '''

        self.prikaži_statistiku()
        std_plus = self.mean_value + self.standard_deviation
        std_minus = self.mean_value - self.standard_deviation
        std_plus2 = self.mean_value + (self.standard_deviation * 2)
        std_minus2 = self.mean_value - (self.standard_deviation * 2)
        std_plus3 = self.mean_value + (self.standard_deviation * 3)
        std_minus3 = self.mean_value - (self.standard_deviation * 3)

        if self.time_seq > 50:
            print(Fore.RED + 'OPREZ: Definirani period uvelike utječe na trajanje izvršavanja ove funkcije.\n' + Fore.RESET)

        print(Fore.GREEN + 'Inicijalizirano iscrtavanje histograma...' + Fore.RESET)
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('diplomski rad (c) David Kundih, 2022', fontsize = 14, weight = 'regular', loc = 'right')

        if method.get("method") != "e":
            print(Fore.GREEN + 'ODABRANI MODEL: Osnovni histogram model.' + Fore.RESET)
            plt.suptitle(naslov, fontsize = 25, weight = 'bold')

        if method.get("method") == "e":
            print(Fore.GREEN + 'ODABRANI MODEL: Model Empirijskog pravila.' + Fore.RESET)
            plt.suptitle('Podjela podataka prema empirijskom pravilu', fontsize = 25, weight = 'bold')
            plt.axvline(x = std_plus, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus, color = 'r', linestyle = 'dashed')
            plt.axvline(x = self.mean_value, color = 'k', linestyle = 'solid')
            plt.axvline(x = std_plus2, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus2, color = 'r', linestyle = 'dashed')
            plt.axvline(x = std_plus3, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus3, color = 'r', linestyle = 'dashed')

        if set_bins == None:
            set_bins = self.time_seq
            
        plt.hist(self.results, bins = set_bins, ec = 'm')
        plt.xlabel(x_naslov, weight = 'semibold')
        plt.ylabel(y_naslov, weight= 'semibold')
        plt.show(block = perform_block)
        print(Fore.GREEN + 'Iscrtavanje histograma je završilo.', Fore.RESET)

        return
