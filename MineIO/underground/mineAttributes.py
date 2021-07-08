
class mine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="macro details", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.depth = self.df['value'].loc['depth']
        self.expected_reserves = self.df['value'].loc["proven + probable deposits"]
        self.mine_production = self.df['value'].loc["mine operating production"]
        self.ore_grade = self.df['value'].loc["ore grade"]
        self.ore_density = self.df['value'].loc["location"]
        self.ore_mkt_price = self.df['value'].loc["ore market price"]
        return

