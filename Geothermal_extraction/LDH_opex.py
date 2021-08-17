import pandas as pd
from Geothermal_IO.LDH import *

class LDH_opex(object):
    def __int__(self):
        self.Costs = Costs.UtilityAndChemicals_att()
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.washing = Column_Washing.ColumnExtractionWashing()
        self.stripping = Column_Stripping.ColumnExtractionStripping()
        self.carbonate_processing = LC_processing.LiCarbonateProcessing_att()
        self.carbonate_purification = LC_purification.LiCarbonatePurification_att()
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name="water", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.df.set_index('key', inplace=True)
        self.water_usage = (self.df['value'].loc['process'] + self.chemicals.mass_H2O * 10 ** (-3) +
                            self.washing.H2O_washing_total + self.stripping.H2O_stripping_total)
        self.total_costs_chemicals_and_utility = self.opex()

    def __repr__(self):
        print_opex = f'The total costs for chemicals, water and electricity to produce {self.chemicals.mass_sorbent_year}' \
                     f'kg for one year operation are: {self.total_costs_chemicals_and_utility} $\n' \
                     f'The costs for chemicals, water and electricity per kg of sorbent are:' \
                     f'{self.total_costs_chemicals_and_utility / self.chemicals.mass_sorbent_year}$/kg'

        output = f"{print_opex}"
        return output


    def opex(self):
        """
        gives the total costs for chemicals, water and electricity used for the sorbent synthesis

        """

        cost_chemicals = self.chemicals.mass_LiOH_H2O * 10 ** (-3) * self.Costs.cost_LiOH_H2O + \
                         self.chemicals.mass_aluminium_hydroxide * 10 ** (-3) * self.Costs.cost_aluminium_hydroxide + \
                         self.chemicals.mass_HCl * self.Costs.cost_HCl

        cost_water = self.water_usage * self.Costs.cost_water

        cost_electricity = self.Costs.cost_electricity * self.energy_df['sum'].loc['Sorbent_Synthesis']

        total_costs_chemicals_and_utility = cost_electricity + cost_water + cost_chemicals

        return total_costs_chemicals_and_utility