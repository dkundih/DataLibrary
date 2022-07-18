# coloring.
from colorama import Fore, init 

init()

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

    def __init__(
        self,
        annual_demand_quantity : NumberType = None,
        order_fixed_cost : NumberType = None, 
        annual_holding_cost : NumberType = None,
    ) -> ReturnType:

        '''
        * initial launch.
        '''

        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        
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

        return eoq

# CLI application.
def EOQapp():
    
    '''
    runs as:

        * IDE: vandal.EOQapp()
        * TERMINAL: python -m vandal -e eoq / python -m vandal --entry eoq
    '''

    print(Fore.YELLOW + 'EOQ app is initializing...', Fore.RESET)
    
    # relevant imports.
    import os
    from vandal.misc._meta import (
        __version__,
        __APPversion__,
    )
    os.system('cls')

    # greeting.
    print(Fore.YELLOW + '\n - vandal Command Line Interface Aplikacija © David Kundih -', __APPversion__)
    print(Fore.YELLOW + ' - vandal verzija paketa (HR verzija) -', 'v',__version__, Fore.RESET, '\n')
    
    adq = float(input('Unesi godišnju količinu nabave: '))
    ofc = float(input('Unesi fiksni trošak narudžbe za jedinicu: '))
    ahc = float(input('Unesi godišnji trošak skladištenja po jedinici: '))

    EOQObj = EOQ(annual_demand_quantity = adq, order_fixed_cost = ofc, annual_holding_cost = ahc)
    print('')
    res = EOQObj.execute(filtered = False)
    print(Fore.GREEN + 'Optimalan broj narudžbi godišnje: ', Fore.RESET, adq / res)


# runs module as an app.
if __name__ == '__main__':
    EOQapp()
    
