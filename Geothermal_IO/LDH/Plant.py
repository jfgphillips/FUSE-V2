import pandas as pd


class Plant_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='plant', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.brine_flow_day = self.df['value'].loc['brine_flow_day']  # m^3/day
        self.plant_uptime = self.df['value'].loc['plant_uptime']  # hours/year
        self.plant_lifetime = self.df['value'].loc['plant_lifetime']  # years
        return

if __name__ == '__main__':
    test = Plant_att()
    print(test)