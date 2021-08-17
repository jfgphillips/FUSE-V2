import pandas as pd


class UtilityAndChemicals_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\own_code\data\LDH_attributes.xlsx',
                                  sheet_name='costs', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.cost_electricity = self.df['value low'].loc['electricity_industry']
        self.cost_water = self.df['value low'].loc['water']
        self.cost_LiOH_H2O = self.df['value low'].loc['LiOH_H2O']
        self.cost_aluminium_hydroxide = self.df['value high'].loc['Al(OH)3']
        self.cost_HCl = self.df['value high'].loc['HCl']
        return

