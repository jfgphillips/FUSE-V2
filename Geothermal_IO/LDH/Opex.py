import pandas as pd


class Costs_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='cost_chemicals', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.cost_electricity = self.df['value_low'].loc['electricity_industry']
        self.cost_water = self.df['value_low'].loc['water']
        self.cost_LiOH_H2O = self.df['value_low'].loc['LiOH_H2O']
        self.cost_aluminium_hydroxide = self.df['value_high'].loc['Al(OH)3']
        self.cost_HCl = self.df['value_high'].loc['HCl']
        self.cost_Na2CO3 = self.df['value_high'].loc['Na2CO3']
        self.cost_CO2_high = self.df['value_high'].loc['CO2']
        self.cost_CO2_low = self.df['value_low'].loc['CO2']
        self.df_2 = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                  sheet_name='opex', skiprows=1)
        self.df_2.set_index('key', inplace=True)
        self.maintenance_material = self.df_2['factor'].loc['maintenance_material']
        self.operating_supplies = self.df_2['factor'].loc['operating_supplies']
        self.contingency_1 = self.df_2['factor'].loc['contingency_1']
        self.contingency_2 = self.df_2['factor'].loc['contingency_2']
        self.property_taxes = self.df_2['factor'].loc['Property_taxes']
        self.insurance = self.df_2['factor'].loc['Insurance']
        self.fringe_benefits = self.df_2['factor'].loc['Fringe_benefits']
        self.overhead = self.df_2['factor'].loc['Overhead']
        self.admin = self.df_2['factor'].loc['Administrative']
        self.marketing = self.df_2['factor'].loc['Marketing']
        self.financing = self.df_2['factor'].loc['Financing']
        self.R_D = self.df_2['factor'].loc['R&D']
        return

if __name__ == '__main__':
    test = Costs_att()
    print(test)