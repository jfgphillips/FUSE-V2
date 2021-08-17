import pandas as pd


class Costs_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='costs', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.cost_electricity = self.df['value_low'].loc['electricity_industry']
        self.cost_water = self.df['value_low'].loc['water']
        self.cost_LiOH_H2O = self.df['value_low'].loc['LiOH_H2O']
        self.cost_aluminium_hydroxide = self.df['value_high'].loc['Al(OH)3']
        self.cost_HCl = self.df['value_high'].loc['HCl']
        self.cost_Na2CO3 = self.df['value_high'].loc['Na2CO3']
        self.cost_CO2_high = self.df['value_high'].loc['CO2']
        self.cost_CO2_low = self.df['value_low'].loc['CO2']
        return

if __name__ == '__main__':
    test = Costs_att()
    print(test)