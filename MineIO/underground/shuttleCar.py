
class shuttleCar_att(object):

    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="shuttle car", skiprows=1)
        self.df.set_index('key', inplace = True)
        self.model = self.df['value'].loc['model']
        self.nameplate_rating = self.df['value'].loc['nameplate rating']
        self.usage = self.df['value'].loc['usage']
        self.maintenance = self.df['value'].loc['maintenance']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        return
