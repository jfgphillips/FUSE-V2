import pandas as pd


class Brine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='brine', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.Li_conc_brine = self.df['value'].loc['Li_conc_brine']  # g/L
        self.brine_specific_enthalpy = self.df['value'].loc['brine_specific_enthalpy']  #KJ/kg
        self.brine_density = self.df['value'].loc['brine_density']  #g/cm^3
        return


if __name__ == '__main__':
    test = Brine_att()
    print(test)