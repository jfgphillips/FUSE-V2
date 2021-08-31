import matplotlib.pyplot as plt
from Geothermal_extraction.LDH.LDH_energy import LDH_energy
from Geothermal_extraction.LDH import LDH_opex
from Geothermal_extraction.LDH import Reactant_flow
from Geothermal_extraction.LDH import LDH_capex
from calculators import unitConversions as uC
import pandas as pd

class EnergyPlot(object):
    def __init__(self):
        self.energy = LDH_energy()
        self.rf = Reactant_flow.ReactantFlow()
        self.energy_data = self.energy.energy_df / uC.tonnes(self.rf.LC_purification_product['pure Li2CO3'])  # energy in kWh/t
        self.opex = LDH_opex.LDH_opex()
        self.opex_data = self.opex.opex_df / uC.tonnes(self.rf.LC_purification_product['pure Li2CO3'])  # costs in $/t
        self.LDH_capex = LDH_capex.LDH_capex()
        self.capex_dict = pd.DataFrame.from_dict(self.LDH_capex.equipment_cost_df)
        self.energy_boxplot()
        self.opex_boxplot()
        return

    def energy_boxplot(self):
        fields = ['Reaction energy', 'Processing energy', 'Transportation energy']
        colours = ['#88CCEE', '#CC6677', '#DDCC77']
        labels = ['Reaction', 'Processing', 'Transportation']
        # print(self.energy_data[""])

        myplot = self.energy_data.plot(use_index=True,
                                       kind="bar",
                                       stacked=True,
                                       color=colours, y=fields)

        myplot.set_ylabel('Energy (kWh/tonne)')
        plt.title('Extraction technique')
        plt.xticks(rotation=0)
        plt.legend(labels, loc='upper right')
        plt.show()
        return


    def opex_boxplot(self):
        fields = ['chemical_costs', 'utility_costs', 'labour_costs', 'other']
        colours = ['#88CCEE', '#CC6677', '#DDCC77', '#78EA6C']
        labels = ['Chemicals', 'Utility', 'Labour', 'Other']

        myplot = self.opex_data.plot(use_index=True,
                                     kind="bar",
                                     stacked=True,
                                     color=colours, y=fields)

        myplot.set_ylabel('Opex ($/tonne)')
        plt.title('Extraction technique')
        plt.xticks(rotation=0)
        plt.legend(labels, loc='upper right')
        plt.show()
        return

if __name__ == '__main__':
    test = EnergyPlot()


