dimport pandas as pd


class Brine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'\data\LDH_attributes.xlsx',
                                sheet_name='brine', skiprows=1) # TODO: chantal, find out how to go back two directories
        self.df.set_index('key', inplace=True)
        self.Li_conc_brine = self.df['value'].loc['LiCl_conc_brine']
        self.brine_specific_enthalpy = self.df['value'].loc['brine_specific_enthalpy']
        self.brine_density = self.df['value'].loc['brine_density']
        return


if __name__ == '__main__':
    print(Brine_att().df)
