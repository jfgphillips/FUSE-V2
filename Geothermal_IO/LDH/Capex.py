import pandas as pd

class CapexCostFactors(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name="capex", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.installation = self.df['factor'].loc['Installation']
        self.IC = self.df['factor'].loc['Instrumentation_and_control']
        self.EEM = self.df['factor'].loc['Electric_equipment_and_materials']
        self.buildings = self.df['factor'].loc['Buildings']
        self.service_facilities = self.df['factor'].loc['Service_Facilities']
        self.land = self.df['factor'].loc['Land']
        self.FSI = self.df['factor'].loc['Facility_site_improvement']
        self.FCC_contingency = self.df['factor'].loc['FCC_contingency']
        self.working_capital = self.df['factor'].loc['Working_capital']
        return

if __name__ == '__main__':
    test = CapexCostFactors()
    print(test)