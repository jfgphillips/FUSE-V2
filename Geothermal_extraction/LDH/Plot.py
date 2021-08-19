import matplotlib.pyplot as plt
from Geothermal_extraction.LDH.LDH_energy import LDH_energy
from Geothermal_extraction.LDH import Reactant_flow
from Geothermal_extraction.LDH.LDH_capex import LDH_capex
import pandas as pd

class EnergyPlot(object):
    def __init__(self):
        self.energy = LDH_energy()
        self.rf = Reactant_flow.ReactantFlow()
        self.energy_data = self.energy.energy_df.div(self.rf.LC_purification_product['pure Li2CO3'])  # energy in kWh/t
        self.LDH_capex = LDH_capex()
        self.capex_dict = pd.DataFrame.from_dict(self.LDH_capex.equipment_cost_df)
        self.energy_boxplot()
        return

    def energy_boxplot(self):
        fields = ['Reaction energy', 'Processing energy', 'Transportation energy']
        colours = ['#88CCEE', '#CC6677', '#DDCC77']
        # print(self.energy_data[""])

        myplot = self.energy_data.plot(use_index=True,
                                       kind="bar",
                                       stacked=True,
                                       color=colours, y=fields)

        myplot.set_ylabel('Energy (kWh/tonnes)')
        plt.title('Extraction technique')
        plt.xticks(rotation=0)
        plt.legend(loc=0)
        plt.show()
        return

if __name__ == '__main__':
    test = EnergyPlot()


