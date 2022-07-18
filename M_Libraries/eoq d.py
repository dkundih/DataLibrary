# coloring.
from colorama import Fore, init 

init()

import duality

app = duality.DualityApp()

# type hints and annotations.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# package.
class EOQ:

    '''

    (OBJECT INFO)
    -------------

    eg. EOQ = vandal.EOQ()

    vandal.EOQ - main class that stores the data required for an EOQ simulation.
        * takes 3 additional arguments.
            annual_demand_quantity - integer of demanded quantity in a year.
            order_fixed_cost - integer or float presenting the fixed cost of the order.
            annual_holding_cost - cost of holding the goods in a year.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.EOQ.function()

        .execute() - executes the calculation of EOQ over the defined parameters.
            * takes 1 additional argument.
                filtered (defualt: filtered = True) - filters the print option and leaves just the return object.

    EOQapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.EOQapp is an executable function that runs the Command Line Interface of the vandal EOQ module.
        print(help(vandal.EOQapp)) in order to see available features.
        
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

    @app.entry(option_name = 'unos parametara', option_description = 'definiranje parametara')
    def __init__(
        self,
        godišnja_količina_nabave : NumberType = app.store(variable = 'godišnja_količina_nabave', type = 'float'),
        fiksni_trošak_po_jedinici : NumberType = app.store(variable = 'fiksni_trošak_po_jedinici', type = 'float'), 
        trošak_skladištenja_po_jedinici : NumberType = app.store(variable = 'trošak_skladištenja_po_jedinici', type = 'float'),
    ) -> ReturnType:

        '''
        * initial launch.
        '''

        self.annual_demand_quantity = godišnja_količina_nabave
        self.order_fixed_cost = fiksni_trošak_po_jedinici
        self.annual_holding_cost = trošak_skladištenja_po_jedinici
        
        return

    def __str__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    def __repr__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    @app.entry(option_name = 'izračunaj', option_description = 'pokretanje izračuna.', print_val = True)
    def execute(
        self, 
        filtered = True,
        ) -> NumberType:

        '''
        * executes the calculation of EOQ over the defined parameters.

        - filtered (True/False) - filters the data of EOQ initial parameters printed.
        # DEFAULT: EOQ.execute(filtered : BooleanType = True.)
        '''

        if filtered == False:
            print(Fore.GREEN + 'EOQ je postavljen za godišnju količinu nabave od ' + Fore.RESET + f'{self.annual_demand_quantity}' + Fore.GREEN + ' komada, uz fiksni trošak narudžbe po jedinici od ' + Fore.RESET + f'{self.order_fixed_cost}' + Fore.GREEN + ' i troškom skladištenja od ' + Fore.RESET + f'{self.annual_holding_cost}' + Fore.GREEN + ' po jedinici.' + Fore.RESET)
        
        import math
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        eoq = round(eoq, 2)

        if filtered == False:
            print(Fore.GREEN + 'Ekonomična količina narudžbe je:', Fore.RESET, eoq)

        self.eoq = eoq
        return eoq

    @app.entry(option_name = 'optimalna narudžba', option_description = 'prikazuje optimalnu godišnju narudžbu.')
    def optimal_order(self):
        opt_ord = self.annual_demand_quantity / self.eoq
        return print('Optimalan broj narudžbi godišnje:', opt_ord)


# runs module as an app.
if __name__ == '__main__':
    print('\n')
    app.config(type = 'dynamic', queue = True, display_headline = 'RASPOLOŽIVE OPCIJE', display_message = 'UNESI OPCIJU: ', output_message = 'ODABRAO SI: ', choice_message = 'NASTAVI DALJE (Y/N)?: ', enter_message = 'UNESI VARIJABLU ')
