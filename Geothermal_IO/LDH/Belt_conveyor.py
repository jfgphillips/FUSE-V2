import pandas as pd

class BeltConveyor_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='standard_belt_conveyor', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.belt_speed = self.df['value'].loc['belt_speed']
        self.belt_length = int(self.df['value'].loc['belt_length'])
        self.gradient = self.df['value'].loc['gradient']
        self.output = self.df['value'].loc['output']
        self.efficiency = self.df['value'].loc['efficiency']
        print(self.belt_length)
        return

if __name__ == '__main__':
    test = BeltConveyor_att()
    print(test)