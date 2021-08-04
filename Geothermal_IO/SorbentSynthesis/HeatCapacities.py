import pandas as pd
from Geothermal_IO.SorbentSynthesis import Chemicals
from calculators import heatCapacities


class HeatCapacities_att(object):
    def __init__(self):
        self.df = pd.read_excel(r"../data/LDH_attributes.xlsx", sheet_name="heat capacities", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.LiOH_A = self.df['A'].loc['LiOH']
        self.LiOH_B = self.df['B'].loc['LiOH']
        self.LiOH_C = self.df['C'].loc['LiOH']
        self.LiOH_D = self.df['D'].loc['LiOH']
        self.LiOH_E = self.df['E'].loc['LiOH']
        self.HCl_A = self.df['A'].loc['HCl']
        self.HCl_B = self.df['B'].loc['HCl']
        self.HCl_C = self.df['C'].loc['HCl']
        self.HCl_D = self.df['D'].loc['HCl']
        self.HCl_E = self.df['E'].loc['HCl']
        self.H2O_A = self.df['A'].loc['H2O']
        self.H2O_B = self.df['B'].loc['H2O']
        self.H2O_C = self.df['C'].loc['H2O']
        self.H2O_D = self.df['D'].loc['H2O']
        self.H2O_E = self.df['E'].loc['H2O']
        self.hc_aluminium_hydroxide_kg = self.df['A'].loc['Al(OH)3']
        self.df_2 = pd.read_excel(r'../data\LDH_attributes.xlsx',sheet_name="reaction conditions", skiprows=1)
        self.df_2.set_index('key', inplace=True)
        self.temperature = self.df_2['value'].loc['reaction_temp']
        self.chemicals = Chemicals.SorbentSynthesisChemicals_att()
        self.hc_aluminium_hydroxide_mol = self.hc_aluminium_hydroxide_kg * (self.chemicals.RMM_aluminium_hydroxide / 10**3)
        self.hc_LiOH = heatCapacities.Schomate_equation(self.LiOH_A, self.LiOH_B, self.LiOH_C, self.LiOH_D, self.LiOH_E, self.temperature)
        self.hc_H2O = heatCapacities.Schomate_equation(self.H2O_A, self.H2O_B, self.H2O_C, self.H2O_D, self.H2O_E, self.temperature)
        self.hc_HCl = heatCapacities.Schomate_equation(self.HCl_A, self.HCl_B, self.HCl_C, self.HCl_D, self.HCl_E, self.temperature)
        return


# if __name__ == '__main__':
#   test = HeatCapacities_att()





