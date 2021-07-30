import pandas as pd



class mine_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="macro details", skiprows=1)
        df.set_index('key', inplace=True)
        self.depth = df['value'].loc['depth']
        self.expected_reserves = df['value'].loc["proven + probable deposits"]
        self.mine_production = df['value'].loc["mine operating production"]
        self.ore_grade = df['value'].loc["ore grade"]
        self.ore_density = df['value'].loc["location"]
        self.ore_mkt_price = df['value'].loc["ore market price"]
        self.mining_operating = df['value'].loc["mining operating"]
        self.mining_usage = df['value'].loc["mining operating"]/df['value'].loc["period"]
        self.maintenance_usage = df['value'].loc['maintenance operating']/df['value'].loc['period']
        self.mining_packages = df['value'].loc["mining packages"]
        self.conversion_efficiency = df['value'].loc['conversion efficiency']
        return


