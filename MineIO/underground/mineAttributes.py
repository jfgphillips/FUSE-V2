import pandas as pd



class mine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="macro details", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.depth = self.df['value'].loc['depth']
        self.expected_reserves = self.df['value'].loc["proven + probable deposits"]
        self.mine_production = self.df['value'].loc["mine operating production"]
        self.ore_grade = self.df['value'].loc["ore grade"]
        self.ore_density = self.df['value'].loc["location"]
        self.ore_mkt_price = self.df['value'].loc["ore market price"]
        self.mining_usage = self.df['value'].loc["mining operating"]/self.df['value'].loc["period"]
        self.maintenance_usage = self.df['value'].loc['maintenance operating']/self.df['value'].loc['period']
        self.mining_packages = self.df['value'].loc["mining packages"]
        return


