import pandas as pd

class worker_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='worker', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.annual_wage = self.df['value'].loc['annual_wage']
        self.no_operators = self.df['value'].loc['no_operators']
        self.supervision = self.df['value'].loc['supervision']
        self.quality_control = self.df['value'].loc['quality_control']
        return

if __name__ == '__main__':
    test = worker_att()
    print(test)