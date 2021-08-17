import pandas as pd
import math

class Column_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='column', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.column_length = self.df['value'].loc['length']
        self.column_diameter = self.df['value'].loc['diameter']
        self.Li_recovery = self.df['value'].loc['Li_recovery']
        self.bed_volume = self.Bed_volume()
        self.brine_flow_rate = self.bed_volume * self.df['value'].loc['brine_flow_rate']
        self.washing_flow_rate = self.bed_volume * self.df['value'].loc['washing_flow_rate']
        self.stripping_flow_rate = self.bed_volume * self.df['value'].loc['stripping_flow_rate']
        return

    def Bed_volume(self):
        bed_volumn = self.column_length * math.pi * self.column_diameter**2
        return bed_volumn

if __name__ == '__main__':
    test = Column_att()
    print(test)